import requests 

def get_joke_data(api):
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url=api,headers=headers)
    return response.json()


api = "https://official-joke-api.appspot.com/random_joke" 
data = get_joke_data(api) 
print(data["setup"])
print(data["punchline"])
print("-------------------------------------------------")
api = "https://icanhazdadjoke.com/"
data = get_joke_data(api)
print(data['joke'])
