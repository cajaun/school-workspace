import java.util.Scanner;

public class PartyBus extends SportsBus {
    int barArea;

    /**
     * Represents a PartyBus, which is a specialized type of SportsBus, designed to accommodate social events.
     * It extends the SportsBus class and adds an attribute for the bar area.
     *
     * @param s the SportsBus object containing shared attributes
     * @param barArea the area designated for the bar within the bus
     */
    public PartyBus(SportsBus s, int barArea) {
        super(s.getBus(), s.getCompetitorArea(), s.getNumSecurity());
        this.barArea = barArea;
    }

    public int getBarArea() {
        return barArea;
    }

    public void setBarArea(int barArea) {
        this.barArea = barArea;
    }

    public String toString() {
        return "ID:" + this.getId() + ";" + this.getName() + ";#Price:" + this.getPrice() + ";Bar Area:" + barArea
                + ";#Sec:" + getNumSecurity();
    }

    public String toFile() {
        return "" + this.getId() + ";" + this.getName() + ";" + this.getPrice() + ";" + barArea + ";"
                + getNumSecurity();
    }
}
