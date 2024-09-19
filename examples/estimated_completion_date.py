from pyfpds import Contracts

c = Contracts()

# Filter by estimated completion date
records = c.get(estimated_completion_date="[2026/01/01,2026/12/31]", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
