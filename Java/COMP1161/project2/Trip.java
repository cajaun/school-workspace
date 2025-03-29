public class Trip {
    private String type;
    private int numPeople;
    private Date date;
    private Bus bus;
    private Planner planner;
    private int comfortLevel;

    public Trip(String type, int numPeople, Date date, int comfortLevel, Planner planner) {
        this.type = type;
        this.numPeople = numPeople;
        this.date = date;
        this.planner = planner;
        this.comfortLevel = comfortLevel;
    }

    public String getType() {
        return type;
    }

    public int getNumPeople() {
        return numPeople;
    }

    public Date getDate() {
        return date;
    }

    public Bus getBus() {
        return bus;
    }

    public void setBus(Bus bus) {
        this.bus = bus;
    }

    public int getComfortLevel() {
        return comfortLevel;
    }

    public String toString() {
        return "Date:" + this.getDate() + ";Type:" + this.getType() + ";Bus:" + this.getBus() + ":numPeople:"
                + this.getNumPeople();
    }

    public Planner getPlanner() {
        return planner;
    }
}
