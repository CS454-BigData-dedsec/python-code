import urllib2
import json
import re

def main():
    response = urllib2.urlopen('https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/35241849?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4')
    string = response.read()        #this is a string
    gameList = json.loads(string)   #this is a json object
   
    c = string.count('matchId')

    #theChamps = []
    print("===Game Data Sample===")
    for i in range(0,c):
        print "Match ID = ", gameList["matches"][i]["matchId"] #the u' annotation is unicode.  you can ignore it
        print "Champion ID = ", gameList["matches"][i]["participants"][0]["championId"] #the u' annotation is unicode.  you can ignore it
        print "Win = ", gameList["matches"][i]["participants"][0]["stats"]["winner"], "\n" #the u' annotation is unicode.  you can ignore it
        
        #print gameList["matches"][i]["ParticipantStats"][0]["winner"]
        #heChapms.append(gameList["matches"][i]["ParticipantStats"][0]["winner"])

    #for i in range(0, len(theChamps)):
           # response = urllib2.urlopen('https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/35241849?api_key=8fc63904-e5cd-4b76-a555-4729dac804b4')



if __name__ == '__main__':
    main()
