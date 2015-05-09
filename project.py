# you see that it first displays one user but then displays all the fights he has faught and goes
# back and uses those battle id's and uses thos to look up all the users in that one battle
import pymongo
import urllib2
import json
import re
import time

def main():
    #from pymongo import MongoClient
    #client = MongoClient()
    #db = client.test_database

    #print db
    
    starting = '35241849'

    newMatches = matches(starting)

    print "this is the list of matches for this guy" + starting
    print newMatches 

    userFromMatches(newMatches)


def userFromMatches(matches):
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
            c = string.count('totalDamageDealtToChampions')
            print "info on match " + str(matches[g]) + ":: participants", c
            for i in range(0,c):

                print i , " Player = ", gameList["participants"][i]["championId"] , "::  Win = ", gameList["participants"][0]["stats"]["winner"], "\n" 

             
    
    return list    


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
                print "Match ID = ", gameList["matches"][i]["matchId"] 
                print "Champion ID = ", gameList["matches"][i]["participants"][0]["championId"] 
                print "Win = ", gameList["matches"][i]["participants"][0]["stats"]["winner"], "\n" 
                list.append(gameList["matches"][i]["matchId"])
    
    return list



if __name__ == '__main__':
    main()
