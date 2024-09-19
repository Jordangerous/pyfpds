from pyfpds import Contracts

c = Contracts()

# Filter by contracting office name
records = c.get(contracting_office_name="Air Force Life Cycle Management Center", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
