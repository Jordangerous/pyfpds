from pyfpds import Contracts

c = Contracts()

# Filter by naics description
records = c.get(naics_description="Computer Systems Design Services", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
