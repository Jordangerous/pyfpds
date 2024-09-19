from pyfpds import Contracts

c = Contracts()

# Filter by product or service code
records = c.get(product_or_service_code="D399", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
