import requests

# The API endpoint
url = "https://api.tvmaze.com/shows/204/episodes"

# A GET request to the API
response = requests.get(url)

# Print the response
#print(response.json())
for episode in response:
    print(episode)