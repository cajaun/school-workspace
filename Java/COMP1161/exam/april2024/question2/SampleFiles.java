package Java.COMP1161.exam.april2024.question2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SampleFiles {

  public void sampleFiles() {
    Scanner s = new Scanner(System.in);
    
    System.out.println("Enter a filename:");
    String filename = s.nextLine();  
    while (!filename.isEmpty()) {
        try {
            Scanner fle = new Scanner(new File(filename));
            if (fle.hasNextLine()) {
                String line = fle.nextLine();
                System.out.println(line + "\n=================");
            } else {
                System.out.println("File is empty.\n=================");
            }
            fle.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not available");
        }

        System.out.println("Enter a filename:");
        filename = s.nextLine();
    }
  }

}
