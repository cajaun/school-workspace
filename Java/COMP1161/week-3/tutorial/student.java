package Java.COMP1161.week3.tutorial;

import java.util.ArrayList;

public class student {

  private String name;
  private ArrayList<course> coursesEnrolled;
  private ArrayList<Double> payments;
  private double amountOwed;
  private int id;
  private static int nextId = 1;

  public student(String name, String courseCode) {
    this.id = nextId++;
    this.name = name;
    this.coursesEnrolled = new ArrayList<>();
    this.amountOwed = 0.0;
    this.payments = new ArrayList<>();

  }

  public boolean requestPaymentPlan(student student) {
    return FinManager.approvePaymentPlan(student);
  }

  public String getName () {
    return name;
  }


  public double sumPayments() {
    double total = 0.0;
    for (double payment : payments) {
      total += payment;
    }

    return total;
  }

  public double sumCourses() {
    double total = 0.0;

    for (course course : coursesEnrolled) {
      total += course.getPrice();
    }

    return total;

  }

}
