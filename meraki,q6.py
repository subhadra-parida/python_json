#Python object key unique key value ko access karne ka program likho?
import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print(python_obj)
json_obj = json.loads(python_obj)
print(json_obj) 

