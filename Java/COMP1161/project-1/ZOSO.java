public class ZOSO extends Operation {
    private int numberOfArrests; 

    public static boolean canDeploy(int deploymentSize) {
        Services service = Services.getService();
        return service.soldiersAvailable(deploymentSize) && service.policeAvailable(1);
    }

    public ZOSO(Community community, int multiplier) {
        super(community);
        Services service = Services.getService();

        int soldiersNeeded = multiplier * community.countCriminals();
        if (canDeploy(soldiersNeeded)) {
            service.deploySoldiers(soldiersNeeded);
            numberOfArrests = community.countCriminals();

            for (Criminal criminal : community.getCriminals()) {
                criminal.arrest();
            }
        } else {
            throw new IllegalArgumentException("Insufficient resources for ZOSO deployment.");
        }
    }

    public int countArrests() {
        return numberOfArrests;
    }

    @Override
    public String toString() {
        return "Operation " + super.getCallSign() + " to be deployed as a ZOSO in " + cm.getName() +
                "\nExpect " + countArrests() + " arrest(s).";
    }
}
