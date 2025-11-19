package Java.COMP1161.exam.april2024.question3;

import java.util.Comparator;

public class UWIGraduate extends UWIStudent implements Comparator<UWIGraduate> {

  public String major;

  public UWIGraduate(double gpa, String name, String major) {
    super(gpa, name);
    this.major = major;
  }

  public String getMajor() {
    return major;
  }

  @Override
  public int compare(UWIGraduate u1, UWIGraduate u2) {

    int majorCompare = u1.getMajor().compareTo(u2.getMajor());
    if (majorCompare != 0) {
      return majorCompare;
    }


    return Double.compare(u2.getGPA(), u1.getGPA());
  }

  @Override
  public double getGPA() {

    return gpa >= 2.0 ? gpa : 0;
  }
}
