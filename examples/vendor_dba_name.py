from pyfpds import Contracts

c = Contracts()

# Filter by vendor dba name
records = c.get(vendor_dba_name="Tech Innovations LLC", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
