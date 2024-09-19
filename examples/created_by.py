from pyfpds import Contracts

c = Contracts()

# Filter by created by
records = c.get(created_by="jdoe@example.com", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
