package Java.COMP1161.exam.july2023.question2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class DataManager {

  String fileName;
  int numLines;

  public DataManager(String fileName) {
    this.fileName = fileName;

  }

  public ArrayList<String> open() {
    ArrayList<String> items = new ArrayList<>();

    try (Scanner scanner = new Scanner(new File(fileName))) {  

      while (scanner.hasNextLine()) { 
        String line = scanner.nextLine(); 
        items.add(line); 
      }

    } catch (FileNotFoundException e) {
      System.out.println("File not found: " + fileName);
    } catch (Exception e) {
      System.out.println("Error reading file: " + e.getMessage());
    }

    return items;
  }

}
