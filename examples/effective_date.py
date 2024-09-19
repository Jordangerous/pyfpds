from pyfpds import Contracts

c = Contracts()

# Filter by effective date
records = c.get(effective_date="[2024/06/01,2024/06/30]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
