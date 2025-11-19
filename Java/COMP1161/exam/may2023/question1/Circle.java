package Java.COMP1161.exam.may2023.question1;

public class Circle extends Shape {

  private double radius;

  public Circle(String fillColor, double radius) {
    super(fillColor);
    this.radius = radius;

  }

  private double area() {
    return 3.14 * radius * radius;
  }
  
}
