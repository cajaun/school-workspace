package Java.COMP1161.exam.april2024.question3;

public abstract class UWIStudent {

  public double gpa;
  private String name;

  public UWIStudent(double gpa, String name) {
    this.gpa = gpa;
    this.name = name;
  }

  public String getName() {
    return name;
  }

  public abstract double getGPA();
}
