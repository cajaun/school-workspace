package ui.panels.AddStudent;

import models.Grade;
import models.Student;
import models.InnercalcGPA;
import ui.MainMenu;
import util.StudentValidator;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

/**
 * The {@code SaveStudentListener} class implements the {@code ActionListener} interface
 * to handle the event triggered when the "Save Student" button is clicked in the
 * {@code AddStudentMenu}. It retrieves the student's information from the input fields,
 * validates the data, creates a new {@code Student} object, calculates the GPA,
 * and adds the student to the system.
 */
public class SaveStudentListener implements ActionListener {
    private final JTextField firstNameField, lastNameField, idField, programField, enrollmentYearField;
    private final JComboBox<String> facultyComboBox;
    private final List<JComboBox<String>> courseComboBoxes;
    private final List<JComboBox<String>> gradeComboBoxes;
    private final MainMenu mainMenu;

    /**
     * Constructs a {@code SaveStudentListener} with references to the input fields
     * and the main application menu.
     *
     * @param firstNameField      The text field for the student's first name.
     * @param lastNameField       The text field for the student's last name.
     * @param idField             The text field for the student's ID.
     * @param programField        The text field for the student's program.
     * @param enrollmentYearField The text field for the student's enrollment year.
     * @param facultyComboBox     The combo box for selecting the student's faculty.
     * @param courseComboBoxes    The list of combo boxes for selecting courses.
     * @param gradeComboBoxes     The list of combo boxes for selecting grades.
     * @param mainMenu            The main application menu instance.
     */
    public SaveStudentListener(JTextField firstNameField, JTextField lastNameField, JTextField idField,
                               JTextField programField, JTextField enrollmentYearField,
                               JComboBox<String> facultyComboBox,
                               List<JComboBox<String>> courseComboBoxes,
                               List<JComboBox<String>> gradeComboBoxes,
                               MainMenu mainMenu) {
        this.firstNameField = firstNameField;
        this.lastNameField = lastNameField;
        this.idField = idField;
        this.programField = programField;
        this.enrollmentYearField = enrollmentYearField;
        this.facultyComboBox = facultyComboBox;
        this.courseComboBoxes = courseComboBoxes;
        this.gradeComboBoxes = gradeComboBoxes;
        this.mainMenu = mainMenu;
    }

    /**
     * Handles the action performed when the "Save Student" button is clicked.
     * It retrieves student data from the input fields, performs validation,
     * creates a new {@code Student} object with associated grades, calculates the GPA,
     * and adds the student to the system via the {@code MainMenu}.
     * Displays error messages if validation fails or if any exception occurs.
     *
     * @param e The {@code ActionEvent} that occurred.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            String firstName = firstNameField.getText();
            String lastName = lastNameField.getText();
            String id = idField.getText();
            String faculty = (String) facultyComboBox.getSelectedItem();
            String program = programField.getText();
            int enrollmentYear = Integer.parseInt(enrollmentYearField.getText());

            if (!StudentValidator.validateStudentData(id, mainMenu))
                return;

            Student newStudent = new Student(firstName, lastName, id, faculty, program, enrollmentYear);

            int filledCount = 0;
            for (int i = 0; i < courseComboBoxes.size(); i++) {
                String course = ((String) courseComboBoxes.get(i).getEditor().getItem()).trim();
                String grade = (String) gradeComboBoxes.get(i).getSelectedItem();

                if (!course.isEmpty() && grade != null && !grade.isEmpty()) {
                    newStudent.addGrade(new Grade(course, grade));
                    filledCount++;
                }
            }

            if (filledCount < 3) {
                JOptionPane.showMessageDialog(mainMenu.getFrame(), "Please fill at least 3 course/grade pairs.");
                return;
            }

            InnercalcGPA gpaCalculator = new InnercalcGPA(newStudent);
            double overallGPA = gpaCalculator.calcOverallGPA();
            newStudent.setGpa(Math.round(overallGPA * 100.0) / 100.0);

            mainMenu.addStudent(newStudent);

            // Show success message
        JOptionPane.showMessageDialog(mainMenu.getFrame(), "Student " + firstName + " " + lastName + " added successfully!");

        // Reset the form fields
        firstNameField.setText("");
        lastNameField.setText("");
        idField.setText("");
        programField.setText("");
        enrollmentYearField.setText("");
        facultyComboBox.setSelectedIndex(0);

        for (JComboBox<String> courseBox : courseComboBoxes) {
            courseBox.setSelectedItem("");
        }

        for (JComboBox<String> gradeBox : gradeComboBoxes) {
            gradeBox.setSelectedIndex(0);
        }

        } catch (Exception ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(mainMenu.getFrame(), "Error: " + ex.getMessage());
        }
    }
}