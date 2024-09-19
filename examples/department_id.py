from pyfpds import Contracts

c = Contracts()

# Filter by department id
records = c.get(department_id="020", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
