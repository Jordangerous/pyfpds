from pyfpds import Contracts

c = Contracts()

# Filter by contract pricing type
records = c.get(contract_pricing_type="Firm Fixed Price", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
