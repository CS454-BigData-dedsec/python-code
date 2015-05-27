package model;

public class Champion implements Comparable{
	private int championID;
	private String name;
	private Object image;
	private int wins;
	private int loses;
	
	public Champion(int championID, Object image, String name){
		this.championID = championID;
		this.name = name;
		this.image = image;
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

	public void setName(String championName) {
		this.name = championName;
	}

	public int getChampionID() {
		return this.championID;
	}

	public int getWins() {
		return wins;
	}

	public void setWins(int wins){
		this.wins = wins;
	}
	public int getLoses() {
		return loses;
	}
	
	public void setLoses(int loses){
		this.loses = loses;
	}

	public double getWinRatio() {
		return this.wins/(double)getNumberOfGames();
	}

	public double getLossRatio() {
		return this.loses/(double)getNumberOfGames();
		
	}
	
	public int getNumberOfGames(){
		return this.wins + this.loses;
	}
	
	@Override
	public String toString(){
		return "Champion Name: " + this.name + ", ChampionID: " + this.championID + " , Wins: " + this.wins + " , Loses: " + this.loses +
				", WinRatio: " + getWinRatio() + ", LossRatio: " + getLossRatio();
	}

	@Override
	public int compareTo(Object o) {
		Champion other = (Champion)o;
		if(this.getWinRatio() > other.getWinRatio()){
			return -1;
		}
		else if(this.getWinRatio() < other.getWinRatio()){
			return 1;
		}
		return 0;
	}
	
}
