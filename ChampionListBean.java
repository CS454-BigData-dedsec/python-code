package model;

import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.Mongo;

public class ChampionListBean {
	private List<Champion> champList;
	private Mongo mongo = null;
	//private Mongo mongo2 = null;
	private DB db = null;
	private DB db2 = null;
	private DBCollection table = null;
	private DBCollection table2 = null;
	
	@SuppressWarnings({ "deprecation", "unchecked" })
	public ChampionListBean(){
		champList = new ArrayList<Champion>();
		
		try{
			mongo = new Mongo("108.225.12.135", 27017);
			// Pull Champ ID, Image, and Name
			db = mongo.getDB("ChampionWin");
			table = db.getCollection("posts");
			// Pull Champs Wins, and Losses
			db2 = mongo.getDB("ChampInfo");
			table2 = db2.getCollection("info");
			
		}catch(UnknownHostException e){
			System.out.println(e.getMessage());
		}catch(Exception e){
			System.out.println(e.getMessage());
		}
		
		BasicDBObject search = new BasicDBObject();
		DBObject row = new BasicDBObject();
		DBCursor cursor2 = table2.find(search);
		while(cursor2.hasNext()){
			row = cursor2.next();
			Champion newChamp = new Champion((int)row.get("_id"), row.get("image"), (String)row.get("name"));
			champList.add(newChamp);
		}
		
		
		BasicDBObject searchQuery = new BasicDBObject();
		DBObject line = new BasicDBObject();
		
		DBCursor cursor = table.find(searchQuery);
		
	
		while(cursor.hasNext()){
			line = cursor.next();
			for(Champion champ: champList){
				if(champ.getChampionID() == (int)line.get("_id")){
					champ.setWins((int)line.get("wins"));
					champ.setLoses((int)line.get("lost"));
				}
			}
			
		}
		Collections.sort(this.champList);
		
		
		
	}
	
	public List<Champion> getChampList(){
		return this.champList;
	}
	
	
	
}
