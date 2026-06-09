import json

#de json a python
x= '{"name": "daniel" , "age":18 , "city":"Tibasosa"}'

#some x:
y= json.loads(x)# combersion de json a python
#the result is a Pytohn dictionary:
print(y)

#se python a json

x= {
    "name": "jhon",
    "age": 18,
    "city": "bogota"
}

#comvertir a json
y= json.dumps(x) #combertir de python a json

print(y)