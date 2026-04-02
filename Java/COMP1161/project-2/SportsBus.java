import java.util.Scanner;

public class SportsBus extends Bus {
    private int competitorArea;
    private int numSecurity;
    private Bus bus;

    /**
     * Represents a specialized bus designed for sporting events in the Jamrock bus management system.
     * This class extends the general Bus class and adds specific attributes related to sports, such as the competitor area and security personnel.
     *
     * @param b the base Bus object containing shared attributes
     * @param competitorArea the area designated for competitors during sports events
     * @param numSecurity the number of security personnel assigned to the bus
     */

    public SportsBus(Bus b, int competitorArea, int numSecurity) {
        super(b.getName(), b.getSize(), b.getPrice(), b.getLevel(), b.getMinistry());
        bus = b;
        this.competitorArea = competitorArea;
        this.numSecurity = numSecurity;
    }

    public int getCompetitorArea() {
        return competitorArea;
    }

    public int getNumSecurity() {
        return numSecurity;
    }

    public Bus getBus() {
        return bus;
    }

    public void setCompetitorArea(int competitorArea) {
        this.competitorArea = competitorArea;
    }

    public void setNumSecurity(int numSecurity) {
        this.numSecurity = numSecurity;
    }

    public String toString() {
        return "ID:" + this.getId() + ";" + this.getName() + ";#Price:" + this.getPrice() + ";Compet Area:"
                + competitorArea + ";#Sec:" + numSecurity;
    }

    public String toFile() {
        return "" + this.getId() + ";" + this.getName() + ";" + this.getPrice() + ";" + competitorArea + ";"
                + numSecurity;
    }

}