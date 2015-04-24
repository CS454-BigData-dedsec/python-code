
import urllib2
import json
import re

def main():
    response = urllib2.urlopen('https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/35241849?&beginIndex=90&endIndex=100&api_key=8fc63904-e5cd-4b76-a555-4729dac804b4')
    string = response.read()        #this is a string
    gameList = json.loads(string)   #this is a json object
   
    c = string.count('matchId')
    got = urllib2.urlopen('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4')
    characters = got.read()
    champion = json.loads(characters)   #this is a json object

    for name in champion["data"].keys():
        print champion["data"][name]["name"], "=", champion["data"][name]["id"]


    #theChamps = []

    for i in range(0,c):
        print gameList["matches"][i]["matchId"] #the u' annotation is unicode.  you can ignore it
        print gameList["matches"][i]["participants"][0]["championId"] #the u' annotation is unicode.  you can ignore it
        print gameList["matches"][i]["participants"][0]["stats"]["winner"] #the u' annotation is unicode.  you can ignore it

        #print gameList["matches"][i]["ParticipantStats"][0]["winner"]
        #heChapms.append(gameList["matches"][i]["ParticipantStats"][0]["winner"])

    #for i in range(0, len(theChamps)):
           # response = urllib2.urlopen('https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/35241849?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4')



if __name__ == '__main__':
    main()
