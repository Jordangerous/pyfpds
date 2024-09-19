from pyfpds import Contracts

c = Contracts()

# Filter by modification number
records = c.get(modification_number="P00001", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
