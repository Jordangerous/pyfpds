from pyfpds import Contracts

c = Contracts()

# Filter by multiyear contract
records = c.get(multiyear_contract="Yes", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
