from pyfpds import Contracts

c = Contracts()

# Filter by award status
records = c.get(award_status="Active", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
