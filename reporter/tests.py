import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/alerts"

querystring = {"lat":"38.5","lon":"-78.5"}

headers = {
    'x-rapidapi-key': "64bf1ccb8cmsh2a5b1e0892d52fdp1e72d8jsn081af20eddb6",
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)