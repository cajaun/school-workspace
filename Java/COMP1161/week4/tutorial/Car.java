package Java.COMP1161.week4.tutorial;

public class Car extends Vehicle {

  private String body;
  private String type;
  private double ccRating;
  
  public Car(String owner, String phoneNumber, int chassisNumber, String colour, int estimatedValue, int year, String body, String type, double ccRating) {
    super( owner, phoneNumber, chassisNumber,  colour, estimatedValue, year);
    this.body = body;
    this.type = type;
    this.ccRating = ccRating;
  }

  @Override
  public double getServiceCharge() {
    return 0.75 * estimatedValue / ccRating;
  }

}
