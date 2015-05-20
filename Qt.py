import pymongo
import urllib2
import json
import re
import time

def main():
    from pymongo import MongoClient
    client = MongoClient()
    
    print "hello Shall we start"
    print "I really hope the hardrive is going to hold all this"
    starting = '35241849'
    matches1(starting,client)

    if(anotherMatchExist(client)):
        matchId = findMatch(client)
        getInfoMatches(matchId,client)
        markAsSeen(matchId,client)

    while(True):

        while(anotherUserExist(client)):
            print "new Person now"
            victimId = findAnotherUser(client)
            matches(victimId,client)

            if(anotherMatchExist(client)):
                print "going thru his matches now"
                while(anotherMatchExist(client)):
                    matchId = findMatch(client)
                    getInfoMatches(matchId,client)
                    markAsSeen(matchId,client)
            print "done with him"
            saveUserInfo(victimId,client)
        print "now I have to reset all"
        redoall(client)

def redoall(client):
    while(anotherUserExistFalse(client)):
        victimId = findAnotherUserFalse(client)
        changeToFalse(victimId,client)

def changeToFalse(victimId,client):

    db = client.Users_Visited
    db.posts.update({"_id" : victimId}, {"Visited": True})

def findAnotherUserFalse(client):# pulls the next User 

    db = client.Users_Visited
    #change this to traveled users
    theOne = db.posts.find_one({"Visited" : True})
    return theOne["_id"]

def anotherUserExistFalse(client): # checks if another User exist

    db = client.Users_Visited
    #change the bello to make it point at the traveled one.......
    theOne = db.posts.find_one({"Visited" : True})
    
    if theOne == None:
        return False

    else:    
        return True
    
def markAsSeen(matchId,client):

    db = client.MatchId_Visited
    db.posts.update({"_id" : matchId}, {"Visited": True})



def userExist(user,client):

    db = client.Users_Visited
    theOne = db.posts.find_one({"_id" : user})
        
    if theOne == None:
        return False
    else:
        return True

def matches(user,client): #looks up by user for matches
    trigger = True
    parseIt = True
    counter = 0


    for g in range(counter, 100):
        if(trigger):
            try: 
                point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code ==503:
                    parseIt = False
                if err.code ==500:
                    parseIt = False
                if err.code ==401:
                    parseIt = False
                    print user
                if err.code ==400:
                    print user
                    parseIt = False
                    trigger = False
                if err.code ==404:
                    parseIt = False
                    print user
                if err.code == 429:
                    time.sleep(11)
                    matches(user,client)
                    parseIt = False        

            if(parseIt):        
                gameList = json.loads(string) 
                c = string.count('matchId')
                if (c<15):
                    trigger = False
                for i in range(0,c):

                    checkMatch(gameList["matches"][i]["matchId"],client) 
                    

def saveUserInfo(user,client):

    db = client.Users_Visited
    db.posts.update({"_id" : user}, {"Visited": True})


def matches1(user,client): #looks up by user for matches
    trigger = True
    parseIt = True
    counter = 0

    if(userExist(user,client)):
        counter = getCunter(user)

    for g in range(counter, counter*10+100):

        if(trigger):
            try: 
                point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code ==503:
                    trigger = False
                if err.code ==500:
                    parseIt = False
                if err.code ==400:
                    trigger = False
                    parseIt = False
                if err.code == 429:
                    time.sleep(11)
                    parseIt = False
                    matches1(user,client)

            if(parseIt):        
                gameList = json.loads(string) 
                c = string.count('matchId')
                if (c<15):
                    trigger = False
                for i in range(0,c):

                    checkMatch(gameList["matches"][i]["matchId"],client)

def getInfoMatches(matchId,client):
    trigger = True
    try: 
        point = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchId)+"?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4"
        response = urllib2.urlopen(point)
        string = response.read()
    except urllib2.HTTPError as err:
        print (err.code)
        if err.code == 503:
            trigger = False
        if err.code == 500:
            trigger = False
        if err.code == 429:
            time.sleep(11)
            getInfoMatches(matchId,client)
            trigger = False
    if trigger:    
        gameList = json.loads(string) 
        c = string.count('totalDamageDealtToChampions')
    
        for i in range(0,c):

            saveSummonerId(gameList['participantIdentities'][i]['player']['summonerId'],client)
    
        saveMatchInfo(gameList,client)


def saveSummonerId(userId,client):

    db = client.Users_Visited
    if (userExist(userId,client) == False):
        print "ill add user " , userId
        data = { "_id" : userId , "Visited": False }
        db.posts.insert(data)


def saveMatchInfo(gameList,client):# this one just saves everything into that one giant database

    db = client.MatchInfo
    db.posts.insert(gameList)



def checkMatch(matchId,client): #this checks the database

    db = client.MatchId_Visited
    if matchExist(matchId,client):
        data = { "_id" : matchId , "Visited" : False }
        db.posts.insert(data) #inserting the data into the collection using insert


def matchExist(matchId,client): # checks if that Match exist

    db = client.MatchId_Visited
    #change the bello to make it point at the traveled one.......
    theOne = db.posts.find_one({"_id" : matchId})
        
    if theOne == None:
        return True
    else:
        return False


def anotherUserExist(client): # checks if another User exist

    db = client.Users_Visited
    #change the bello to make it point at the traveled one.......
    theOne = db.posts.find_one({"Visited" : False})
    
    if theOne == None:
        return False
    else:    
        return True

def findAnotherUser(client):# pulls the next User 

    db = client.Users_Visited
    #change this to traveled users
    theOne = db.posts.find_one({"Visited" : False})
    return theOne["_id"]

def anotherMatchExist(client): # checks if another match exist

    db = client.MatchId_Visited
    #change the bello to make it point at the traveled one.......
    theOne = db.posts.find_one({"Visited" : False})
    
    if theOne == None:
        return False
    else:   
        return True

def findMatch(client):# pulls the next one 

    db = client.MatchId_Visited
    #change this to traveled users
    theOne = db.posts.find_one({"Visited" : False})

    return theOne["_id"]


if __name__ == '__main__':
    main()

