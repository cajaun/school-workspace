
import java.text.NumberFormat;

abstract class Person implements Comparable<Person> {
  private int dobYear, dobMonth, dobDay;

  public Person() {};

  public Person(int d, int m, int y)
  {
      dobYear =y;
      dobMonth=m;
      dobDay =d;
  }

  public void setDob(int d, int m, int y)
  {
      dobYear =y;
      dobMonth=m;
      dobDay =d;
  }

  public int getDobYear()
  {
      return dobYear;
  }

  public int getDobMonth()
  {
      return dobMonth;
  }

  public int getDobDay()
  {
      return dobDay;
  }

  abstract double getPay();

  abstract String getSector();	

  abstract String getContact();

  public String toString()
  {
      NumberFormat formatter = NumberFormat.getCurrencyInstance();
      return "["+getDobDay()+"]"+getContact() +" to be paid "+ formatter.format(getPay()) +" in the "+getSector() +" sector";
  }

public int compareTo(Person other) {
  return Integer.compare(this.getDobDay(), other.getDobDay());
}

}