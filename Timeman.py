import os
import time
import sys


def youtubeSettings():
    import webbrowser
    print("here")
    
    
    
print ("ready to start getting shit done?")
input("Press anything to proceed to settings")

wBlocks = input("Enter Work time Blocks in Minutes")
bBlocks = input("Enter Break time Blocks in Minutes")

breakActivities = input('''select some break activities. Put a '-' between each one ---
                        -- y = youtube videos, f = five38, c = codecampwork, g = gaming m = meditate, n= nothing at all, e = exercise''')
breakActivities = str(breakActivities)

if breakActivities.find("y") != -1:
    youtubeSettings()
else:
    print (breakActivities)
    



    