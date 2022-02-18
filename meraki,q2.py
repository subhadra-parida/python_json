# Q.2 Python object ko json data main convert karne ka program likho?

import json
dict={"name": "Subha","From":"Odisha","age":21 }
with open ("Shubha.json", "w") as file:
    json.dump(dict,file,indent = 0)
    print(dict)
