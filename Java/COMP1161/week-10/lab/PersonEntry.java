package Java.COMP1161.week10.lab;

import java.awt.*;
import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class PersonEntry extends JFrame {
    private JTextField txtFirstName;
    private JTextField txtLastName;
    private JTextField txtAge;
    private JCheckBox chkPublish;
    private JButton cmdSave, cmdClose;
    private PersonListing personListing;
    private PersonEntry thisForm;

    public PersonEntry(PersonListing personListing) {
        this.personListing = personListing;
        thisForm = this;

        setTitle("Entering New Person");
        setLayout(new BorderLayout());

        JPanel pnlDisplay = new JPanel();
        pnlDisplay.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        // First Name
        gbc.gridx = 0;
        gbc.gridy = 0;
        pnlDisplay.add(new JLabel("First Name:"), gbc);

        txtFirstName = new JTextField(15);
        gbc.gridx = 1;
        pnlDisplay.add(txtFirstName, gbc);

        // Last Name
        gbc.gridx = 0;
        gbc.gridy = 1;
        pnlDisplay.add(new JLabel("Last Name:"), gbc);

        txtLastName = new JTextField(15);
        gbc.gridx = 1;
        pnlDisplay.add(txtLastName, gbc);

        // Age
        gbc.gridx = 0;
        gbc.gridy = 2;
        pnlDisplay.add(new JLabel("Age:"), gbc);

        txtAge = new JTextField(3);
        gbc.gridx = 1;
        pnlDisplay.add(txtAge, gbc);

        // Will Publish Checkbox
        gbc.gridx = 0;
        gbc.gridy = 3;
        pnlDisplay.add(new JLabel("Will Publish:"), gbc);

        chkPublish = new JCheckBox();
        gbc.gridx = 1;
        pnlDisplay.add(chkPublish, gbc);

        // Command Panel
        JPanel pnlCommand = new JPanel();
        cmdSave = new JButton("Save");
        cmdClose = new JButton("Close");

        pnlCommand.add(cmdSave);
        pnlCommand.add(cmdClose);

        add(pnlDisplay, BorderLayout.CENTER);
        add(pnlCommand, BorderLayout.SOUTH);

        pack();
        setVisible(true);

        cmdSave.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String firstName = txtFirstName.getText().trim();
                String lastName = txtLastName.getText().trim();
                String ageText = txtAge.getText().trim();
                boolean publish = chkPublish.isSelected();

                if (firstName.isEmpty() || lastName.isEmpty()) {
                    JOptionPane.showMessageDialog(thisForm, "First and Last Name must be entered.", "Error",
                            JOptionPane.ERROR_MESSAGE);
                    return;
                }

                int age;
                try {
                    age = Integer.parseInt(ageText);
                    if (age < 0) {
                        JOptionPane.showMessageDialog(thisForm, "Age must be a positive number.", "Error",
                                JOptionPane.ERROR_MESSAGE);
                        return;
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(thisForm, "Age must be a valid integer.", "Error",
                            JOptionPane.ERROR_MESSAGE);
                    return;
                }

                Person newPerson = new Person(firstName + " " + lastName, age, publish);
                personListing.addPerson(newPerson);

                thisForm.setVisible(false);
            }
        });

        cmdClose.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                thisForm.setVisible(false);
            }
        });
    }
}
