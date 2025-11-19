package Java.COMP1161.exam.july2017;

public class Contractor extends PartTime {
  private String companyName;
  private String phoneNumber;

  public Contractor(int id, String name, String address, double flatRate, double hoursWorked, double maxHours,
                    String companyName, String phoneNumber) {
      super(id, name, address, flatRate, hoursWorked, maxHours);
      this.companyName = companyName;
      this.phoneNumber = phoneNumber;
  }

  public String getCompanyName() { return companyName; }
  public String getPhoneNumber() { return phoneNumber; }

  public void setCompanyName(String companyName) { this.companyName = companyName; }
  public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; }

  @Override
  public String toString() {
      return "Contractor Details:\n" +
             "Name: " + getName() + "\n" +
             "ID: " + getId() + "\n" +
             "Company: " + companyName + "\n" +
             "Phone: " + phoneNumber;
  }
}
