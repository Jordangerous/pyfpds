from pyfpds import Contracts

c = Contracts()

# Filter by local area setaside
records = c.get(local_area_setaside="N/A", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
