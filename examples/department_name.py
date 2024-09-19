from pyfpds import Contracts

c = Contracts()

# Filter by department name
records = c.get(department_name="Department of the Navy", num_records="all")

for record in records:
    r = record.get('content')
    c.pretty_print(r)
    
print("Length: {0}".format(len(records)))
