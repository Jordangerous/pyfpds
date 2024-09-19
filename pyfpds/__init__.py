import os
import json
import re
import requests
import xmltodict
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import OrderedDict
import warnings

warnings.filterwarnings('ignore')

field_map = {
    'piid': 'PIID',
    'idv_piid': 'REF_IDV_PIID',
    'idv_agency_id': 'REF_IDV_AGENCY_ID',
    'modification_number': 'MODIFICATION_NUMBER',
    'contracting_agency_id': 'CONTRACTING_AGENCY_ID',
    'contracting_agency_name': 'CONTRACTING_AGENCY_NAME',
    'contracting_office_id': 'CONTRACTING_OFFICE_ID',
    'contracting_office_name': 'CONTRACTING_OFFICE_NAME',
    'funding_agency_id': 'FUNDING_AGENCY_ID',
    'funding_office_id': 'FUNDING_OFFICE_ID',
    'funding_office_name': 'FUNDING_OFFICE_NAME',
    'agency_code': 'AGENCY_CODE',
    'agency_name': 'AGENCY_NAME',
    'department_id': 'DEPARTMENT_ID',
    'department_name': 'DEPARTMENT_NAME',
    'last_modified_date': 'LAST_MOD_DATE',
    'last_modified_by': 'LAST_MODIFIED_BY',
    'award_completion_date': 'AWARD_COMPLETION_DATE',
    'created_on': 'CREATED_DATE',
    'date_signed': 'SIGNED_DATE',
    'effective_date': 'EFFECTIVE_DATE',
    'estimated_completion_date': 'ESTIMATED_COMPLETION_DATE',
    'obligated_amount': 'OBLIGATED_AMOUNT',
    'ultimate_contract_value': 'ULTIMATE_CONTRACT_VALUE',
    'contract_pricing_type': 'TYPE_OF_CONTRACT_PRICING',
    'award_status': 'AWARD_STATUS',
    'contract_type': 'CONTRACT_TYPE',
    'created_by': 'CREATED_BY',
    'description': 'DESCRIPTION_OF_REQUIREMENT',
    'modification_reason': 'REASON_FOR_MODIFICATION',
    'legislative_mandates': 'LEGISLATIVE_MANDATES',
    'local_area_setaside': 'LOCAL_AREA_SET_ASIDE',
    'socioeconomic_indicators': 'SOCIO_ECONOMIC_INDICATORS',
    'multiyear_contract': 'MULTIYEAR_CONTRACT',
    'national_interest_code': 'NATIONAL_INTEREST_CODE',
    'national_interest_description': 'NATIONAL_INTEREST_DESCRIPTION',
    'naics_code': 'PRINCIPAL_NAICS_CODE',
    'naics_description': 'NAICS_DESCRIPTION',
    'product_or_service_code': 'PRODUCT_OR_SERVICE_CODE',
    'product_or_service_description': 'PRODUCT_OR_SERVICE_DESCRIPTION',
    'place_of_performance_district': 'POP_CONGRESS_DISTRICT_CODE',
    'place_of_performance_country': 'POP_CONGRESS_COUNTRY',
    'place_of_performance_state': 'POP_STATE_NAME',
    'vendor_city': 'VENDOR_ADDRESS_CITY',
    'vendor_district': 'VENDOR_CONGRESS_DISTRICT_CODE',
    'vendor_country_code': 'VENDOR_ADDRESS_COUNTRY_CODE',
    'vendor_country_name': 'VENDOR_ADDRESS_COUNTRY_NAME',
    'vendor_duns': 'VENDOR_DUNS_NUMBER',
    'vendor_dba_name': 'VENDOR_DOING_BUSINESS_AS_NAME',
    'vendor_name': 'VENDOR_NAME',
    'vendor_state_code': 'VENDOR_ADDRESS_STATE_CODE',
    'vendor_state_name': 'VENDOR_ADDRESS_STATE_NAME',
    'vendor_zip': 'VENDOR_ADDRESS_ZIP_CODE',
}

class Contracts:
    feed_url = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q="
    feed_size = 10
    query_url = ''
   
    def __init__(self, logger=None):
        # Point logger to a log function, print by default
        self.log = logger if logger else print

    def pretty_print(self, data):
        self.log(json.dumps(data, indent=4))

    def convert_params(self, params):
        new_params = {}
        for k, v in params.items():
            new_params[field_map[k]] = v
        return new_params

    def combine_params(self, params):
        return " ".join(f"{k}:{v}" for k, v in params.items())

    def process_data(self, data):
        # Make a list if it's a dict for consistency
        if isinstance(data, dict):
            data = [data]
        return data

    def save_data(self, data, directory, filename):
        # Ensure directory exists
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        self.log(f"Saved data to {filepath}")

    def get_last(self, params):
        """
        Fetches the 'last' page URL and extracts the last 'start' value.
        """
        try:
            url = f"{self.feed_url}{params}&start=0"
            self.log(f"Querying {url} for the last page")
            resp = requests.get(url, timeout=60, verify=False)
            self.query_url = resp.url
            self.log(f"Finished querying {resp.url}")
            resp_data = xmltodict.parse(resp.text, process_namespaces=True, namespaces={
                'http://www.fpdsng.com/FPDS': None,
                'http://www.w3.org/2005/Atom': None
            })

            # Extract 'last' page URL
            links = resp_data['feed']['link']
            last_link = next(link for link in links if link['@rel'] == 'last')
            last_start_param = re.search(r'start=(\d+)', last_link['@href'])
            return int(last_start_param.group(1)) + 10 if last_start_param else 0
        except (KeyError, StopIteration, AttributeError, Exception) as e:
            self.log(f"Error extracting the last page: {e}")
            return 0

    def get(self, num_records=100, order='desc', save_dir=None, **kwargs):
        params = self.combine_params(self.convert_params(kwargs))
        data = []
        i = 0

        def fetch_data(start):
            try:
                url = f"{self.feed_url}{params}&start={start}"
                self.log(f"Querying {url}")
                resp = requests.get(url, timeout=60, verify=False)
                self.query_url = resp.url
                self.log(f"Finished querying {resp.url}")
                resp_data = xmltodict.parse(resp.text, process_namespaces=True, namespaces={
                    'http://www.fpdsng.com/FPDS': None, 
                    'http://www.w3.org/2005/Atom': None
                })
                return self.process_data(resp_data['feed']['entry']), start
            except KeyError:
                self.log("No results for query")
                return [], start
            except Exception as e:
                self.log(f"Error fetching data: {e}")
                return [], start

        # Determine the last page if needed
        if num_records == "all":
            last_page_index = self.get_last(params)
            if last_page_index:
                num_records = last_page_index

        with ThreadPoolExecutor() as executor:
            futures = []

            # Schedule the first set of tasks
            while i < num_records:
                futures.append(executor.submit(fetch_data, i))
                i += 10
                if num_records != "all" and i >= num_records:
                    break

            # Collect the results as they complete
            for future in as_completed(futures):
                processed_data, start_index = future.result()
                data.extend(processed_data)

                # Save data if a directory is provided
                if save_dir:
                    self.save_data(processed_data, save_dir, f"{start_index}.json")

                # If a result has less than 10 records, break out of the loop
                if len(processed_data) < 10:
                    break

        return data
