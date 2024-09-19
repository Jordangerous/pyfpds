from pyfpds import Contracts

c = Contracts()

# Filter by contracting agency id
records = c.get(contracting_agency_id="9700", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
