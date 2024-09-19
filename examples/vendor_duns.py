from pyfpds import Contracts

c = Contracts()

# Filter by vendor duns
records = c.get(vendor_duns="123456789", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
