import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class EntryScreen {

    public EntryScreen() {
    }

    public ArrayList<Planner> managePlanners(Scanner scan, ArrayList<Planner> plans, Ministry mny, ArrayList<Bus> buses)
            throws NumberFormatException {
        ReportScreen r = new ReportScreen();
        char mchoice = 'c';
        String menu = "";
        while (mchoice != 'X') {
            String menuOptions = "[A]dd/Create planner\n[E]dit/Update planner\n";
            menuOptions += "[L]ist/Read planner\n[D]elete planner\nE[x]it\n";
            System.out.println(menuOptions);
            menu = scan.next().toUpperCase();
            mchoice = menu.charAt(0);
            switch (mchoice) {
                case 'A': {
                    Planner p = createPlanner(scan, mny, buses);
                    if (p != null) {
                        plans.add(p);
                    }
                    break;
                }
                case 'L': {
                    Collections.sort(plans);
                    r.listPlanners(plans, System.out);
                    break;
                }
                case 'E': {
                    System.out.println("Please enter the ID of the planner to be updated:");
                    int pid = Integer.parseInt(scan.next());
                    int pdx = findPlanner(plans, pid);
                    if (pdx >= 0)
                        plans.get(pdx).updateLocalData(scan);
                    else
                        System.out.println("Planner with id " + pid + " not found.");
                    break;
                }
                case 'D': {
                    System.out.println("Please enter the ID of the planner to be deleted:");
                    int pid = Integer.parseInt(scan.next());
                    int pdx = findPlanner(plans, pid);

                    if (pdx >= 0)
                        plans.remove(pdx);
                    else
                        System.out.println("Planner with id " + pid + " not found.");
                    break;
                }
            }

        }
        return plans;
    }

    public Planner createPlanner(Scanner scan, Ministry mny, ArrayList<Bus> buses) {
        Planner p = null;
        try {
            System.out.println("Please enter Planner Name:");
            String name = scan.next();
            System.out.println("Please enter Planner Budget:");
            int budget = Integer.parseInt(scan.next());
            p = new Planner(name, budget, mny, buses);
        } catch (NumberFormatException nfe) {
        }
        return p;
    }

    public int findPlanner(ArrayList<Planner> plans, int pid) {
        int pdx = -1;
        int currdx = 0;
        while ((currdx < plans.size()) && (pdx == -1)) {
            if (plans.get(currdx).getId() == pid)
                pdx = currdx;
            currdx++;

        }

        return pdx;

    }

    public void manageBuses(Scanner scan, Ministry mny, ArrayList<Bus> buses) {
        char choice = ' ';
        while (choice != 'X') {
            System.out.println("\nBus Management Menu:");
            System.out.println("[A]dd Bus");
            System.out.println("[L]ist Buses");
            System.out.println("[E]dit Bus");
            System.out.println("[X] Exit Bus Management");
            choice = scan.next().toUpperCase().charAt(0);

            switch (choice) {
                case 'A':
                    Bus b = createBus(scan, mny);
                    if (b != null) {
                        buses.add(b);
                    }
                    break;
                case 'L':
                    ReportScreen r = new ReportScreen();
                    r.listBuses(buses, System.out); // assuming this exists
                    break;
                case 'E':
                    System.out.println("Enter Bus ID to edit:");
                    int bid = Integer.parseInt(scan.next());
                    int bdx = findBus(buses, bid);
                    if (bdx >= 0) {
                        buses.get(bdx).updateLocalData(scan); // will need to be implemented
                    } else {
                        System.out.println("Bus with ID " + bid + " not found.");
                    }
                    break;
                case 'X':
                    System.out.println("Returning to main menu.");
                    break;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    public Bus createBus(Scanner scan, Ministry mny) {
        System.out.println("Select bus type:");
        System.out.println("[1] Basic Bus");
        System.out.println("[2] Training Bus");
        System.out.println("[3] Sport Bus");
        System.out.println("[4] Party Bus");
        int type = Integer.parseInt(scan.next());

        System.out.println("Enter Bus Name:");
        String name = scan.next();
        System.out.println("Enter Size:");
        int size = Integer.parseInt(scan.next());
        System.out.println("Enter Price:");
        int price = Integer.parseInt(scan.next());
        System.out.println("Enter Comfort Level:");
        int level = Integer.parseInt(scan.next());

        // Step 1: Always create a basic Bus
        Bus baseBus = new Bus(name, size, price, level, mny);

        switch (type) {
            case 1:
                return baseBus;
            case 2:
                System.out.println("Enter Teacher Area:");
                int teacherArea = Integer.parseInt(scan.next());
                return new TrainingBus(baseBus, teacherArea);
            case 3:
                System.out.println("Enter Competitor Area:");
                int compArea = Integer.parseInt(scan.next());
                System.out.println("Enter Number of Security:");
                int security = Integer.parseInt(scan.next());
                return new SportsBus(baseBus, compArea, security);
            case 4:
                System.out.println("Enter Competitor Area:");
                int compAreaP = Integer.parseInt(scan.next());
                System.out.println("Enter Number of Security:");
                int securityP = Integer.parseInt(scan.next());

                // Create a SportsBus first
                SportsBus sb = new SportsBus(baseBus, compAreaP, securityP);

                System.out.println("Enter Bar Area:");
                int barArea = Integer.parseInt(scan.next());
                return new PartyBus(sb, barArea);

            default:
                System.out.println("Invalid type.");
                return null;
        }
    }

    public int findBus(ArrayList<Bus> buses, int bid) {
        for (int i = 0; i < buses.size(); i++) {
            if (buses.get(i).getId() == bid) {
                return i; // Return the index immediately when the bus is found
            }
        }
        return -1;

    }

}
