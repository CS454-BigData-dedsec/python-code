package model;

public class Spell implements Comparable{
	private int spellID;
	private String name;
	private String description;
	
	public Spell(int spellID, String name, String description){
		this.spellID = spellID;
		this.name = name;
		this.description = description;	
	}
	
	public String getName() {
		return name;
	}

	public void setName(String spellName) {
		this.name = spellName;
	}

	public int getSpellID() {
		return this.spellID;
	}
	
	public void setSpell(int spellID){
		this.spellID = spellID;
	}
	public String getDescription() {
		return description;
	}

	public void setDescription(String description){
		this.description = description;
	}

	@Override
	public String toString(){
		return "spellID : " + this.spellID + ", Name: " + this.name + " ,description: " + description;
	}

	@Override
	public int compareTo(Object o) {
		Spell other = (Spell)o;
		if(this.spellID > other.getSpellID()){
			return -1;
		}
		else if(this.spellID < other.getSpellID()){
			return 1;
		}
		return 0;
	}
	
}
