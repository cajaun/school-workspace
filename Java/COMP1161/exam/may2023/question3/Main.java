package Java.COMP1161.exam.may2023.question3;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Climate climate = new Climate();

    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter a number");
    double number = scanner.nextDouble();

    while (number != 400) {
      climate.addTemp(number);
      System.out.println("Enter a number");
      number = scanner.nextDouble();
    }
    double average = climate.avg();
    ArrayList<Double> warmerTemps = climate.warmer();

    System.out.println("\nAverage temperature: " + average);
    System.out.println("Temperatures above average:");
    for (double temp : warmerTemps) {
      System.out.println(temp);
    }

  }

}
