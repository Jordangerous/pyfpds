from pyfpds import Contracts

c = Contracts()

# Filter by contracting office id
records = c.get(contracting_office_id="FA8501", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
