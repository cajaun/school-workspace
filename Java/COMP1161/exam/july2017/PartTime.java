package Java.COMP1161.exam.july2017;

public class PartTime  extends StaffMember {

  private double maxHours;
  private double flatRate;
  private double hoursWorked;

  public PartTime(int id, String name, String address, double maxHours, double flatRate, double hoursWorked) {
    super(id, name, address);
    this.flatRate = flatRate;
    this.hoursWorked = hoursWorked;
    this.maxHours = maxHours;
  }

  public double getFlatRate() { return flatRate; }
  public double getHoursWorked() { return hoursWorked; }
  public double getMaxHours() { return maxHours; }

  public void setFlatRate(double flatRate) { this.flatRate = flatRate; }
  public void setHoursWorked(double hoursWorked) { this.hoursWorked = hoursWorked; }
  public void setMaxHours(double maxHours) { this.maxHours = maxHours; }


  @Override
  public double pay() {
    if (hoursWorked <= maxHours) {
      return flatRate;
    } else {
      double extraHours = hoursWorked - maxHours;
      return flatRate + (extraHours * (flatRate / maxHours));
    }
  }
  
}
