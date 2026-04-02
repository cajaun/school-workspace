package Java.COMP1161.week5.tutorial;

public abstract class Vehicle {
  
  private String id;
  private String color;
  private int year;
  private double price;

  public Vehicle(String id, String color, int year, double price) {
    this.id = id;
    this.color = color;
    this.year = year;
    this.price = price;
  }

  public String getId () {
    return id;
  }

  public String getColor() {
    return color;
  }

  public int getYear() {
    return year;
  }

  public double getPrice() {
    return price;
  }

  public abstract double forceSaleValue(int currentYear);

}
