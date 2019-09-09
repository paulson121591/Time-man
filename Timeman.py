import os
import time
import sys
import pickle
import math
import cmath
import pylast
import pprint
import random

def youtubeSettings():
    import webbrowser
    print("here")
    




def lastFmLoad(username, password):

    
    API_KEY = "ef31fa7d2f19d54b6ff8f6d6c1122f35"
    API_SECRET = "a82839d2f09ef2299cf570e63fb20e0f"   
    
    username = username
    password_hash = pylast.md5(password)
    
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
    
    return network

    


    
    # artist = pylast.Artist("Manchester Orchestra", network)

    #     # Act
    # bio = artist.get_bio_published_date()
    # print (bio)
    
    
    
    
    
   
   
def newProfile():
    profileName= input('Name of profile   -')
    
    wBlocks = input("Enter Work time Blocks in Minutes   -")
    bBlocks = input("Enter Break time Blocks in Minutes   -")
    

    breakActivities = input('''select some break activities. 
                                Put a '-' between each one 
                                y = youtube videos 
                                f = five38 
                                c = codecampwork 
                                g = gaming 
                                m = meditate 
                                n= nothing at all 
                                e = exercise
                                
                                ''')
    
    profileInfo = {"profileName":profileName, "wBlocks":wBlocks,"bBlocks":bBlocks,"breakActivities":breakActivities}


            

    music= input("Would you like music suggestions as you work?y = Yes n = No   ")

    if music.find("y") != -1:
        username =  input("Last FM Username   -")
        password = input("Last FM Password   -")
        profileInfo["username"]= username
        profileInfo["password"]= password
        network = lastFmLoad(username, password)
        
        
    pickle.dump(profileInfo, open( profileName, "wb") )
    
    
    return network, breakActivities, bBlocks, wBlocks
            
    
    
def loadProfile():
    
    profileName = input("Input Profile name     -")
    
    profile = pickle.load( open( profileName, "rb" ))
    
    username = profile.get("username","")
    password = profile.get("password","")
    breakActivities = profile.get("breakActivities","")
    bBlocks = profile.get("bBlocks","")
    wBlocks = profile.get("wBlocks","")
    
    
    network = lastFmLoad(username, password)
    
    return network, breakActivities, bBlocks, wBlocks, username
    
    
        
        
        
        
        
        
        
            
            
        
        
    
    
    
    

    

    
    
    
print ("ready to start getting shit done?  ")
pro = input("Enter 'N' to create a NEW profile. Enter L to LOAD an existing profile")
if pro.find("n") != -1:
    profile = newProfile()
else:
    profile = loadProfile()
    
    network = profile[0]
    breakActivities= profile[1]
    bBlocks = profile[2]
    wBlocks = profile[3]
    username = profile[4]
    
    
print('Welcome back! ' + username)
time.sleep(3)
print('lets see what should we Jam to...')






    
user = network.get_user(username)

# Act/Assert
artist1 = user.get_top_artists(limit=20)[0].item
artist2 = user.get_top_artists(limit=20)[1].item
artist3 = user.get_top_artists(limit=20)[2].item
artist4 = user.get_top_artists(limit=20)[3].item
artist5 = user.get_top_artists(limit=20)[4].item
artist6 = user.get_top_artists(limit=20)[5].item
artist7 = user.get_top_artists(limit=20)[6].item
artist8 = user.get_top_artists(limit=20)[7].item
artist9 = user.get_top_artists(limit=20)[8].item
artist10 = user.get_top_artists(limit=20)[9].item
artist11= user.get_top_artists(limit=20)[10].item
artist12 = user.get_top_artists(limit=20)[11].item
artist13 = user.get_top_artists(limit=20)[12].item


artists = [artist1,artist2,artist3,artist4,artist5,artist6,artist7,artist8,artist9,artist10,artist11,artist12,artist13]
print('...')
rand = random.randint(0, 12)

print ('How about some  '+ str(artists[rand])+'?')
choice = input("Just say -'yes' or 'no' ")
while choice == 'no':
    print('Hmmmmm.... Okay, how about...')
    time.sleep(2)
    rand = random.randint(0, 12)
    
    print('Okay, how about ' + str(artists[rand])+'?' )
    choice = input("Just say -'yes' or 'no' ")
    if choice == 'yes':
        artist = str(artists[rand])
        
        break
print('Awesome, lets get started..')
ready = input('Ready yes or no  ')
while ready == 'yes':
    tw = int(int(wBlocks)*60)
    tb = int(int(bBlocks)*60)

    print('Timer of '+wBlocks+' minute starts in..')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    for remaining in range(int(tw), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")
    
    print('STOP! Take a break!')
    for remaining in range(int(tb), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!            \n")
        
    ready = input('Ready to go again? yes or no  ')
        

    
    





            
        







    

    
    

