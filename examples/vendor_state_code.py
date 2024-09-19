from pyfpds import Contracts

c = Contracts()

# Filter by vendor state code
records = c.get(vendor_state_code="VA", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
