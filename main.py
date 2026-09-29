import requests
import json

# The API endpoint
url = "https://api.tvmaze.com/shows/204/episodes"

# A GET request to the API
response = requests.get(url)

# Print the response
episodes = response.json()
rating = 10
name= ''
for episode in episodes:
    if (rating > episode['rating']['average']):
        rating = episode['rating']['average']
        name = episode['name']
        
print(name)