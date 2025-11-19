package Java.COMP1161.exam.may2023.question2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Scanner;

public class Load {

public void loadData(List<Integer> data) {
    try {
        Scanner s = new Scanner(new File("data_file.txt"));
        while (s.hasNext()) {
            Integer n = new Integer(s.next());
            data.add(n);
        }
    } catch (FileNotFoundException | NumberFormatException error) {
        System.out.println(error.getMessage());
    }
}
  
}
