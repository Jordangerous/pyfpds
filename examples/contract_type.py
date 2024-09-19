from pyfpds import Contracts

c = Contracts()

# Filter by contract type
records = c.get(contract_type="Definitive Contract", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
