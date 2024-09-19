from pyfpds import Contracts

c = Contracts()

# Filter by product or service description
records = c.get(product_or_service_description="IT and Telecom - Other IT and Telecommunications", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
