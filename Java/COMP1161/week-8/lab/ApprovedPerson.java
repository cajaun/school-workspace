package Java.COMP1161.week8.lab;
import java.util.ArrayList;

public class ApprovedPerson extends BasePerson implements Comparable<ApprovedPerson> {
    ArrayList<String> safeReqs;

    public ApprovedPerson(int age, String name, boolean publish, int id) {
        super(name, age, publish);
        super.setId(id);
        safeReqs = new ArrayList<String>();

    }

    public void addSafeReq(String sreq) {
        safeReqs.add(sreq);
    }

    public ArrayList<String> getSafeReqs() {
        return safeReqs;
    }

    public int compareTo(ApprovedPerson ap) {
        return ap.getAge() - this.getAge();
    }

    public String getName() {
        String returnval = "";
        String[] nameparts = name.split(" ");
        if (nameparts.length == 1)
            returnval = nameparts[0];
        if (nameparts.length == 2)
            returnval = nameparts[1] + ", " + nameparts[0];

        return returnval;
    }

    public String getSimpleName() {
        return name;
    }

    public static String getAPHeader() {
        String returnval = "ID\tName\t\tSafety_Requirements";
        returnval += "\n---------------------------------";
        return returnval;

    }

    public String toString() {
        return (getId() + "\t" + getName() + "\t\t" + getSafeReqs());
    }

}
