from pyfpds import Contracts

c = Contracts()

# Filter by date signed
records = c.get(date_signed="[2024/09/09,2024/09/19]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
