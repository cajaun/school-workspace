package Java.COMP1161.exam.july2017;

public class Seasonal extends StaffMember {
  private double weeklyRate;
  private String season;

  public Seasonal(int id, String name, String address, double weeklyRate, String season) {
      super(id, name, address);
      this.weeklyRate = weeklyRate;
      this.season = season;
  }

  public double getWeeklyRate() { return weeklyRate; }
  public String getSeason() { return season; }

  public void setWeeklyRate(double weeklyRate) { this.weeklyRate = weeklyRate; }
  public void setSeason(String season) { this.season = season; }

  @Override
  public double pay() {
      return weeklyRate;
  }
}