## Spotify_Playlist_Creator

# Objective

The scripts uses `BeautifulSoup` to scrap out the top 100 songs on the Billboard on a specified data which is then stored in list. 

```
Which year do you want to Travel to? Type the date in this format YYYY-MM-DD: 2015-12-09
Hello
Sorry
Hotline Bling
What Do You Mean?
The Hills
Stitches
... and so on 
```

The scripts then loop through the list and find each song on spotify and adds it to a newly created playlist on the client's spotify account. In order to interact with the spotify we use `spotify` library and `SpotifOAuth` class from `spotify.oauth2` module to authenticate the client.
