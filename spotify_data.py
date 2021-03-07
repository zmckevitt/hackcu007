from __future__ import print_function
import sys
import spotipy
import os
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 2:
    username = sys.argv[1]
    time = sys.argv[2]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

os.environ["SPOTIPY_CLIENT_ID"] = "7e9f9c2e77b64e66a6c20b5b3eb7b479"
os.environ["SPOTIPY_CLIENT_SECRET"] = "c4bb8e27f686455182b644fb10b61d6e"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:7777/callback"

def func(user,time_range):
    #username='31exjzvo2nlf4xdgeffjq3ndafwq'
    client_id='7e9f9c2e77b64e66a6c20b5b3eb7b479'
    client_secret='c4bb8e27f686455182b644fb10b61d6e'
    ret=[]
    redirect_uri = 'http://localhost:7777/callback'
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username=username, 
                                   scope=scope,
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri
                                   )

    #print("HERE")

    if(time == 'week'):
        time_range = 'short_term'
    if(time == 'month'):
        time_range = 'medium_term'
    if(time == 'year'):
        time_range = 'long_term'

    sp = spotipy.Spotify(auth=token)
    
    top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range=time_range)
    for i in range (len(top_tracks['items'])):
        count=0
        ret_features=[]
        features=sp.audio_features(top_tracks['items'][i]['id'])
        artist_ID=top_tracks['items'][i]['artists'][0]['id']
        artist=sp.artist(artist_ID)
        genres=artist['genres']
        for j in features[0]:
            ret_features.append((j,features[0][j]))
            count+=1
            if(count>10):
                break
        song_name=top_tracks['items'][i]['name']
        artist_name=top_tracks['items'][i]['artists'][0]['name']
        time_ms=top_tracks['items'][i]['duration_ms']/60000
        ret.append((song_name,artist_name,time_ms,genres,ret_features))
    top_G=[]
    num=[]
    
    for i in range(len(ret)):
        for j in range(len(ret[i][3])) :
            if(ret[i][3][j] in top_G):
                num[j]+=1
            else:
                top_G.append(ret[i][3][j])
                num.append(1)
    max_value = max(num)
    max_index = num.index(max_value)
#     print(top_G[max_index])
    file1 = open("txt_files/out.txt","w") 
    topS=[]
    topA=[]
    topD=[]
    for i in ret:
        for j in range(len(i)):
            if(j==0):
                topS.append(i[j])
            if(j==1):
                topA.append(i[j])
    len1=len(ret)
    temp=[]                
    for i in range(0,len1-1): 
        for j in range(0, len1-1): 
            if ret[j][4][0][1] < ret[j+1][4][0][1] : 
                ret[j], ret[j+1] = ret[j+1], ret[j]
    for i in range(0,10):
        topD.append(ret[i][0])
    
    for i in range(0,10):
        temp=str(topS[i])+'\n'
        file1.write(temp)
    for i in range(0,10):
        temp=str(topA[i])+'\n'
        file1.write(temp)
    for i in range(0,10):
        temp=str(topD[i])+'\n'
        file1.write(temp)
    
    file1.write(top_G[max_index])
    return ret


func('a',time)