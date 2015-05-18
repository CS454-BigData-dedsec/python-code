'''
Checks if "matchId" already exists in "matchData" collection.
If it doesn't exist, continue.

Queries "Match" Riot API using specified "matchId" parameter.

Inserts parsed "match" into "matchData" collection

'''

import pymongo
import urllib2
import json
import pprint

def matchData(matchId):
    #check database
    client = pymongo.MongoClient()
    db = client.test_database
    exists = db.matchData.find({"matchId": matchId })
    if exists:
    	print("match found, returning without inserting")
    	return
    
    #api call
    webhook = ("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchId) + 
    			"?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6")
    response = urllib2.urlopen(webhook)
    response = json.loads(response.read())
    
    #response parsing
    match = { 	"mapId": response["mapId"],
    			"matchCreation": response["matchCreation"],
    			"matchDuration": response["matchDuration"],
    			"matchId": response["matchId"],
    			"matchMode": response["matchMode"],
    			"matchType": response["matchType"],
    			"matchVersion": response["matchVersion"],
    			"platformId": response["platformId"],
    			"queueType": response["queueType"],
    			"region": response["region"],
    			"season": response["season"]
    }

    #teams
    winTeamId = 0
    bans = []
    for team in response["teams"]:
    	if team["winner"] == True:
    		winTeamId = team["teamId"]
    	for ban in team["bans"]:
    		bans.append(ban["championId"])
    match["bans"] = bans

    #participants
    participants = []
    for p in response["participants"]:
    	current = {	"championId": p["championId"],
    				"highestAchievedSeasonTier": p["highestAchievedSeasonTier"],
    				"masteries": p["masteries"],
    				"runes": p["runes"],
    				"spells": [ p["spell1Id"], p["spell2Id"] ]
    	}

    	#did participant win?
    	if p["teamId"] == winTeamId:
    		win = True
    	elif p["teamId"] != winTeamId:
    		win = False
    	current["win"] = win

    	#ParticipantStats
    	stats = p["stats"]
    	if stats["firstBloodAssist"] or stats["firstBloodKill"] is True:
    		firstBlood = True
    	else:
    		firstBlood = False
    	current["firstBlood"] = firstBlood

    	if stats["firstTowerAssist"] or stats["firstTowerKill"] is True:
    		firstTower = True
    	else:
    		firstTower = False
    	current["firstTower"] = firstTower

    	items = []
    	for x in range(7):
    		items.append(stats["item" + str(x)])
    	current["items"] = items

    	#ParticipantTimeLine
    	current["lane"] = p["timeline"]["lane"]
    	current["role"] = p["timeline"]["role"]

    	participants.append(current)
    match["participants"] = participants

    #insert into database
    db.matchData.insert(match)



    #debug printing
    pp = pprint.PrettyPrinter()
    pp.pprint(match)




if __name__ == "__main__":
	matchData(1721458584)
    