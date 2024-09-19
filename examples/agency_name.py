from pyfpds import Contracts

c = Contracts()

# Filter by agency name
records = c.get(agency_name="General Services Administration", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
