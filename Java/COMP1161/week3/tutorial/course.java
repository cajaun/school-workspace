package Java.COMP1161.week3.tutorial;
import java.util.ArrayList;


public class course {

  private int id;
  private static int nextId = 1;
  private String name;
  private double price;
  private double cost;
  private ArrayList<student> studentsEnrolled;
  private int studentCount;

  public course(String name, double price, double cost) {
      this.id = nextId++;
      this.name = name;
      this.price = price;
      this.cost = cost;
      this.studentsEnrolled = new ArrayList<>();
      this.studentCount = 0;

  }

  public void linkStudent(student student) {

    if (!studentsEnrolled.contains(student)) {
      studentsEnrolled.add(student);
      studentCount++;
    } else {
      System.out.println(student.getName() + "is already enrolled");
    }

  }

  public double getPrice() {
    return price;
  }

  public double getCost() {
    return cost;
  }




  
}
