from pyfpds import Contracts

c = Contracts()

# Filter by vendor country name
records = c.get(vendor_country_name="United States", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
