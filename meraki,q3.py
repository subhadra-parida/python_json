# Q.3 Python object ko json string mai convert karne ka program likho?

import json
dict={"name": "Subha","From":"Odisha","age":21 }
new=json.loads('{"name":"Subha","From":"Odisha","age":21}')
print(new)
print(type(new))

