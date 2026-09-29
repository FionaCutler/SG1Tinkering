import requests
import json
import time


# The API endpoint
base_url = "https://api.tvmaze.com/shows/204/episodes"


# A GET request to the API
response = requests.get(base_url)

# Print the response
episodes = response.json()
rating = 0
name= ''
for episode in episodes:
    if ( episode['rating']['average'] > rating):
        rating = episode['rating']['average']
        name = episode['name']
        url = 'https://api.tvmaze.com/episodes/' + str(episode['id']) + '/guestcrew'
        guestcrew = requests.get(url).json()
        for crewmember in guestcrew:
            if(crewmember['guestCrewType'] == 'Writer'):
                print(crewmember['person']['name'])
        time.sleep(2.5)

        
print(name)