package ui.panels.AddStudent;

import javax.swing.*;
import config.Constants;
import ui.components.StyledPanel;
import util.ComboBoxUtils;
import util.CustomHeightComboBoxUI;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

/**
 * The {@code StudentFormBuilder} class is responsible for creating the UI form
 * used to input student information, including personal details and course grades.
 */
public class StudentFormBuilder {
    private JTextField firstNameField, lastNameField, idField, programField, enrollmentYearField;
    private JComboBox<String> facultyComboBox;
    private List<JComboBox<String>> courseComboBoxes = new ArrayList<>();
    private List<JComboBox<String>> gradeComboBoxes = new ArrayList<>();

    /**
     * Builds the student information input form.
     *
     * @param courseList A list of available courses to populate the course selection dropdowns.
     * @return A {@code StyledPanel} containing the student information form.
     */
    public StyledPanel buildForm(List<String> courseList) {
        StyledPanel mainPanel = StyledPanel.createMainPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        mainPanel.setOpaque(false);
        mainPanel.setBackgroundColor(StyledPanel.MAIN_BACKGROUND);
        mainPanel.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createMatteBorder(0, 0, 1, 1, StyledPanel.TEXT_GRAY),
                BorderFactory.createEmptyBorder(10, 10, 10, 10)
        ));

        JPanel alignedInfoPanel = new JPanel(new BorderLayout());
        alignedInfoPanel.setOpaque(false);
        alignedInfoPanel.add(createInfoPanel(), BorderLayout.WEST);
        mainPanel.add(alignedInfoPanel);

        JPanel alignedCoursePanel = new JPanel(new BorderLayout());
        alignedCoursePanel.setOpaque(false);
        alignedCoursePanel.add(createCoursePanel(courseList), BorderLayout.WEST);
        mainPanel.add(alignedCoursePanel);

        return mainPanel;
    }

    /**
     * Creates the panel for inputting basic student information such as ID, faculty, and personal details.
     *
     * @return A {@code JPanel} containing the student's personal information fields.
     */
    private JPanel createInfoPanel() {
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setOpaque(false);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(2, 5, 2, 5);
        gbc.anchor = GridBagConstraints.WEST;

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(new JLabel("Student ID:"), gbc);
        gbc.gridx = 1;
        idField = new JTextField(15);
        panel.add(idField, gbc);

        gbc.gridy++;
        gbc.gridx = 0;
        panel.add(new JLabel("Faculty:"), gbc);
        gbc.gridx = 1;
        facultyComboBox = new JComboBox<>(Constants.FACULTIES);
        panel.add(facultyComboBox, gbc);

        gbc.gridy++;
        gbc.gridx = 0;
        panel.add(new JLabel("First Name:"), gbc);
        gbc.gridx = 1;
        firstNameField = new JTextField(15);
        panel.add(firstNameField, gbc);

        gbc.gridy++;
        gbc.gridx = 0;
        panel.add(new JLabel("Last Name:"), gbc);
        gbc.gridx = 1;
        lastNameField = new JTextField(15);
        panel.add(lastNameField, gbc);

        gbc.gridy++;
        gbc.gridx = 0;
        panel.add(new JLabel("Program:"), gbc);
        gbc.gridx = 1;
        programField = new JTextField(15);
        panel.add(programField, gbc);

        gbc.gridy++;
        gbc.gridx = 0;
        panel.add(new JLabel("Enrollment Year:"), gbc);
        gbc.gridx = 1;
        enrollmentYearField = new JTextField(15);
        panel.add(enrollmentYearField, gbc);

        return panel;
    }

    /**
     * Creates the panel for inputting course selections and corresponding letter grades.
     * It generates a fixed number of rows for course and grade selection.
     *
     * @param courseList A list of available courses to populate the course selection dropdowns.
     * @return A {@code JPanel} containing the course and grade selection fields.
     */
    private JPanel createCoursePanel(List<String> courseList) {
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setOpaque(false);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.anchor = GridBagConstraints.WEST;

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 4;
        panel.add(new JLabel("Courses & Letter Grades (min 3):"), gbc);
        gbc.gridwidth = 1;

        for (int i = 0; i < 6; i++) {
            gbc.gridy++;
            gbc.gridx = 0;
            panel.add(new JLabel("Course " + (i + 1) + ":"), gbc);

            gbc.gridx = 1;
            JComboBox<String> courseComboBox = new JComboBox<>(courseList.toArray(new String[0]));
            courseComboBox.setEditable(true);
            courseComboBox.setUI(new CustomHeightComboBoxUI(150));
            courseComboBox.setSelectedItem(null);
            ComboBoxUtils.makeSearchable(courseComboBox, courseList);
            courseComboBoxes.add(courseComboBox);
            panel.add(courseComboBox, gbc);

            gbc.gridx = 2;
            panel.add(new JLabel("Grade:"), gbc);

            gbc.gridx = 3;
            JComboBox<String> gradeComboBox = new JComboBox<>();
            gradeComboBox.addItem("");
            for (String grade : Constants.LETTER_GRADES) {
                gradeComboBox.addItem(grade);
            }
            gradeComboBox.setSelectedItem("");
            gradeComboBoxes.add(gradeComboBox);
            panel.add(gradeComboBox, gbc);
        }

        return panel;
    }

    /**
     * Retrieves the text field for the student's first name.
     *
     * @return The {@code JTextField} for the first name.
     */
    public JTextField getFirstNameField() {
        return firstNameField;
    }

    /**
     * Retrieves the text field for the student's last name.
     *
     * @return The {@code JTextField} for the last name.
     */
    public JTextField getLastNameField() {
        return lastNameField;
    }

    /**
     * Retrieves the text field for the student's ID.
     *
     * @return The {@code JTextField} for the student ID.
     */
    public JTextField getIdField() {
        return idField;
    }

    /**
     * Retrieves the text field for the student's program.
     *
     * @return The {@code JTextField} for the program.
     */
    public JTextField getProgramField() {
        return programField;
    }

    /**
     * Retrieves the text field for the student's enrollment year.
     *
     * @return The {@code JTextField} for the enrollment year.
     */
    public JTextField getEnrollmentYearField() {
        return enrollmentYearField;
    }

    /**
     * Retrieves the combo box for selecting the student's faculty.
     *
     * @return The {@code JComboBox} for the faculty.
     */
    public JComboBox<String> getFacultyComboBox() {
        return facultyComboBox;
    }

    /**
     * Retrieves the list of combo boxes for selecting courses.
     *
     * @return A {@code List} of {@code JComboBox<String>} for courses.
     */
    public List<JComboBox<String>> getCourseComboBoxes() {
        return courseComboBoxes;
    }

    /**
     * Retrieves the list of combo boxes for selecting grades.
     *
     * @return A {@code List} of {@code JComboBox<String>} for grades.
     */
    public List<JComboBox<String>> getGradeComboBoxes() {
        return gradeComboBoxes;
    }
}