package model;

public class Champion {
	private int championID;
	private String championName;
	private int wins;
	private int loses;
	
	public Champion(int id, int wins, int loses){
		this.championID = id;
		this.wins = wins;
		this.loses = loses;
	}

	public String getChampionName() {
		return championName;
	}

	public void setChampionName(String championName) {
		this.championName = championName;
	}

	public int getChampionID() {
		return championID;
	}

	public int getWins() {
		return wins;
	}

	public int getLoses() {
		return loses;
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
		return "Champion Name: " + this.championName + ", ChampionID: " + this.championID + " , Wins: " + this.wins + " , Loses: " + this.loses +
				", WinRatio: " + getWinRatio() + ", LossRatio: " + getLossRatio();
	}
	
}
