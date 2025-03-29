public class SOE extends ZOSO {
    private int numberOfRehabs;

    public static boolean canDeploy(int deploymentSize) {
        Services service = Services.getService();
        return service.soldiersAvailable(deploymentSize) && 
               service.socialAvailable(deploymentSize) && 
               service.policeAvailable(2);
    }

    public SOE(Community community, int multiplier, int rehabRate) {
        super(community, multiplier);
        Services service = Services.getService();

        int soldiersNeeded = multiplier * community.countCriminals();
        if (!canDeploy(soldiersNeeded)) {
            throw new IllegalArgumentException("Insufficient resources for SOE deployment.");
        }


        
        service.deploySocial(soldiersNeeded);


        numberOfRehabs = (int) Math.floor((rehabRate / 100.0) * community.countCriminals());
        for (int i = 0; i < numberOfRehabs && !community.getCriminals().isEmpty(); i++) {
            Criminal criminal = community.getCriminals().remove(0); 
            Resident rehabilitatedResident = new Resident(criminal.getName(), community);
            community.addResident(rehabilitatedResident); 
        }
    }

    public int countRehabs() {
        return numberOfRehabs;
    }

    @Override
    public String toString() {
        String result = "Operation " + super.getCallSign() + " to be deployed as a SOE in " + cm.getName() + ".\n";
        result += "Expect " + countArrests() + " arrest(s)";
        if (numberOfRehabs > 0) {
            result += " and " + numberOfRehabs + " rehabilitation(s).";
        }
        return result;
    }
}