from pyfpds import Contracts

c = Contracts()

# Filter by award completion date
records = c.get(award_completion_date="[2025/09/01,2025/09/30]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
