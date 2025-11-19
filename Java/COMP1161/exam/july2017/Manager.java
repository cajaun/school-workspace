package Java.COMP1161.exam.july2017;

public class Manager extends StaffMember {
  private double monthlySalary;
  private String division;
  private int teamSize;

  public Manager(int id, String name, String address, double monthlySalary, String division, int teamSize) {
      super(id, name, address);
      this.monthlySalary = monthlySalary;
      this.division = division;
      this.teamSize = teamSize;
  }

  public double getMonthlySalary() { return monthlySalary; }
  public String getDivision() { return division; }
  public int getTeamSize() { return teamSize; }

  public void setMonthlySalary(double monthlySalary) { this.monthlySalary = monthlySalary; }
  public void setDivision(String division) { this.division = division; }
  public void setTeamSize(int teamSize) { this.teamSize = teamSize; }

  @Override
  public double pay() {
      // Managers are paid a monthly salary, no tax here as per description
      return monthlySalary;
  }
}
