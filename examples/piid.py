from pyfpds import Contracts

c = Contracts()

# Filter by piid
records = c.get(piid="FA865014M5002", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
