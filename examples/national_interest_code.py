from pyfpds import Contracts

c = Contracts()

# Filter by national interest code
records = c.get(national_interest_code="001", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
