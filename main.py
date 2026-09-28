import requests

# The API endpoint
url = "https://www.tvmaze.com/shows/204/stargate-sg1/episodes"

# A GET request to the API
response = requests.get(url)

# Print the response
print(response.json())