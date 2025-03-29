public class Plan {

    private int numPatrons;
    private String tripType;
    private Date date;
    private int comfortLevel;

    public Plan(int numPatrons, String tripType, Date date, int comfortLevel) {
        this.numPatrons = numPatrons;
        this.tripType = tripType;
        this.date = new Date(date.getDay());
        this.comfortLevel = comfortLevel;

    }

    public int getNumPatrons() {
        return numPatrons;
    }

    public String getTripType() {
        return tripType;
    }

    public Date getDate() {
        return date;
    }

    public int getComfortLevel() {
        return comfortLevel;
    }
}
