from pyfpds import Contracts

c = Contracts()

# Filter by last modified date
records = c.get(last_modified_date="[2024/09/01,2024/09/19]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
