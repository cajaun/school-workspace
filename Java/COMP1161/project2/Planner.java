import java.util.ArrayList;
import java.util.Scanner;

public class Planner implements Comparable<Planner> {

    private String name;
    private int budget;
    private Ministry mny;
    private ArrayList<Bus> buses, possibleBuses;
    private int id;
    private static int nextId = 0;
    private ArrayList<Plan> plannedTrips = new ArrayList<Plan>();
    private ArrayList<Trip> approvedTrips = new ArrayList<Trip>();

    public Planner(String name, int budget, Ministry mny, ArrayList<Bus> buses) {
        this.name = name;
        this.budget = budget;
        this.mny = mny;
        this.buses = buses;
        possibleBuses = new ArrayList<Bus>();
        id = ++nextId;
    }

    public String getName() {
        return name;
    }

    public int getBudget() {
        return budget;
    }

    public int planTrip(int numPassengers, String tripType, Date date, int comfortLevel) {
        int retval = -1;
        possibleBuses.clear();
        for (Bus b : buses) {
            if (b.isSuitable(tripType)) {
                if (b.canHold(numPassengers, comfortLevel)) {
                    int bestimate = b.getEstimate(tripType, numPassengers, comfortLevel);
                    // System.out.println("Estimate for "+ b.getName() +" is "+bestimate+", budget
                    // is "+budget);
                    if (bestimate <= budget)
                        possibleBuses.add(b);
                }
                // else{
                // System.out.println(b.getName() +" cannot hold "+ numPassengers +" level
                // "+comfortLevel + " passengers");
                // }
            }
            // else{
            // System.out.println(b.getName() +" not suitable for "+ tripType +" trip.");
            // }
        }

        // System.out.println(possibleBuses.size() +" affordable buses ");
        if (possibleBuses.size() > 0) {
            double minPrice = Double.MAX_VALUE;
            Bus minBus = null;
            for (Bus ab : possibleBuses) {
                if (ab.getEstimate(tripType, numPassengers, comfortLevel) < minPrice) {
                    if (ab.available(date)) {
                        minPrice = ab.getEstimate(tripType, numPassengers, comfortLevel);
                        minBus = ab;

                    }
                }
            }
            if (minBus == null)
                System.out.println("No suitable bus is available");
            else {
                Trip trip = new Trip(tripType, numPassengers, date, comfortLevel, this);
                int reserved = minBus.reserve(trip, mny);
                if (reserved >= 0) {
                    trip.setBus(minBus);
                    payFor(minBus, tripType, numPassengers, comfortLevel);
                    retval = reserved;
                    System.out.println(name + " successfully reserved " + trip);
                }

            }
        } else
            System.out.println(name + " cannot afford to pay for any suitable buses");
        return retval;
    }

    public void payFor(Bus bus, String tripType, int numPassengers, int comfortLevel) {
        budget -= bus.getEstimate(tripType, numPassengers, comfortLevel);

    }

    public void addPlan(Plan p) {
        plannedTrips.add(p);
    }

    public void submitPlans() {
        // System.out.println(name + " submitting "+ plannedEvents.size()+ " events.");
        for (Plan pl : plannedTrips) {
            int approvid = planTrip(pl.getNumPatrons(), pl.getTripType(), pl.getDate(), pl.getComfortLevel());
            // System.out.println(approvid +":"+ pl.getNumPatrons()+
            // pl.getEventType()+pl.getDate());
        }

    }

    public static void resetId() {

        nextId = 0;
    }

    public int compareTo(Planner other) {
        return this.getName().compareTo(other.getName());
    }

    public int getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }

    public void updateLocalData(Scanner scan) {
        scan.nextLine();
        String currname = getName();
        int currBudget = getBudget();
        System.out.println("Hit enter to keep name as [" + currname + "], or enter new name:");
        String name = scan.nextLine();
        if (name.equals(""))
            name = currname;
        System.out.println("Hit enter to keep budget at [" + currBudget + "] or enter new budget:");
        String budentry = scan.nextLine();
        int budget;
        if (budentry.equals(""))
            budget = currBudget;
        else
            budget = Integer.parseInt(budentry);
        setName(name);
        setBudget(budget);

    }

    public String toString() {
        return this.getId() + ";" + this.name + ";" + this.budget + ";" + this.plannedTrips.size() + ";"
                + this.approvedTrips.size();
    }

}
