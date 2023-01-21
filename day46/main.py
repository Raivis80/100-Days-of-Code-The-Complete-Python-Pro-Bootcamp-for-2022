import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests as req
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

user_input = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = req.get(f"https://www.billboard.com/charts/hot-100/{user_input}")
soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.find_all(name="li", class_="o-chart-results-list__item")
song_titles = [song.find(name="h3", id="title-of-a-story").getText().strip() for song in song_titles if song.find(name="h3", id="title-of-a-story") is not None]

print(song_titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
    )
)

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = user_input.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
