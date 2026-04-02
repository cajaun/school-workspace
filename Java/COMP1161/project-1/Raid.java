public class Raid extends Operation {
    private int numberOfArrests; 


    public static boolean canDeploy(int numCriminalsAdjusted) {
        Services service = Services.getService();
        return service.policeAvailable(numCriminalsAdjusted);
    }


    public Raid(Community community, int multiplier) {
        super(community); 
        Services service = Services.getService();


        int totalCriminals = community.countCriminals();

        int policeNeeded = multiplier * totalCriminals;

 
        if (canDeploy(policeNeeded)) {
            service.deployPolice(policeNeeded);  

            numberOfArrests = totalCriminals;

            for (Criminal criminal : community.getCriminals()) {
                criminal.arrest();
            }
        } else {

            throw new IllegalArgumentException("Insufficient resources for Raid deployment.");
        }
    }


    public int countArrests() {
        return numberOfArrests;
    }


    @Override
    public String toString() {
        return "Operation " + super.getCallSign() + " to be deployed as a Raid in " + cm.getName() +
                ".\nExpect " + countArrests() + " arrest(s).";
    }
}
