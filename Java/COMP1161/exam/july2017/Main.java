package Java.COMP1161.exam.july2017;


public class Main {
    public static void main(String[] args) {

        StaffMember[] staffArray = new StaffMember[10];

       
        staffArray[0] = new Manager(1, "Alex", "Kingston", 5000.0, "Operations", 5);
        staffArray[1] = new Contractor(2, "Jordan", "Bay Street", 300.0, 40, 35, "Alpha Services", "123-456-7890");
        staffArray[2] = new PartTime(3, "Casey", "Willow Ave", 250.0, 30, 35);
        staffArray[3] = new PartTime(4, "Morgan", "Elm Road", 280.0, 38, 35);

       
        for (int i = 0; i < staffArray.length; i++) {
            if (staffArray[i] != null) {
                System.out.println(staffArray[i].toString());
                System.out.println("Payment: $" + staffArray[i].pay());
                System.out.println("------------------------------");
            }
        }
    }
}
