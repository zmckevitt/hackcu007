import spotipy
import spotipy.util as util
def func(user,time_range):
    username='31exjzvo2nlf4xdgeffjq3ndafwq'
    client_id='7e9f9c2e77b64e66a6c20b5b3eb7b479'
    client_secret='c4bb8e27f686455182b644fb10b61d6e'
    ret=[]
    redirect_uri = 'http://localhost:7777/callback'
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)
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
    file1 = open("txt_files/out.txt","w")

     
    topS=[]
    topA=[]
    topD=[]
    topE=[]
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

    for i in range(0,len1-1): 
        for j in range(0, len1-1): 
            if ret[j][4][1][1] < ret[j+1][4][1][1] : 
                ret[j], ret[j+1] = ret[j+1], ret[j]
    for i in range(0,10):
        topE.append(ret[i][0])

    for i in range(0,10):
        temp=str(topS[i])+'\n'
        file1.write(temp)
    for i in range(0,10):
        temp=str(topA[i])+'\n'
        file1.write(temp)
    for i in range(0,10):
        temp=str(topD[i])+'\n'
        file1.write(temp)
    for i in range(0,10):
        temp=str(topE[i])+'\n'
        file1.write(temp)
    
    newline = '\n'
    max_value = max(num)
    max_index = num.index(max_value)
    file1.write(top_G[max_index])
    file1.write(newline)
    num.pop(max_index)
    top_G.pop(max_index)
    max_value_2 = max(num)
    max_index = num.index(max_value_2)
    file1.write(top_G[max_index])
    file1.write(newline)
    num.pop(max_index)
    top_G.pop(max_index)
    max_value_3 = max(num)
    max_index = num.index(max_value_3)
    file1.write(top_G[max_index])
    file1.write(newline)
    num.pop(max_index)
    top_G.pop(max_index)


    tot_valence = 0
    avg_valence = 0
    # finding how sad the person is
    for i in range (0,len1-1):
        tot_valence += ret[i][4][9][1]
    avg_valence = tot_valence/len1
    sad_string = ""
    if(avg_valence < 0.25):
        sad_string = "... see a therapist."
    elif(avg_valence < 0.5):
        sad_string = "Your music's on the sadder side, but we're sure you'll be fine"
    elif(avg_valence < 0.75):
        sad_string = "Your music seems on the happier side, we'd be on the happier side if you venmoed ;)" 
    elif(avg_valence < 1):
        sad_string = "Your music is a little too happy. Might want to settle down a little"
    file1.write(sad_string)


    return ret
func('a','medium_term')