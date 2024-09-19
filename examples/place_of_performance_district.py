from pyfpds import Contracts

c = Contracts()

# Filter by place of performance district
records = c.get(place_of_performance_district="VA-08", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
