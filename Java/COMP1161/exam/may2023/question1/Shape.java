package Java.COMP1161.exam.may2023.question1;

public class Shape {
  
  private static int numShapes = 0;
  private int shapeId;
  public String lineColor;
  public String fillColor;
  final String unit = "cm";


  public Shape (String fillColor) {
    this.fillColor = fillColor;
    this.lineColor = "white";
    this.shapeId = getNewShapeId();

  }
  
  private int getNewShapeId() {
    numShapes++;
    return numShapes;
  }

  private void setLineColor(String input) {
    this.lineColor = input;
  }




}
