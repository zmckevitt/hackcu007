from __future__ import print_function
import sys
import spotipy
import os
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

os.environ["SPOTIPY_CLIENT_ID"] = "7e9f9c2e77b64e66a6c20b5b3eb7b479"
os.environ["SPOTIPY_CLIENT_SECRET"] = "c4bb8e27f686455182b644fb10b61d6e"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:7777/callback"
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'


scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)