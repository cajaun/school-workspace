import java.text.*;

class AssignPlan {
  private String highestPriorityItem = "";
  private int numAssignments, numComplete, hoursAvailable;
  private double totalPoints;
  DecimalFormat df = new DecimalFormat("#.##");

  private String getHighestPriorityItem() {

    return highestPriorityItem;

  }

  public int getNumAssignments() {

    return numAssignments;

  }

  public int getNumComplete() {
    

    return numComplete;

  }

  public int getHoursAvailable() {

    return hoursAvailable;

  }

  public double getTotalPoints() {

    return totalPoints;

  }

  public AssignPlan(String highestPriority, int numberOfAssigns, int numberComplete, int hoursAvail, double totPoints) {

    this.highestPriorityItem = highestPriority;
    this.numAssignments = numberOfAssigns;
    this.numComplete = numberComplete;
    this.hoursAvailable = hoursAvail;
    this.totalPoints = totPoints;

  }

  public void setPriorityTo(String aname) {

    this.highestPriorityItem = aname;

  }

  public void setAssigns(int numAssigns) {
    numAssignments = numAssigns;
  }

  public void handleAssignment(int effort) {

    hoursAvailable -= effort;
    totalPoints++;
    numComplete++;

  }

  public void handleUrgentAssignment(String name, int effort, int resources, int difficulty) {
    setPriorityTo(name);
    Assignment newAssignment = new Assignment(effort, resources, difficulty);

    this.numComplete++;
    this.hoursAvailable -= effort;
    this.totalPoints += newAssignment.getExpectedScore();
  }

  public String toString() {
    return "Priority:" + getHighestPriorityItem() + "\n"
        + "Assignments:" + getNumAssignments() + "\n"
        + "Complete:" + getNumComplete() + "\n"
        + "Hours Avail:" + getHoursAvailable() + "\n"
        + "Tot. Points:" + df.format(getTotalPoints()) + "\n";

  }

  public AssignPlan() {
  }

  public AssignPlan(int numAssigns) {
    numAssignments = numAssigns;
  }

}


