package Java.COMP1161.exam.may2023.question1;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Shape> list = new ArrayList<>();

        for (int i = 1; i < 5; i++) {
            if (i % 2 == 0) {
                list.add(new Circle("Blue", i)); // i as radius
            } else {
                list.add(new Rectangle("Red", i, i + 2)); // i as length, i+2 as width
            }
        }

        int lineNumber = 1;
        for (Shape shape : list) {
            System.out.println(lineNumber + ". " + shape.toString());
            lineNumber++;
        }
    }
}

