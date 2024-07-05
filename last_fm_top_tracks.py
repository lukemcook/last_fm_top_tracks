import requests
from datetime import datetime

# Set your Last.fm username and API key
username = 'your_username'
api_key = 'your_api_key'

# Set the limit and page for the API request
limit = 100
page = 1

# Set the start and end dates for the weekly track chart
start_date = datetime(2015, 9, 14)  # YYYY, MM, DD
end_date = datetime(2016, 9, 1)

# Convert the start and end dates to timestamps
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

# Construct the URL for the API request
url = f'http://ws.audioscrobbler.com/2.0/?method=user.getWeeklyTrackChart&user={username}&api_key={api_key}&limit={limit}&page={page}&format=json&from={start_timestamp}&to={end_timestamp}'

# Send the API request and get the response
response = requests.get(url)
data = response.json()

# Extract the top tracks from the response
top_tracks = data['weeklytrackchart']['track']

# Write the top tracks to a file
with open('top_tracks.txt', 'w') as file:
    for track in top_tracks:
        file.write(f"Track: {track['name']}\n")
        file.write(f"Artist: {track['artist']['#text']}\n")
        file.write(f"Play Count: {track['playcount']}\n")
        file.write('---\n')

# Print a message to indicate that the tracks have been exported
print("Tracks exported to top_tracks.txt")
