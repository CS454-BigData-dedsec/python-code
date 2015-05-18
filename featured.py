'''
http://www.themeta.gg

Queries Riot API
https://na.api.pvp.net/observer-mode/rest/featured?
api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6

Constructs an object: LeagueOfLegends and stores values

'''
import urllib2
import json

class LeagueOfLegends():
    '''
    self.variables
    ---------------------------------------------------
    riotGameId: int
    riotPlatformId: string (ex. NA1)
    riotMapId:  int (11 is summoner's rift)
    riotGameQueueConfigId: int (4 is ranked solo queue)
    riotParticipants: list of dictionary{???}
    riotBannedChampions:  list of dictary{???}
    banned:  list of championIds
    played:  list of championIds
    spell:  list of spellIds
    '''

    def __init__(self):
        self.riotGameId = int
        self.riotPlatformId = None
        self.riotMapId = int
        self.riotGameQueueConfigId = int
        self.riotParticipants = []
        self.riotBannedChampions = []
        self.banned = []
        self.spell = []
        self.played = []

    def parse(self, game):
        self.riotGameId = game['gameId']
        self.riotPlatformId = game['platformId']
        self.riotMapId = game['mapId']
        self.riotGameQueueConfigId = game['gameQueueConfigId']
        self.riotParticipants = game['participants']             #list
        self.riotBannedChampions = game['bannedChampions']       #list
        #parses the lists
        self.banned = []
        for champion in self.riotBannedChampions:
            self.banned.append(champion['championId'])
        self.played = []
        self.spell =[]
        for participant in self.riotParticipants:
            if(participant['bot']) == True:
                break
            self.played.append(participant['championId'])
            self.spell.append(participant['spell1Id'])
            self.spell.append(participant['spell2Id'])
        #end parse

    def display(self):
        print('riotGameId ' + str(self.riotGameId))
        print('riotPlatformId ' + str(self.riotPlatformId))
        print('riotMapId ' + str(self.riotMapId))
        print('riotGameQueueConfigId ' + str(self.riotGameQueueConfigId))
        print('played: ' + str(self.played))
        print('banned: ' + str(self.banned))
        print('spell: ' + str(self.spell))
        print('-------------------------------------------')

    def store(self):
        f = open('riot-featured-log.txt', 'a')
        f.write('riotGameId:' + str(self.riotGameId) + '\n')
        f.write('riotPlatformId:' + str(self.riotPlatformId) + '\n')
        f.write('riotMapId:' + str(self.riotMapId) + '\n')
        f.write('riotGameQueueConfigId:' + str(self.riotGameQueueConfigId) + '\n')
        f.write('played:' + str(self.played) + '\n')
        f.write('banned:' + str(self.banned) + '\n')
        f.write('spell:' + str(self.spell) + '\n')
        f.write('-' + '\n')
        f.flush()

def matchData():
    r = urllib2.urlopen('https://na.api.pvp.net/observer-mode/rest/' +
                'featured?api_key=e63ca19d-7ce7-4fc7-9b85-35759aab7ec6')
    rr = json.loads(r.read()) #dict
    l = LeagueOfLegends()
    for game in rr['gameList']:
        l.parse(game)  #parses the dict
        l.display()
        l.store()

if __name__ == '__main__':
    matchData(1721458584)
