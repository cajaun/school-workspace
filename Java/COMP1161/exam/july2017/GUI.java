package Java.COMP1161.exam.july2017;

import javax.swing.JButton;
import javax.swing.JTextField;

public class GUI {

  private JButton convertButton;
  private JButton resetButton;
  private JTextField input;
  private JTextField output;
 

  public GUI() {
    convertButton = new JButton("convert");
    resetButton = new JButton("convert");
    input = new JTextField(5);
    output = new JTextField(5);


    convertButton.addActionListener(e -> {
      try {
        double result = Double.parseDouble((input.getText())) * 0.3;
        output.setText("Result: " + result);
      } catch(NumberFormatException ex) {


      }
      
    });

    resetButton.addActionListener(e -> {
      input.setText("");
      output.setText("");

    });

  }

  
}
