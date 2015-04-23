'''
Created on Apr 23, 2015

@author: Deadsec

http://www.themeta.gg

This module makes an API call to a game and stores a json object to a textfile.
The JSON object is statistics on a game's relevant meta information.

'''
import urllib2
import json

def main():
    response = urllib2.urlopen('https://na.api.pvp.net/observer-mode/rest/' +
                'featured?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6')
    string = response.read()        #this is a string
    gameList = json.loads(string)   #this is a json object
    
    
    #print(string)
    print(gameList)     #the u' annotation is unicode.  you can ignore it
    
    #prints out the values stored in the 'gameList' key, this will help us determine what
    #we can use to answer our question, it is stored as a dictionary
    for i in gameList['gameList']:
        print(i)              
    

if __name__ == '__main__':
    main()
