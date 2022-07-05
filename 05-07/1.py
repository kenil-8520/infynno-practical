import json

data = '[{"Name":"john","Age":"","DOB":"04/02/2000"},' \
 			'{"Name":"Abhishek","Age":"","DOB":""},' \
 			'{"Name":"Abhishek","Age":"","DOB":""},' \
 			'{"Name":"Abhishek","Age":"","DOB":""},' \
 			'{"Name":"Abhishek","Age":"","DOB":""}]' \

x = json.loads(data)
# print(x)

print(json.dumps(x, indent = 1))

