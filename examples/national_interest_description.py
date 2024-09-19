from pyfpds import Contracts

c = Contracts()

# Filter by national interest description
records = c.get(national_interest_description="National Defense", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
