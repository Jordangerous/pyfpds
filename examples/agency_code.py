from pyfpds import Contracts

c = Contracts()

# Filter by agency code
records = c.get(agency_code="9700", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
