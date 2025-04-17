package Java.COMP1161.week5.tutorial;

public class Truck extends Vehicle implements Comparable<Truck> {

  private int tipperNumber;
  private String registrationNumber;
  private double maxLadenWeight;

  public Truck (String id, String color, int year, double price, int tipperNumber, String registrationNumber, double maxLadenWeight) {
    super(id, color, year, price);
    this.tipperNumber = tipperNumber;
    this.registrationNumber = registrationNumber;
    this.maxLadenWeight = maxLadenWeight;
  }

  public double getMaxLadenWeight() {
    return maxLadenWeight;
  }

  @Override
  public double forceSaleValue(int currentYear) {
    int age = currentYear - getYear();
    double value = getPrice();
    for (int i = 0; i < age; i++) {
      value *= 0.9;
    }

    return value;
  }

  @Override
  public int compareTo(Truck other) {
      return this.getId().compareTo(other.getId());
  }


  
}
