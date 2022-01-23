
'''
#TODO:
Print currently playing song
SPOTIPY Library URL:
    https://spotipy.readthedocs.io/en/2.19.0/?highlight=currently#spotipy.client.Spotify.currently_playing

#TODO:
Tweet on twitter from this script
#TODO:
Tweet something about me listening to "Money Machine"

#TODO:
Tweet how many times I've listened to it this month
'''

import spotipy

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)


#pip install spotipy
