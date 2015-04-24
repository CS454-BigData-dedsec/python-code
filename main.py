'''
http://www.themeta.gg

This module makes an API call to a game and stores a json object to a textfile.
The JSON object is statistics on a game's relevant meta information.

'''
import urllib2
import json

class LeagueOfLegends():
    def __init__(self):
        print('League object saved')

    def parse(self):
        for champion in self.riotBannedChampions:
            riotChampionId = champion['championId']

    def __str__(self):
        print('-------------------------------------------')
        print('-------------------------------------------')
        print('riotGameId ' + str(self.riotGameId))
        print('riotPlatformId ' + str(self.riotPlatformId))
        print('riotMapId ' + str(self.riotMapId))
        print('riotGameQueueConfigId ' + str(self.riotGameQueueConfigId))
        print('riotMapId' + str(self.riotMapId))        
        print('riotPlatformId ' + str(self.riotPlatformId))
        print('-------------------------------------------')

        print('participants ' + str(self.riotParticipants))
        print('bannedChampions ' + str(self.riotBannedChampions))
        print('-------------------------------------------')
        print('-------------------------------------------')


def main():
    response = urllib2.urlopen('https://na.api.pvp.net/observer-mode/rest/' +
                'featured?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6')
    riot_response = response.read()                 #string
    riot_response = json.loads(riot_response)       #dict 
    
    buffer_game = LeagueOfLegends()
    for game in riot_response['gameList']:
        buffer_game.riotGameId = game['gameId']
        buffer_game.riotPlatformId = game['platformId']
        buffer_game.riotMapId = game['mapId']
        buffer_game.riotGameQueueConfigId = game['gameQueueConfigId']
        buffer_game.riotParticipants = game['participants']             #array
        buffer_game.riotMapId = game['mapId']
        buffer_game.riotBannedChampions = game['bannedChampions']       #array
        buffer_game.riotPlatformId = game['platformId']
        
        print(buffer_game.__str__())

if __name__ == '__main__':
    main()
