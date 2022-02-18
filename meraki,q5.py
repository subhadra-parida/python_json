#Json string ko check karo ki bo complex object contain karti hai ya nahi?
import json
data ='{"name": "Subha","From":"Odisha","age":21 ,"complex":3j+3}'
print(data)
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# import json 
# def is_complex_num(objct):
#     if '_complex_' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# complex_object =json.loads('{"_complex_": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print(complex_object)
# print("Without complex object: ",simple_object)