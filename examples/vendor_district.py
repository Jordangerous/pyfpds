from pyfpds import Contracts

c = Contracts()

# Filter by vendor district
records = c.get(vendor_district="VA-08", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
