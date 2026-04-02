import java.util.Comparator;

class PayOrder implements Comparator<Person> {
  public int compare(Person p1, Person p2)
  {
      if (p1.getPay()>p2.getPay())
          return 1;
      else
      {
          if (p1.getPay()<p2.getPay())
              return -1;
          else
              return 0;
      }
      //try this -- return p1.getPay() - p2.getPay();
  }

}
