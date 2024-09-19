from pyfpds import Contracts

c = Contracts()

# Filter by funding agency id
records = c.get(funding_agency_id="1700", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
