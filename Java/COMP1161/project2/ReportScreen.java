import java.io.PrintStream;
import java.util.ArrayList;

public class ReportScreen {

    public ReportScreen() {
    }

    public void listPlanners(ArrayList<Planner> plist, PrintStream outStream) {
        if (outStream == System.out) {
            outStream.println("---------------Planner List---------------");
            outStream.println("ID\tName\tBudget\t#Plans\t#Trips");
            outStream.println("--------------------------------------------");
        }

        for (Planner p : plist) {
            String outline = p.toString();
            if (outStream == System.out)
                outline = outline.replace(';', '\t');
            outStream.println(outline);
        }
    }

    public void listBuses(ArrayList<Bus> blist, PrintStream outStream) {
        if (outStream == System.out)
            outStream.println("------Bus List--------");

        for (Bus b : blist)
            if (outStream == System.out)
                outStream.println(b);
            else
                outStream.println(b.toFile());
    }

}
