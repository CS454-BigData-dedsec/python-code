'''


'''

import pymongo
import urllib2
import json
import pprint
import datetime

uri = "108.225.12.135"

def matchDataDriver():
	client = pymongo.MongoClient(uri)
	db = client.MatchIdList
	cursor = db.posts.find()
	for doc in cursor:
		matchData(doc["_id"])

def matchData(matchId):
	'''
	This function inserts a parsed (hence skinny) "match" document into 
	"SkinnyMatchData" collection using "matchId" parameter.

	Queries using "match-v2.2" webhook located at 
	https://developer.riotgames.com/api/methods#!/967
	'''
	#check database
	client = pymongo.MongoClient(uri)
	db = client.LeagueOfLegends
	cursor = db.SkinnyMatchData.find({"_id": matchId })
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
				"_id": response["matchId"],
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
	client = pymongo.MongoClient(uri)
	db = client.LeagueOfLegends
	cursor = db.SkinnyMatchData.find()
	db.drop_collection("GlobalStats")

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
				"_id": datetime.datetime.now()
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
	print("Global stats dropped and recalculated")

def staticData():
	#api call
	webhook = ("https://global.api.pvp.net/api/lol/static-data/na/v1.2/" +
				"champion?champData=image&api_key=e63ca19d-7ce7-4fc7-9b85-" +
				"35759aab7ec6")
	response = urllib2.urlopen(webhook)
	response = json.loads(response.read())
	image_url = "http://ddragon.leagueoflegends.com/cdn/4.2.6/img/champion/"

	#database insert
	client = pymongo.MongoClient(uri)
	db = client.LeagueOfLegends
	db.drop_collection("ChampionStats")

	for champ in response["data"]:
		champ = response["data"][str(champ)]
		champ_stat = {	"name": champ["name"],
						"_id": champ["id"],
						"title": champ["title"],
						"image": image_url + champ["image"]["full"],
						"firstBlood": 0,
						"firstTower": [],
						"win": [],
						"loss": [],
						"highestAchievedSeasonTier": [],
						"items": [],
						"spells": []
		}
		result = db.ChampionStats.insert_one(champ_stat)
	print("ChampionStats dropped and updated with empty champs.")

def fillChampStats():
	'''
	'''
	#database
	client = pymongo.MongoClient(uri)
	db = client.LeagueOfLegends
	matches = db.SkinnyMatchData.find()
	stats = db.ChampionStats.find()


	pp = pprint.PrettyPrinter()
	for match in matches:
		container = []
		for p in match["participants"]:
			# losers
			if(p["win"] is False and p["lane"] == "BOTTOM" and p["role"] == "DUO_SUPPORT"):
				bot_support_loser = p
			if(p["win"] is False and p["lane"] == "BOTTOM" and p["role"] == "DUO_CARRY"):
				bot_carry_loser = p
			if(p["win"] is False and p["lane"] == "TOP"):
				top_loser = p
			if(p["win"] is False and p["lane"] == "MIDDLE"):
				mid_loser = p
			if(p["win"] is False and p["lane"] == "JUNGLE"):
				jungle_loser = p
			# winners 
			if(p["win"] is True and p["lane"] == "BOTTOM" and p["role"] == "DUO_SUPPORT"):
				bot_support_winner = p
			if(p["win"] is True and p["lane"] == "BOTTOM" and p["role"] == "DUO_CARRY"):
				bot_carry_winner = p
			if(p["win"] is True and p["lane"] == "TOP"):
				top_winner = p
			if(p["win"] is True and p["lane"] == "MIDDLE"):
				mid_winner = p
			if(p["win"] is True and p["lane"] == "JUNGLE"):
				jungle_winner = p
		container.append(bot_support_loser)
		container.append(bot_carry_loser)
		container.append(mid_loser)
		container.append(top_loser)
		container.append(jungle_loser)
		container.append(bot_support_winner)
		container.append(bot_carry_winner)
		container.append(mid_winner)
		container.append(top_winner)
		container.append(jungle_winner)
		
		# first bloods, highestAchievedSeasonTier, items, spells
		for c in container:
			if c["firstBlood"] is True:
				incrementFirstBlood(db.ChampionStats, c)
			pushSeasonTier(db.ChampionStats, c)
			pushItems(db.ChampionStats, c)
			pushSpells(db.ChampionStats, c)

		# first towers
		if bot_support_loser["firstTower"] is True:
			pushFirstTower(db.ChampionStats, bot_support_loser, bot_support_winner)
		if bot_carry_loser["firstTower"] is True:
			pushFirstTower(db.ChampionStats, bot_carry_loser, bot_carry_winner)
		if mid_loser["firstTower"] is True:
			pushFirstTower(db.ChampionStats, mid_loser, mid_winner)
		if top_loser["firstTower"] is True:
			pushFirstTower(db.ChampionStats, top_loser, top_winner)
		if jungle_loser["firstTower"] is True:
			pushFirstTower(db.ChampionStats, jungle_loser, jungle_winner)
		if bot_support_winner["firstTower"] is True:
			pushFirstTower(db.ChampionStats, bot_support_winner, bot_support_loser)
		if bot_carry_winner["firstTower"] is True:
			pushFirstTower(db.ChampionStats, bot_carry_winner, bot_carry_loser)
		if mid_winner["firstTower"] is True:
			pushFirstTower(db.ChampionStats, mid_winner, mid_loser)
		if top_winner["firstTower"] is True:
			pushFirstTower(db.ChampionStats, top_winner, top_loser)
		if jungle_winner["firstTower"] is True:
			pushFirstTower(db.ChampionStats, jungle_winner, jungle_loser)

		#wins, losses
		pushWin(db.ChampionStats, bot_support_winner, bot_support_loser)
		pushLoss(db.ChampionStats, bot_support_loser, bot_support_winner)
		pushWin(db.ChampionStats, bot_carry_winner, bot_carry_loser)
		pushLoss(db.ChampionStats, bot_carry_loser, bot_carry_winner)
		pushWin(db.ChampionStats, mid_winner, mid_loser)
		pushLoss(db.ChampionStats, mid_loser, mid_winner)
		pushWin(db.ChampionStats, top_winner, top_loser)
		pushLoss(db.ChampionStats, top_loser, top_winner)
		pushWin(db.ChampionStats, jungle_winner, jungle_loser)
		pushLoss(db.ChampionStats, jungle_loser, jungle_winner)
		print("Stats from one match updated")



def incrementFirstBlood(collection, champion):
	collection.update_one({"_id": champion["championId"]},
		{"$inc": {"firstBlood": 1}})    

def pushFirstTower(collection, champion, adversary):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"firstTower": adversary["championId"]}})

def pushSeasonTier(collection, champion):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"highestAchievedSeasonTier": champion["highestAchievedSeasonTier"]}})

def pushItems(collection, champion):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"items": {"$each": champion["items"]}}})

def pushSpells(collection, champion):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"spells": {"$each": champion["spells"]}}})

def pushWin(collection, champion, adversary):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"win": adversary["championId"]}})

def pushLoss(collection, champion, adversary):
	collection.update_one({"_id": champion["championId"]},
		{"$push": {"loss": adversary["championId"]}})



if __name__ == "__main__":
	matchDataDriver()
	globalStats()
	staticData()
	fillChampStats()