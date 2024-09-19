from pyfpds import Contracts

c = Contracts()

# Filter by idv agency id
records = c.get(idv_agency_id="1700", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
