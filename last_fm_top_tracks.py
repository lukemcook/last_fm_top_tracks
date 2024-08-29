import requests
from datetime import datetime

def get_weekly_track_chart(username, api_key, limit, page, start_date, end_date):
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
    
    return top_tracks

def write_top_tracks_to_file(top_tracks):
    # Write the top tracks to a file
    with open('top_tracks.txt', 'w') as file:
        for track in top_tracks:
            file.write(f"Track: {track['name']}\n")
            file.write(f"Artist: {track['artist']['#text']}\n")
            file.write(f"Play Count: {track['playcount']}\n")
            file.write('---\n')

def export_tracks(username, api_key, limit, page, start_date, end_date):
    top_tracks = get_weekly_track_chart(username, api_key, limit, page, start_date, end_date)
    write_top_tracks_to_file(top_tracks)
    print("Tracks exported to top_tracks.txt")

# Set your Last.fm username and API key
username = input("Enter your Last.fm username: ") #'your_username'
api_key = input("Enter your Last.fm API key: ") #'your_api_key'

# Set the limit and page for the API request
limit = 100
page = 1

# Ask the user for the start and end dates
start_date_input = input("Enter the start date (YYYY, MM, DD): ")
end_date_input = input("Enter the end date (YYYY, MM, DD): ")

# Convert the user's input into datetime objects
start_date = datetime.strptime(start_date_input, '%Y, %m, %d')
end_date = datetime.strptime(end_date_input, '%Y, %m, %d')

# Export tracks
export_tracks(username, api_key, limit, page, start_date, end_date)