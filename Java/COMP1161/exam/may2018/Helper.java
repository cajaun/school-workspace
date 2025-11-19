package Java.COMP1161.exam.may2018;

import java.util.ArrayList;
import java.util.Scanner;

public class Helper {


  public static double mean(double[] arr) {
      double sum = 0;
      for (double num : arr) {
          sum += num;
      }
      return arr.length > 0 ? sum / arr.length : 0;
  }

  
  public static ArrayList<Double> lower(double[] arr) {
      double avg = mean(arr);
      ArrayList<Double> result = new ArrayList<>();
      for (double num : arr) {
          if (num < avg) {
              result.add(num);
          }
      }
      return result;
  }

  public static void main (String[] agrs) {

    double[] tempList = new double[7];

    Scanner scanner = new Scanner(System.in);

            System.out.println("Enter 7 temperature readings (one for each day):");
            for (int i = 0; i < 7; i++) {
                System.out.print("Day " + (i + 1) + ": ");
                tempList[i] = scanner.nextInt();  
            }

            double average = mean(tempList);
            System.out.printf("\nAverage temperature: %.2f\n", average);
    
     
            System.out.println("Temperatures below average:");
            ArrayList<Double> belowAverageTemps = Helper.lower(tempList);
            if (belowAverageTemps.isEmpty()) {
                System.out.println("No temperatures below average.");
            } else {
                for (double temp : belowAverageTemps) {
                    System.out.println(temp);
                }
            }
    
            scanner.close(); 
  }
}
