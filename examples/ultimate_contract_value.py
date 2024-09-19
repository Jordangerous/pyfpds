from pyfpds import Contracts

c = Contracts()

# Filter by ultimate contract value
records = c.get(ultimate_contract_value="1000000", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
