package model;

public class Item implements Comparable{
	private int itemID;
	private String name;
	private Object image;
	private String description;
	
	public Item(int itemID, Object image, String name, String description){
		this.itemID = itemID;
		this.name = name;
		this.image = image;
		this.description = description;
			
	}
	

	public Object getImage() {
		return image;
	}
	
	public void setImage(Object image) {
		this.image = image;
	}
	
	public String getName() {
		return name;
	}

	public void setName(String itemName) {
		this.name = itemName;
	}

	public int getItemID() {
		return this.itemID;
	}
	
	public void setItemID(int itemID){
		this.itemID = itemID;
	}
	public String getDescription() {
		return description;
	}

	public void setDescription(String description){
		this.description = description;
	}

	@Override
	public String toString(){
		return "itemID : " + this.itemID + ", Name: " + this.name + " , image: " + this.image + " ,description: " + description;
	}

	@Override
	public int compareTo(Object o) {
		Item other = (Item)o;
		if(this.itemID > other.getItemID()){
			return -1;
		}
		else if(this.itemID < other.getItemID()){
			return 1;
		}
		return 0;
	}
	
}
