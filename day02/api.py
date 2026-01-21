#API (Application Programming Interface)

import requests 


response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")

print(type(response.json()))

for key,value in response.json().items(): 
    if key == "userId":
        if value in [1,255,52]:
            print('user found')
        else:
            print("user not found")