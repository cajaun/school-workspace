package Java.COMP1161.exam.may2017;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUI {

  private JButton submit, cancel;
  private JRadioButton studentRadioButton, lecturerRadioButton, labTechRadioButton;
  private JCheckBox agree;
  private JTextField username, password;


  public GUI() {

    studentRadioButton = new JRadioButton("studentRadioButton");
    studentRadioButton.addActionListener(new RadioButtonListener());



  }

  private class RadioButtonListener implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == studentRadioButton) {
            username.setText("studentRadioButton Selected");
        } else if (e.getSource() == lecturerRadioButton) {
            username.setText("lecturerRadioButton Selected");
        } else if (e.getSource() == labTechRadioButton) {
            username.setText("LABTEC");
            username.setEnabled(false); 
        }
    }
}

// private class TextFieldListener implements ActionListener {
//   @Override
//   public void actionPerformed(ActionEvent e) {

//   }
// }
  
}
