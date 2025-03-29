import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Random;
import java.io.*;



public class SML {

  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new FileReader("input04.txt"));

      double taxRate = 0.15;
      Random r = new Random();

      // Comment the line below to have fun with test cases 4 and 5
      r.setSeed(7);

      String test = bufferedReader.readLine().replaceAll("\\s+$", "");

      ArrayList<Person> plist = new ArrayList<Person>();

      // MOVE DOWN BEGINNING OF COMMENT BLOCK AFTER DOING WORK TO PASS TEST CASE
      if (test.equals("CASE0-Q1")) {
          ExpatConsultant ec0 = new ExpatConsultant("2/1/2001", "Computing", 200000, taxRate, 50000);
          if (ec0 instanceof RegisteredExpat)
              System.out.println(ec0);
          else
              System.out.println("RegisteredExpat not implemented");
      }

      if (test.equals("CASE1-Q2")) {
          ExpatConsultant ec0 = new ExpatConsultant("2/1/2001", "Computing", 200000, taxRate, 50000);
          System.out.println(ec0.getWorkPermit() + ";Birthday:" + ec0.getDobDay() + "/" + ec0.getDobMonth() + "/" + ec0.getDobYear());
      }

      taxRate = 0.1;

      if (test.equals("CASE2-Q3")) {
          NineToFiver n50 = new NineToFiver("2/1/2001", "Computing", 9, 17, 5, taxRate, 200);

          if (n50 instanceof LocalResource) {
              System.out.println("LocalResource implemented");
              System.out.println(n50.getContact() + ";Birthday:" + n50.getDobDay() + "/" + n50.getDobMonth() + "/" + n50.getDobYear());
              System.out.println(n50);
          }
      }

      if (test.equals("CASE3-Q4")) {
          LocalConsultant lc0 = new LocalConsultant("2/1/2001", "Computing", 200000, taxRate);
          if (lc0 instanceof LocalResource)
              System.out.println(lc0);
      }

      if (test.equals("CASE4-Q5") || test.equals("CASE5-Q6")) {

          double basefare = 50000;
          int minwage = 100, numCases = 5;

          // Add some NineToFivers
          for (int i = 0; i < numCases; i++) {
              String birthday = getBirthDay("Jamaican", r);
              String sector = getSector(r);
              double hourlyRate = getHourlyRate(minwage, r);
              NineToFiver n5 = new NineToFiver(birthday, sector, 9, 17, 5, hourlyRate, taxRate);
              plist.add(n5);
          }

          taxRate = 0.15;

          // Add some local consultants
          for (int i = 0; i < numCases; i++) {
              String birthday = getBirthDay("Jamaican", r);
              String sector = getSector(r);
              double skillPrice = getConsultRate(r);
              LocalConsultant lc = new LocalConsultant(birthday, sector, skillPrice, taxRate);
              plist.add(lc);
          }

          // Add some expat consultants
          for (int i = 0; i < numCases; i++) {
              String birthday = getBirthDay("US/CAN", r);
              String sector = getSector(r);
              double skillPrice = getConsultRate(r);
              double airfare = getAirfare(basefare, r);
              ExpatConsultant ec = new ExpatConsultant(birthday, sector, skillPrice, taxRate, airfare);
              plist.add(ec);
          }

          // Print the list
          System.out.println("====================================");
          System.out.println("Displayed in order entered");
          System.out.println("====================================");
          for (Person p : plist)
              System.out.println(p);
          System.out.println("-------------------------------------");
      }

      if (test.equals("CASE4-Q5")) {
          System.out.println("====================================");
          System.out.println("Displayed in order of day of birth");
          System.out.println("====================================");

          // Sort the list of persons by day of birth
          Collections.sort(plist);
          for (Person p : plist)
              System.out.println(p);
          System.out.println("-------------------------------------");
      }

      if (test.equals("CASE5-Q6")) {
          System.out.println("====================================");
          System.out.println("Displayed in order of pay rate");
          System.out.println("====================================");

          Collections.sort(plist, new PayOrder());
          for (Person p : plist)
              System.out.println(p);
          System.out.println("-------------------------------------");

          System.out.println("====================================");
          System.out.println("Displayed in order of sector and pay rate");
          System.out.println("====================================");

          // Sort by sector first, then by pay rate
          plist.sort(Comparator.comparing(Person::getSector).thenComparing(new PayOrder()));

          for (Person p : plist)
              System.out.println(p);
          System.out.println("-------------------------------------");
      }
    bufferedReader.close();

  }

  static String getBirthDay(String country, Random r) {
      int d = Math.abs(r.nextInt()) % 28 + 1;
      int m = Math.abs(r.nextInt()) % 12 + 1;
      int y = 1956 + Math.abs(r.nextInt()) % 65;

      String daypart = (d < 10) ? "0" + d : "" + d;
      String monthpart = (m < 10) ? "0" + m : "" + m;
      String yearpart = "" + y;

      if (country.equals("Jamaica"))
          return daypart + "/" + monthpart + "/" + yearpart;
      else
          return monthpart + "/" + daypart + "/" + yearpart;
  }

  static String getSector(Random r) {
      String[] sectors = {"Finance", "Entertainment", "Sports", "Computing", "Medical", "Manufacturing", "Legal", "Unknown"};
      return sectors[Math.abs(r.nextInt()) % sectors.length];
  }

  static double getHourlyRate(int base, Random r) {
      return base + Math.abs(r.nextInt()) % 1000;
  }

  static double getConsultRate(Random r) {
      return Math.abs(r.nextInt()) % 500000;
  }

  static double getAirfare(double basefare, Random r) {
      return basefare + Math.abs(r.nextInt()) % 150000;
  }
}