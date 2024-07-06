import json

# create a python dictionary
student_data = {
    'name': 'Martha Aya',
    'age': 22,
    'state': 'California',
    'City': 'Los Angeles',
    'marital_status': 'single'
}

# Serialization: Converting a Python Object to JSON string
json_string = json.dumps(student_data)

# see structure of a JSON string output
print(json_string)

# converting JSON string back to Python

python_obj = json.loads(json_string)

print(python_obj)
