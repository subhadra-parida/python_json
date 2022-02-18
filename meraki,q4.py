# Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
json_str = {'4': 5, '6': 7, '1': 3, '2': 4}
for key in sorted(json_str):
    print(json.dumps(json_str, sort_keys=True, indent=4))




