# Q.1 Json data ko python object main convert karne ka program likho?.

import json
data ='{"name": "Subha","From":"Odisha","age":21 }'
print(type(data))
a = json.loads(data)
print(a)
print(type(a))


