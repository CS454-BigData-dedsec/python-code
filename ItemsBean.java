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

public class ItemsBean {
	private List<Item> itemList;
	private Mongo mongo = null;
	//private Mongo mongo2 = null;
	private DB db = null;
	private DBCollection table = null;
	
	@SuppressWarnings({ "deprecation", "unchecked" })
	public ItemsBean(){
		itemList = new ArrayList<Item>();
		
		try{
			mongo = new Mongo("108.225.12.135", 27017);
			// Pull Champ ID, Image, and Name
			db = mongo.getDB("Items2");
			table = db.getCollection("Info");

			
		}catch(UnknownHostException e){
			System.out.println(e.getMessage());
		}catch(Exception e){
			System.out.println(e.getMessage());
		}
		
		BasicDBObject search = new BasicDBObject();
		DBObject row = new BasicDBObject();
		DBCursor cursor = table.find(search);
		while(cursor.hasNext()){
			row = cursor.next();
			//Item(int itemID, Object image, String name, String description)
			Item item = new Item((int)row.get("_id"), row.get("image"), (String)row.get("name"),(String)row.get("description"));
			itemList.add(item);
		}		
	
		Collections.sort(this.itemList);
		
	}
	
	public List<Item> getItemList(){
		return this.itemList;
	}
	
	
	
}
