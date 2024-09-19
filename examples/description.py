from pyfpds import Contracts

c = Contracts()

# Filter by description
records = c.get(description="IT Support Services", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
