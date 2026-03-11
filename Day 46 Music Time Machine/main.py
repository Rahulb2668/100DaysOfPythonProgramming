from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR UNIQUE CLIENT ID",
        client_secret="YOUR UNIQUE CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY DISPLAY NAME",
    )
)
user_id = sp.current_user()["id"]
date_user_input = input("Which is the date your prefer for your music. Enter Date in yyyy-mm-dd format")

BILLBOARD_URL=f"https://www.billboard.com/charts/hot-100/{date_user_input}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(BILLBOARD_URL, headers=headers)
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")

# Find all the h3 tags that contain the song titles
# We use a CSS selector that targets the specific structure Billboard currently uses
song_names_spans = soup.select("li ul li h3")

# Extract the text and strip away the messy whitespace/newlines
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

song_uris = []
year = date_user_input.split("-")[0] # Get just the year from the user's YYYY-MM-DD input

print("Searching Spotify for songs...")

for song in song_names:
    # Search for the track name and the year it came out
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        # Drill down into the JSON response to grab the URI
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # If the search list comes back empty, skip it so the code doesn't crash
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(f"Found {len(song_uris)} songs on Spotify!")

# Create the playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)
print(f"Playlist created: {playlist['name']}")

# Add the tracks to the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Success! Check your Spotify app.")