package Java.COMP1161.exam.april2024.question1;

import java.util.ArrayList;

public class Main {





  public static void main(String[] args) {
    ArrayList<School> scList = new ArrayList<School>();

    scList.add(new School(20, "First Primary"));

    scList.add(new HighSchool(100, "jamrock ", 5));


    
  }

  public static String countSchoolTypes(ArrayList<School> scList) {
    int numSchools = scList.size();
    int numHighSchools = 0;

    for (School s : scList) {
        if (s instanceof HighSchool) {
            numHighSchools++;
        }
    }

    return "There are a total of " + numSchools + " schools, including " +
           numHighSchools + " high school(s)";
}

}
