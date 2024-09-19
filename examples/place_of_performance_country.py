from pyfpds import Contracts

c = Contracts()

# Filter by place of performance country
records = c.get(place_of_performance_country="USA", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
