from pyfpds import Contracts

c = Contracts()

# Filter by legislative mandates
records = c.get(legislative_mandates="Small Business Set-Aside", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
