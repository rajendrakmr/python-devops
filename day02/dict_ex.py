info = {
    "name": "Rajendra KUmar",
    "city": "Bokaro",
    "age" : 28,
    "salary": 12.2,
    "married": True,
    "fav": [
        "teachhing","moving","eating"
    ]
}

print(" I love in ",info["city"])

print('My favourite',info.get('favourite','Not found'))

info.update({'color':"blaack"})

print("What's your color: ", info['color'])
print("----------------------------------------------------")
for key,value in info.items():
    print(key,value)