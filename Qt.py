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
                point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code <600:
                    parseIt = False
                if err.code ==400:
                    trigger = False
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
                point = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+str(user)+"?&beginIndex="+str(g*15)+"&endIndex=100&api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6"
                response = urllib2.urlopen(point)
                string = response.read()
            except urllib2.HTTPError as err:
                print (err.code)
                if err.code <600:
                    parseIt = False
                if err.code ==400:
                    trigger = False
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
        point = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchId)+"?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6"
        response = urllib2.urlopen(point)
        string = response.read()
    except urllib2.HTTPError as err:
        print (err.code)
        if err.code <600:
            trigger = False
        if err.code ==400:
            trigger = False
        if err.code == 429:
            time.sleep(11)
            getInfoMatches(matchId,client)
            trigger = False
    if trigger:    
        gameList = json.loads(string) 
        c = string.count('totalDamageDealtToChampions')
        saveChampInfo(gameList,client,c,matchId)
        for i in range(0,c):

            saveSummonerId(gameList['participantIdentities'][i]['player']['summonerId'],client)
        # this saves the match info but im going to comment it out
        #saveMatchInfo(gameList,client)
        #this down here just saves the matchId
        saveMatchId(matchId,client)

#this one saves the id only>>>>>>>>>>>>>>>>>>>>>>
def saveMatchId(matchId,client):
    print "new MatchId added"
    db = client.MatchIdList
    data = { "_id" : matchId }
    db.posts.insert(data)

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

def saveChampInfo(gameData,client,entries,matchId):
    winners = []
    lossers = []

    for i in range(0,entries):

        if gameData["participants"][i]["stats"]["winner"]:
            winners.append(entries)
        else:
            lossers.append(entries)

        summoner = gameData["participants"][i]["championId"]

        win = gameData["participants"][i]["stats"]["winner"]

        items = []
        items.append(gameData["participants"][i]["stats"]["item0"])
        items.append(gameData["participants"][i]["stats"]["item1"])
        items.append(gameData["participants"][i]["stats"]["item2"])
        items.append(gameData["participants"][i]["stats"]["item3"])
        items.append(gameData["participants"][i]["stats"]["item4"])
        items.append(gameData["participants"][i]["stats"]["item5"])
        items.append(gameData["participants"][i]["stats"]["item6"])
        
        # this is just in game data that I added later
        kills = gameData["participants"][i]["stats"]["kills"]
        goldE = gameData["participants"][i]["stats"]["goldEarned"]
        deaths = gameData["participants"][i]["stats"]["deaths"]
        goldS = gameData["participants"][i]["stats"]["goldSpent"]
        level = gameData["participants"][i]["stats"]["champLevel"]


        addtoData(summoner,matchId,win,kills,goldE,goldS,deaths,level,client)


        spell1 = gameData['participants'][i]['spell1Id']
        spell2 = gameData['participants'][i]['spell2Id']

        lane = gameData['participants'][i]['timeline']['lane']
        role = gameData['participants'][i]['timeline']['role']
        
        databaseAdd(summoner,win,items,spell1,spell2,level,lane,role,client,matchId)

def addtoData(summoner,matchId,win,kills,goldE,goldS,deaths,level,client):
    
    if win:
        db = client.ChampionGameStatsW
        entry = {"summoner": summoner,"matchId":matchId,"kills":kills,"goldE":goldE,"goldS":goldS,"death":deaths,"level":level}
        db.posts.insert(entry)
    else:
        db = client.ChampionGameStatsL
        entry = {"summoner": summoner,"matchId":matchId,"kills":kills,"goldE":goldE,"goldS":goldS,"death":deaths,"level":level}
        db.posts.insert(entry)


def databaseAdd(summoner,win,items,spell1,spell2,level,lane,role,client,matchId):
    if doesChampExist(summoner,client):
        updateChampWin(summoner,win,client)
        createThisChamp(summoner,win,items,spell1,spell2,level,lane,role,client,matchId)

    else:
        winUpdate(summoner,win,client)
        createThisChamp(summoner,win,items,spell1,spell2,level,lane,role,client,matchId)

def updateChampWin(summoner,win,client):
    db = client.ChampionWin

    theOne = db.posts.find_one({"_id" : summoner})
    winData = theOne['wins']
    lostData = theOne['lost']

    if win:
        db.posts.update({"_id" : summoner}, {"wins": winData+1,"lost": lostData})
    else:
        db.posts.update({"_id" : summoner}, {"lost": lostData+1,"wins": winData})
    

def updateChampItems(summoner, items,client):
    itemsList = {}
    for i in range(0,len(items)):
        itemsList[str(items[i])] = 1
    
    db = client.ChampionData

    theOne = db.posts.find_one({"_id" : summoner})

    print theOne["items"][""]

    #db.posts.update({"_id" : summoner}, {"wins": winData+win})
def winUpdate(summoner,win,client):
    db = client.ChampionWin

    wins = 0
    lost = 0
    if win:
        wins = 1
    else:
        lost = 1

    entry = {"_id": summoner, "wins" : wins, "lost" : lost}
    db.posts.insert(entry)


def createThisChamp(summoner,win,items,spell1,spell2,level,lane,role,client,matchId):
    if win:

        db = client.ChampionItemsW
        for i in range(0,len(items)):
            entry = {"summoner": summoner, "items":items[i],"matchId":matchId}
            db.posts.insert(entry)

        db = client.ChampionSpellsW
        entry = {"summoner": summoner,"spell":spell1,"matchId":matchId}
        db.posts.insert(entry)
        entry = {"summoner": summoner,"spell":spell2,"matchId":matchId}
        db.posts.insert(entry)


        db = client.ChampionLaneW
        entry = {"summoner": summoner,"lane":lane,"role":role,"matchId":matchId}
        db.posts.insert(entry)
    else:

        db = client.ChampionItemsL
        for i in range(0,len(items)):
            entry = {"summoner": summoner, "item":items[i],"matchId":matchId}
            db.posts.insert(entry)

        db = client.ChampionSpellsL
        entry = {"summoner": summoner,"spell":spell1,"matchId":matchId}
        db.posts.insert(entry)
        entry = {"summoner": summoner,"spell":spell2,"matchId":matchId}
        db.posts.insert(entry)


        db = client.ChampionLaneL
        entry = {"summoner": summoner,"lane":lane,"role":role,"matchId":matchId}
        db.posts.insert(entry)

   
def submitEntryToDataBase(entry,client):
    db = client.ChampionData
    db.posts.insert(entry)

def doesChampExist(summoner,client):
    db = client.ChampionWin
    
    theOne = db.posts.find_one({"_id" : summoner})

    if theOne == None:

        return False

    return True



if __name__ == '__main__':
    main()

