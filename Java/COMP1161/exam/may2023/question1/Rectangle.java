package Java.COMP1161.exam.may2023.question1;

public class Rectangle extends Shape {

  private double length, width;


  public Rectangle(String fillColor, double length, double width) {
    super(fillColor);
    this.length = length;
    this.width = width;
  }

  public double area() {
    return length * width;
  }
  
}

