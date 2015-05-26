package model;

import java.net.UnknownHostException;
import java.util.ArrayList;
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
	private DB db = null;
	private DBCollection table = null;
	
	@SuppressWarnings("deprecation")
	public ChampionListBean(){
		champList = new ArrayList<Champion>();
		
		try{
			mongo = new Mongo("localhost");
			db = mongo.getDB("local");
			table = db.getCollection("ChampionWin");
			
		}catch(UnknownHostException e){
			System.out.println(e.getMessage());
		}catch(Exception e){
			System.out.println(e.getMessage());
		}
		
		BasicDBObject searchQuery = new BasicDBObject();
		DBObject line = new BasicDBObject();
		
		DBCursor cursor = table.find(searchQuery);
		while(cursor.hasNext()){
			line = cursor.next();
			Champion newChamp = new Champion((int)line.get("_id"), (int)line.get("wins"), (int)line.get("lost") );
			champList.add(newChamp);
		}
	}
	
	public List<Champion> getChampList(){
		return this.champList;
	}
	
	
	
}
