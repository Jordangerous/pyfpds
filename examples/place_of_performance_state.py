from pyfpds import Contracts

c = Contracts()

# Filter by place of performance state
records = c.get(place_of_performance_state="Virginia", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
