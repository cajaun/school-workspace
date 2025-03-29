public class Services {
    private int numSoldiers;
    private int numEquipment;
    private int numPolice;
    private int numSocialWorkers; 
    private int numSupplyKits;  

    private static Services theService;

    private Services(int numSoldiers, int numEquipment, int numPolice, int numSocial, int numSupplies) {
        this.numSoldiers = numSoldiers;
        this.numEquipment = numEquipment;
        this.numPolice = numPolice;
        this.numSocialWorkers = numSocial;
        this.numSupplyKits = numSupplies;
    }

    public static Services getService(int numSoldiers, int numEquipment, int numPolice, int numSocial, int numSupplies) {
        if (theService == null)
            theService = new Services(numSoldiers, numEquipment, numPolice, numSocial, numSupplies);

        return theService;
    }

    public static Services getService() {
        return theService;
    }

    public boolean policeAvailable(int req) {
        return numPolice >= req;
    }

    public boolean soldiersAvailable(int req) {
        return (numSoldiers >= req && numEquipment >= req);
    }

    public boolean socialAvailable(int deploymentSize) { 
        return (numSocialWorkers >= deploymentSize && numSupplyKits >= deploymentSize);
    }

    public void deployPolice(int numNeeded) {
        numPolice -= numNeeded;
    }

    public void deploySoldiers(int numNeeded) {
        numPolice -= 1;
        numSoldiers -= numNeeded;
        numEquipment -= numNeeded;
    }

    public void deploySocial(int deploymentSize) { 
        if (socialAvailable(deploymentSize)) {
            numSocialWorkers -= deploymentSize;
            numSupplyKits -= deploymentSize;
            numPolice -= 1;
        } else {
            throw new IllegalArgumentException("Insufficient resources for social deployment.");
        }
    }
}
