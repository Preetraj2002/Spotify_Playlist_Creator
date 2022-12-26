import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from os import environ

date=input("Which year do you want to Travel to? Type the date in this format YYYY-MM-DD: ")
year=date.split("-")[0]
# print(year)
API_endpoint="https://www.billboard.com/charts/hot-100/"


ClientID=environ["Spotify_ClientID"]
ClientSecret=environ["Spotify_ClientSecret"]
redirect_url="http://example.com"
prof_id= environ["Spotify_profID"]


response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
website_content=response.text

soup=BeautifulSoup(website_content,"html.parser")

# print(soup.prettify())

songs = [song.getText().strip() for song in soup.find_all(name="h3",id="title-of-a-story",class_="a-no-trucate")]

for song in songs:

    print(song)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ClientID,
                                               client_secret=ClientSecret,
                                               redirect_uri=redirect_url,
                                               scope="playlist-modify-private"))
results = sp.current_user()
print(results)

track_uris=[]
count=0

for song in songs:
    query=f"track:{song} year:{year}"
    spotify_response=sp.search(q=query,limit=1,type="track")
    # print(spotify_response)
    try:
        item=spotify_response["tracks"]["items"][0]

    except IndexError:
        print(f"Song with {query} not found")
        count+=1


    else:
        uri = item["uri"]
        # print(uri)
        track_uris.append(uri)



for i in range(len(track_uris)):
    print(f"{i+1}.{track_uris[i]}")


pl_response=sp.user_playlist_create(user=prof_id, name=f"{date} Billboard 100", public=False)
pl_id=pl_response["id"]
print(pl_response)
print(pl_id)

reply=sp.playlist_add_items(playlist_id=pl_id,items=track_uris)
print(reply)
