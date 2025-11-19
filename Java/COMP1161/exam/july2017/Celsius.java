package Java.COMP1161.exam.july2017;

import java.util.ArrayList;

public class Celsius {

  public static double listAverage(ArrayList<Integer> numbers) {

    int sum = 0;

    for (Integer number : numbers) {
      sum += number;

    }

    return sum / numbers.size();

  }

  public static void listRange(ArrayList<Integer> numbers) {

    int largest = numbers.get(0);;
    int smallest = numbers.get(0);

    for (Integer number: numbers) {
      if (number > largest) {
        largest = number;
      }

      if (number < smallest) {
        smallest = number;
      }


    }

    System.out.println("Smallest is: " + smallest + " & Largest is: " + largest);

  }

  

}
