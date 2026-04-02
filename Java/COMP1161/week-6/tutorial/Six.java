package Java.COMP1161.week6.tutorial;
import java.io.*;
import java.util.*;

public class Six {

    public static void main(String args[]) {
        double[] amount = new double[5];
        int indx, num = 0;
        double sum = 0;

        try {
            Scanner fileData = new Scanner(new File("fileData.txt"));
            Scanner userIn = new Scanner(System.in);

            while (fileData.hasNextLine()) {
                try {
                    System.out.print("Enter an index (0-4): ");
                    indx = Integer.parseInt(userIn.next());

                    if (indx < 0 || indx >= amount.length) {
                        System.out.println("Invalid index. Please enter a number between 0 and 4.");
                        continue;
                    }

                    String line = fileData.nextLine();
                    double value = Double.parseDouble(line);
                    amount[indx] = value;
                    num++;

                    double avg = sumArr(amount) / num;
                    System.out.println("avg: " + avg);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number format. Skipping line...");
                } catch (ArrayIndexOutOfBoundsException e) {
                    System.out.println("Index out of bounds. Please use index between 0 and 4.");
                } catch (ArithmeticException e) {
                    System.out.println("Cannot divide by zero.");
                }
            }

            fileData.close();
            userIn.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found: fileData.txt");
        }
    }

    /// Utility function to provide sum functionality
    static double sumArr(double[] arr) {
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0.01)
                sum += arr[i];
        }
        return sum;
    }


}
