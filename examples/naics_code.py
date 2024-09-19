from pyfpds import Contracts

c = Contracts()

# Filter by naics code
records = c.get(naics_code="541512", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
