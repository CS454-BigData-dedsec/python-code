
import pymongo
import urllib2
import json
### this is the code i used to upload the ChampID, image, and name into Ignacios mongoDB
### simple cut up stats is what i need, not stas that im going to have to filter through to get what i want to show
def main():


    webhook = ("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=f61f7e49-9d5a-4145-84f1-cf0974bdfbbd")
    response = urllib2.urlopen(webhook)
    response = json.loads(response.read())
    image_url = "http://ddragon.leagueoflegends.com/cdn/4.2.6/img/champion/"

    #database insert
    client = pymongo.MongoClient("108.225.12.135", 27017) ## all you have to do is put his IP address and port
    db = client.ChampInfo
    db.drop_collection("ChampID")
    for champ in response["data"]:
        champ = response["data"][str(champ)]
        champ_stat = {  "name": champ["name"],
                        "_id": champ["id"],
                        "image": image_url + champ["image"]["full"] }
        db.info.insert(champ_stat)
        
    
    
    

if __name__ == '__main__':
    main()
