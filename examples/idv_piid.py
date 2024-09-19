from pyfpds import Contracts

c = Contracts()

# Filter by idv piid
records = c.get(idv_piid="W15P7T05DC402", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
