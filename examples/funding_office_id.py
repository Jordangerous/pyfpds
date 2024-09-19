from pyfpds import Contracts

c = Contracts()

# Filter by funding office id
records = c.get(funding_office_id="FA7014", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
