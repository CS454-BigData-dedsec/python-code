
'''
Created on Apr 23, 2015

@author: Deadsec

http://www.themeta.gg

This module makes an API call to a game and stores a json object to a textfile.
The JSON object is statistics on a game's relevant meta information.

'''
# you see that it first displays one user but then displays all the fights he has fought and goes
# back and uses those battle id's and uses those to look up all the users in that one battle
import pymongo
import urllib2
import json
import re
import time

def main():
    response = urllib2.urlopen('https://na.api.pvp.net/observer-mode/rest/' +
                'featured?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6')
    string = response.read()        #this is a string
    gameList = json.loads(string)   #this is a json object
    from pymongo import MongoClient
    client = MongoClient()
    db = client.test_database
    
    starting = '35241849'
    
    #print(string)
    print(gameList)     #the u' annotation is unicode.  you can ignore it
    newMatches = matches(starting)
    
    #prints out the values stored in the 'gameList' key, this will help us determine what
    #we can use to answer our question, it is stored as a dictionary
    for i in gameList['gameList']:
        print(i)              
    print("this is the list of matches for this guy", starting)
    print(newMatches)
    
    userFromMatches(newMatches,db)# I PASS THE db TO userFromMatches so when i insert into mongodb it recognizes it


def userFromMatches(matches,db):
    list = []
    trigger = True
    for g in range(0, len(matches)):
        if(trigger):
            try:
                point = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matches[g])+"?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code ==400:
                    time.sleep(20)
                    point = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matches[g])+"?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                    response = urllib2.urlopen(point)
                    string = response.read()
        
        
            gameList = json.loads(string)
            
            #db.posts.insert(gameList) THIS WILL LOAD ALL THE INFORMATION INTO THE database, i dont know why but the name of collection is posts
            
            c = string.count('totalDamageDealtToChampions')
            print( "info on match ", str(matches[g]), ":: participants", c)
            for i in range(0,c):
                
                print(i , " Player = ", gameList["participants"][i]["championId"] , "::  Win = ", gameList["participants"][i]["stats"]["winner"], "\n" )
                #here i create the object that i will load into the posts collection
                data = {"Player":gameList["participants"][i]["championId"], "Win":gameList["participants"][i]["stats"]["winner"]}
                db.posts.insert(data) #inserting the data into the collection using insert
                #To find the data in your mongoDB
                #type:
                
                #show dbs
                #--it should have test_database in the list
                
                #use test_database  --itll change to that database
                #show collections
                #--it should show posts in the list
                #db.posts.find()      --this will show you every document you have in posts
                
                #we can look up specific queries like this:
                #db.posts.find({"Win": true})    --to find where the player won




def matches(user): #looks up by user for matches
    list = []
    trigger = True
    for g in range(0, 100):
        if(trigger):
            try:
                point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code ==400:
                    time.sleep(20)
                    point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                    response = urllib2.urlopen(point)
                    string = response.read()
        
        
            gameList = json.loads(string)
            c = string.count('matchId')
            if (c<15):
                trigger = False
            print("===Game Data Sample===",g)
            for i in range(0,c):
                print( "Match ID = ", gameList["matches"][i]["matchId"])
                print( "Champion ID = ", gameList["matches"][i]["participants"][0]["championId"] )
                print( "Win = ", gameList["matches"][i]["participants"][0]["stats"]["winner"], "\n" )
                list.append(gameList["matches"][i]["matchId"])

                    return list



if __name__ == '__main__':
    main()
