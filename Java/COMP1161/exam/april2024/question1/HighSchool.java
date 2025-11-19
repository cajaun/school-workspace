package Java.COMP1161.exam.april2024.question1;

import Java.COMP1161.week3.tutorial.school;

public class HighSchool extends School {

  private int numStudentGroups;


  public HighSchool(int numStudents, String name, int numStudentGroups) {
    super(numStudents, name);
    this.numStudentGroups = numStudentGroups;
  }

  public double getAvgGroupSize() {
    return getNumStudents()/numStudentGroups;
  }


  
}
