from pyfpds import Contracts

c = Contracts()

# Filter by vendor zip
records = c.get(vendor_zip="22202", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
