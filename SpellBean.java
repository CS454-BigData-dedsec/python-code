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

public class SpellBean {
	private List<Spell> spellList;
	private Mongo mongo = null;
	//private Mongo mongo2 = null;
	private DB db = null;
	private DBCollection table = null;
	
	@SuppressWarnings({ "deprecation", "unchecked" })
	public SpellBean(){
		spellList = new ArrayList<Spell>();
		
		try{
			mongo = new Mongo("108.225.12.135", 27017);
			// Pull Champ ID, Image, and Name
			db = mongo.getDB("Spells2");
			table = db.getCollection("posts");

			
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
			Spell spell = new Spell((int)row.get("_id"), (String)row.get("name"),(String)row.get("description"));
			spellList.add(spell);
		}		
	
		Collections.sort(this.spellList);
		
	}
	
	public List<Spell> getSpellList(){
		return this.spellList;
	}
	
	
	
}
