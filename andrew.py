'''


'''

import pymongo
import urllib2
import json
import pprint
import datetime

def matchData(matchId):
	'''
	This function inserts a parsed (hence skinny) "match" document into 
	"SkinnyMatchData" collection using "matchId" parameter.

	Queries using "match-v2.2" webhook located at 
	https://developer.riotgames.com/api/methods#!/967
	'''
	#check database
	client = pymongo.MongoClient()
	db = client.LeagueOfLegends
	cursor = db.SkinnyMatchData.find({"matchId": matchId })
	if cursor.count() > 0:
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
	db.SkinnyMatchData.insert(match)

	print('SkinnyMatchData document entered!')

def globalStats():
	'''
	This function inserts a document "stat" into "GlobalStats" collection based 
	upon "SkinnyMatchData" collection.  

	Each "stat" document has a datetime.now() located in stat["currentTime"]

	'''
	#database
	client = pymongo.MongoClient()
	db = client.LeagueOfLegends
	cursor = db.SkinnyMatchData.find()
	
	#parsing
	stat = {	"matchCount": 0,
				"participants": 0,
				"champions": 0,
				"bans": 0,
				"masteries": 0,
				"runes": 0,
				"spells": 0,
				"tiers": {
					"challenger": 0,
					"diamond": 0,
					"platinum": 0,
					"gold": 0,
					"silver": 0,
					"bronze": 0
				},
				"currentTime": datetime.datetime.now()
	}
	for match in cursor:
		stat["matchCount"] += 1
		for ban in match["bans"]:
			stat["bans"] += 1
		for participant in match["participants"]:
			stat["participants"] += 1
			if participant["championId"]:
				stat["champions"] += 1
			for mastery in participant["masteries"]:
				stat["masteries"] += 1
			for rune in participant["runes"]:
				stat["runes"] += 1
			for spell in participant["spells"]:
				stat["spells"] += 1
			tier = participant["highestAchievedSeasonTier"]
			if tier:
				if tier == "CHALLENGER":
					stat["tiers"]["challenger"] += 1
				elif tier == "DIAMOND":
					stat["tiers"]["diamond"] += 1
				elif tier == "PLATINUM":
					stat["tiers"]["platinum"] += 1
				elif tier == "GOLD":
					stat["tiers"]["gold"] += 1
				elif tier == "SILVER":
					stat["tiers"]["silver"] += 1
				elif tier == "BRONZE":
					stat["tiers"]["bronze"] += 1
	db.GlobalStats.insert(stat)
	print("Global stats updated")

def championStats():
	'''
	This function inserts a "champion_stat" document into "ChampionStat" 
	collection

	'''
	#database
	client = pymongo.MongoClient()
	db = client.LeagueOfLegends
	matchData = db.SkinnyMatchData.find()
	championData = db.ChampionStats.find()

	#api call
	webhook = ("https://global.api.pvp.net/api/lol/static-data/na/v1.2/" +
				"champion?champData=image&api_key=e63ca19d-7ce7-4fc7-9b85-" +
				"35759aab7ec6")
	response = urllib2.urlopen(webhook)
	response = json.loads(response.read())
	image_url = "http://ddragon.leagueoflegends.com/cdn/4.2.6/img/champion/"

	#parsing
	for champ in response["data"]:
		champ = response["data"][str(champ)]
		champion_stat = {	"name": champ["name"],
					"id": champ["id"],
					"title": champ["title"],
					"image": image_url + champ["image"]["full"],
					"times_played": 0,
					
		}



	#debug printing
	pp = pprint.PrettyPrinter()
	pp.pprint(champ)



if __name__ == "__main__":
	#matchData(1721458584)
	#globalStats()
	championStats()