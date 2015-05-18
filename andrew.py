import pymongo
import urllib2
import json
import pprint

def matchData(matchId):
    #database
    client = pymongo.MongoClient()
    db = client.test_database
    
    #api call
    webhook = ("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchId) + 
    			"?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6")
    response = urllib2.urlopen(webhook)
    json_response = json.loads(response.read())
    
    #response parsing
    match = { 	"mapId": json_response["mapId"],
    			"matchCreation": json_response["matchCreation"],
    			"matchDuration": json_response["matchDuration"],
    			"matchId": json_response["matchId"],
    			"matchMode": json_response["matchMode"],
    			"matchType": json_response["matchType"],
    			"matchVersion": json_response["matchVersion"],
    			"platformId": json_response["platformId"],
    			"queueType": json_response["queueType"],
    			"region": json_response["region"],
    			"season": json_response["season"],
    		}
    participants = json_response["participants"]
    pp = pprint.PrettyPrinter()
    pp.pprint(match)


if __name__ == "__main__":
	matchData(1721458584)
    