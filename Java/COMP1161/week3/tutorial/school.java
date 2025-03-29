package Java.COMP1161.week3.tutorial;

public class school {

  private String name;
  private int studentCount;
  private int courseCount;
  private student[] students;
  private course[] courses;

  public static int MAXSTUDENTS = 100;
  public static int MAXCOURSES = 50;

  public school(String name) {
    this.name = name;
    this.studentCount = 0;
    this.courseCount = 0;
    this.students = new student[MAXSTUDENTS];
    this.courses = new course[MAXCOURSES];
  }

  public void addStudent(String name, char courseCode) {

    if (studentCount < MAXSTUDENTS) {
      // students[studentCount] = new student(name, courseCode);
      studentCount++;
    }
  }
  
}
