from pyfpds import Contracts

c = Contracts()

# Filter by vendor country code
records = c.get(vendor_country_code="USA", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
