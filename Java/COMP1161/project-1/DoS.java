import java.util.ArrayList;
public class DoS
{
    private ArrayList<Community> communities;
    private ArrayList<Operation> ops;

    private Services activeService;
    private int forceMultiplier, gangLimit, rehabRate;

    public DoS(int forceMultiplier, int gangLimit, int rehabRate, int numSoldiers, int numEquipment, int numPolice,
               int numSocial, int numSupplies)
    {
        activeService = Services.getService(numSoldiers, numEquipment, numPolice, numSocial, numSupplies);
        communities = new ArrayList<>();
        ops = new ArrayList<>();
        this.forceMultiplier = forceMultiplier;
        this.gangLimit = gangLimit;
        this.rehabRate = rehabRate;
    }

    public Services getService(){
        return activeService;
    }

    public int getForceMultiplier(){
        return forceMultiplier;
    }

    public int getGangLimit(){
        return gangLimit;
    }

    public void takeReport(String report)
    {

    }

    public String deploymentPlan()
    {
        return "";
    }

    public Community getCommunity(String cname){
        Community retval = null;
        for (Community c : communities)
            if (c.getName().equals(cname))
                retval = c;
        if (retval == null)
        {
            retval = new Community(cname);
            communities.add(retval);
        }
        return retval;
    }

    public void assessForOps() {
        double emergencyRatio = 0.3;
        
        for (Community cm : communities) {
            int numCriminals = cm.countCriminals();
            int population = cm.getPopulation();
    

            System.out.println("Debug: Assessing " + cm.getName());
            System.out.println("  Criminals: " + numCriminals + ", Population: " + population);
            
            if (numCriminals > 0) {
                if (numCriminals < gangLimit) { 

                    System.out.println("  -> Small-scale crime detected.");
                    System.out.println("  -> Checking Raid Deployability: " + Raid.canDeploy(numCriminals * forceMultiplier));

                    System.out.println("  -> Checking UnderCover Deployability: " + UnderCover.canDeploy());

                    System.out.println("  -> Checking Police Availability: " + activeService.policeAvailable(2));
                    
                    if (Raid.canDeploy(numCriminals * forceMultiplier)) {
                        System.out.println("  -> Assigning Raid");
                        ops.add(new Raid(cm, forceMultiplier));
                    } else if (UnderCover.canDeploy()){

                        System.out.println("  -> Assigning UnderCover (Raid not deployable)");
                        ops.add(new UnderCover(cm)); 
                    }
                } else { 
                    if (numCriminals < emergencyRatio * population) { 

                        System.out.println("  -> Moderate-level crime detected.");
                        System.out.println("  -> Checking ZOSO Deployability: " + ZOSO.canDeploy(numCriminals * forceMultiplier));
                        
                        if (ZOSO.canDeploy(numCriminals * forceMultiplier)) {
                            System.out.println("  -> Assigning ZOSO");
                            ops.add(new ZOSO(cm, forceMultiplier));
                        } else if (UnderCover.canDeploy()){
                            System.out.println("  -> Assigning UnderCover (ZOSO not deployable)");
                            ops.add(new UnderCover(cm)); 
                        }
                    } else { 
                        System.out.println("  -> High-level emergency detected.");
                        System.out.println("  -> Checking SOE Deployability: " + SOE.canDeploy(numCriminals * forceMultiplier));
                        
                        if (SOE.canDeploy(numCriminals * forceMultiplier)) {
                            System.out.println("  -> Assigning SOE");
                            ops.add(new SOE(cm, forceMultiplier, rehabRate));
                        } else if (UnderCover.canDeploy()){
                            System.out.println("  -> Assigning UnderCover (SOE not deployable)");
                            ops.add(new UnderCover(cm)); 
                        }
                    }
                }
            }
        }
    }
    
    
    

    public void publicPolicyReport(){
        System.out.println("=================SUMMARY FOR POLICY MAKERS=============================");
        int totOps = 0;
        int totArrests = 0;
        int totRehabs = 0;
    
        for (Operation op : ops) {
            if (op instanceof SOE) {  // Check SOE FIRST
                int arrests = ((SOE) op).countArrests();
                int rehabs = ((SOE) op).countRehabs();
                // System.out.println("Debug: SOE arrests = " + arrests + ", rehabs = " + rehabs);
                totArrests += arrests;
                totRehabs += rehabs;
                totOps++;
            } else if (op instanceof Raid) {
                int arrests = ((Raid) op).countArrests();
                // System.out.println("Debug: Raid arrests = " + arrests);
                totArrests += arrests;
                totOps++;
            } else if (op instanceof ZOSO) {
                int arrests = ((ZOSO) op).countArrests();
                // System.out.println("Debug: ZOSO arrests = " + arrests);
                totArrests += arrests;
                totOps++;
            } else if (op instanceof UnderCover) {
                // System.out.println("Debug: UnderCover operation detected.");
            }
        }
    
        String str = "We expect " + totOps + " operation(s), yielding " + totArrests + " arrest(s)";
        if (totRehabs > 0) {
            str += " and " + totRehabs + " rehab(s)";
        }
        str += ".";
        System.out.println(str);
        System.out.println("");
    }
    
    
    

    public void classifiedInformationBrief(){
        System.out.println("=================CLASSIFIED INTERNAL OPERATION BRIEF=============================");
        for (Operation op : ops)
            System.out.println(op.toString());
    }
}