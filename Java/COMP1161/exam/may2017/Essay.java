package Java.COMP1161.exam.may2017;

import java.util.ArrayList;

public class Essay {

  private String title;
  private String author;
  private int day;
  private int month;
  private int year;


  public Essay(String title, String author) {
    this.title = title;
    this.author = author;

  }

  public void touch(int day, int month, int year) {
    this.day = day;
    this.month = month;
    this.year = year;
  }

  public boolean touchedSince(int day, int month, int year) {
    if (this.year > year) return true;
    if (this.year == year && this.month > month) return true;
    if (this.year == year && this.month == month && this.day >= day) return true;
    return false;
  }

  @Override
  public String toString () {
    return String.format("%-30s%-20s%d-%d-%d", title, author, day, month, year);
  }

  public static void codeB () {

    ArrayList<Essay> archive = new ArrayList<>();

    for (Essay e : archive) {
      if (!e.touchedSince(1, 1, 1980)) {
          e.touch(18, 4, 2025); 
      }
  }
  }
}
