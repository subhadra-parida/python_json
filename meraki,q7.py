# Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
dict={"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male","Age":29}
with open ("Json_file.json", "w") as file:
    json.dump(dict,file,indent = 6)
    print(dict)

 




#  Json_file.json:-{
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }