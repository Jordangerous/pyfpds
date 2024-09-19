from pyfpds import Contracts

c = Contracts()

# Filter by created on
records = c.get(created_on="[2024/08/19,2024/09/19]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
