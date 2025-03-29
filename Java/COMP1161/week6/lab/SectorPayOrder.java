
import java.util.Comparator;


class SectorPayOrder implements Comparator<Person> {
  public int compare(Person p1, Person p2) {
      int sectorComparison = p1.getSector().compareTo(p2.getSector());
      if (sectorComparison != 0) {
          return sectorComparison;
      }
      return Double.compare(p1.getPay(), p2.getPay());
  }
}
