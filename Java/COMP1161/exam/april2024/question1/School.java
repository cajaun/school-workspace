package Java.COMP1161.exam.april2024.question1;

public  class School implements Comparable<School>  {

  private int numStudents;
  protected String name;

  public School(int numStudents, String name) {
    this.numStudents = numStudents;
    this.name = name;
  }
  

  public int getNumStudents() {
    return numStudents;
  }

  @Override
  public int compareTo(School other) {
      return Integer.compare(this.numStudents, other.numStudents);
  }

}
