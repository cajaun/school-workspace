package Java.COMP1161.week4.tutorial;

public class Vehicle {

  protected String owner;
  protected int chassisNumber;
  protected String phoneNumber;
  protected String colour;
  protected int estimatedValue;
  protected int year;
  protected double serviceCharge;


  public Vehicle(String owner, String phoneNumber, int chassisNumber, String colour, int estimatedValue, int year) {
    this.owner = owner;
    this.phoneNumber = phoneNumber;
    this.chassisNumber = chassisNumber;
    this.colour = colour;
    this.estimatedValue = estimatedValue;
    this.year = year;
  }

  public double getServiceCharge() {
    return 0.01 * estimatedValue;
  }


  
}
