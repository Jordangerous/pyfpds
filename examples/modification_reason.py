from pyfpds import Contracts

c = Contracts()

# Filter by modification reason
records = c.get(modification_reason="Funding Increase", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
