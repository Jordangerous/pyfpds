from pyfpds import Contracts

c = Contracts()

# Filter by socioeconomic indicators
records = c.get(socioeconomic_indicators="Small Disadvantaged Business", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
