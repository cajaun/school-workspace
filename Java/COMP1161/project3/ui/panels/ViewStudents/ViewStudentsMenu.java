package ui.panels.ViewStudents;

import models.Grade;
import models.Student;
import ui.components.StyledPanel;
import util.Fonts;
import util.StudentUtils;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import javax.swing.table.TableModel;
import javax.swing.table.TableRowSorter;

import java.awt.*;
import java.util.List;
import java.util.ArrayList;

import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.CategoryChartBuilder;
import org.knowm.xchart.XChartPanel;

/**
 * The {@code ViewStudentsMenu} class displays a table of student information
 * and provides options to visualize a student's grades as a bar chart or delete
 * a student.
 */
public class ViewStudentsMenu extends StyledPanel {

    private JPanel centerPanel;
    private CardLayout cardLayout;
    private JPanel buttonPanel;
    private JButton visualizeButton, backButton, deleteButton;
    private JTable studentTable;
    private DefaultTableModel tableModel;

    /**
     * Constructs a new {@code ViewStudentsMenu} with the provided list of students.
     * Initializes the UI components, including the student table, visualization,
     * and deletion controls.
     *
     * @param students The list of {@code Student} objects to be displayed.
     */
    public ViewStudentsMenu(List<Student> students) {
        super();
        setBackgroundColor(StyledPanel.MAIN_BACKGROUND);
        setLayout(new BorderLayout());

        JLabel titleLabel = createTitleLabel();
        add(titleLabel, BorderLayout.NORTH);

        Object[][] data = prepareStudentData(students);
        tableModel = createTableModel(data);
        studentTable = createStudentTable();

        JScrollPane scrollPane = createScrollPane(studentTable);
        initializeCenterPanel(scrollPane);

        initializeButtonPanel(students);

        add(buttonPanel, BorderLayout.SOUTH);
    }

    /**
     * Creates the title label for the panel.
     */
    private JLabel createTitleLabel() {
        JLabel titleLabel = new JLabel("Student Information", SwingConstants.LEFT);
        titleLabel.setFont(Fonts.OPEN_RUNDE.deriveFont(16f));
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        return titleLabel;
    }

    /**
     * Prepares the data for the student table.
     */
    private Object[][] prepareStudentData(List<Student> students) {
        Object[][] data = new Object[students.size()][7];
        for (int i = 0; i < students.size(); i++) {
            Student s = students.get(i);
            data[i][0] = s.getId();
            data[i][1] = s.getFirstName();
            data[i][2] = s.getLastName();
            data[i][3] = s.getFaculty();
            data[i][4] = s.getProgram();
            data[i][5] = s.getEnrollmentYear();
            data[i][6] = s.getGpa();
        }
        return data;
    }

    /**
     * Creates a table model for the student table.
     */
    private DefaultTableModel createTableModel(Object[][] data) {
        String[] columnNames = { "ID", "First Name", "Last Name", "Faculty", "Program", "Enrollment Year", "GPA" };
        return new DefaultTableModel(data, columnNames) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };
    }

    /**
     * Creates the student table.
     */
    private JTable createStudentTable() {
        JTable table = new JTable(tableModel);
        TableRowSorter<TableModel> sorter = new TableRowSorter<>(tableModel);
        table.setRowSorter(sorter);
        table.setBackground(StyledPanel.MAIN_BACKGROUND);
        table.setForeground(Color.WHITE);
        table.setGridColor(new Color(80, 80, 80));
        table.setSelectionBackground(new Color(60, 60, 60));
        table.setSelectionForeground(Color.WHITE);
        table.setShowGrid(true);
        table.setOpaque(false);

        JTableHeader header = table.getTableHeader();
        header.setBackground(new Color(50, 50, 50));
        header.setForeground(Color.WHITE);
        header.setReorderingAllowed(false);
        return table;
    }

    /**
     * Creates a scroll pane for the student table.
     */
    private JScrollPane createScrollPane(JTable table) {
        JScrollPane scrollPane = new JScrollPane(table);
        scrollPane.setOpaque(false);
        scrollPane.getViewport().setOpaque(false);
        return scrollPane;
    }

    /**
     * Initializes the center panel and adds the scroll pane.
     */
    private void initializeCenterPanel(JScrollPane scrollPane) {
        cardLayout = new CardLayout();
        centerPanel = new JPanel(cardLayout);
        centerPanel.setOpaque(false);
        centerPanel.add(scrollPane, "TABLE");
        add(centerPanel, BorderLayout.CENTER);
    }

    /**
     * Initializes the button panel and sets up button actions.
     */
    private void initializeButtonPanel(List<Student> students) {
        buttonPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        buttonPanel.setOpaque(false);

        visualizeButton = new JButton("Visualize Grades");
        visualizeButton.addActionListener(e -> showGradeChart(students));
        buttonPanel.add(visualizeButton);

        deleteButton = new JButton("Delete Student");
        deleteButton.addActionListener(e -> deleteStudent(students));
        buttonPanel.add(deleteButton);

        backButton = new JButton("Back to Table");
        backButton.setVisible(false);
        backButton.addActionListener(e -> {
            cardLayout.show(centerPanel, "TABLE");
            backButton.setVisible(false);
            visualizeButton.setVisible(true);
        });
        buttonPanel.add(backButton);
    }

/**
 * Deletes the selected student from the list and updates the table and the students.json file.
 */
private void deleteStudent(List<Student> students) {
    int selectedRow = studentTable.getSelectedRow();
    if (selectedRow == -1) {
        JOptionPane.showMessageDialog(this, "Please select a student to delete.");
        return;
    }

    // Convert row index in view to model index since the table is sortable
    int modelRow = studentTable.convertRowIndexToModel(selectedRow);
    String studentId = studentTable.getValueAt(modelRow, 0).toString();

    int confirm = JOptionPane.showConfirmDialog(this,
            "Are you sure you want to delete Student ID: " + studentId + "?",
            "Confirm Delete", JOptionPane.YES_NO_OPTION);

    if (confirm == JOptionPane.YES_OPTION) {
        // Remove student from the list
        students.removeIf(s -> s.getId().equals(studentId));

        // Remove row from the table model
        tableModel.removeRow(modelRow);

        // Update the students.json file with the new list of students
        StudentUtils.saveStudents(students);

        JOptionPane.showMessageDialog(this, "Student ID: " + studentId + " deleted successfully.");
    }
}


    /**
     * Displays a bar chart visualizing the grades of the selected student in the
     * table.
     * If no student is selected, prompts the user to select one.
     *
     * @param students The list of {@code Student} objects to search from.
     */
    private void showGradeChart(List<Student> students) {
        int selectedRow = studentTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this, "Please select a student to visualize.");
            return;
        }

        int modelRow = studentTable.convertRowIndexToModel(selectedRow);
        String studentId = studentTable.getValueAt(modelRow, 0).toString();

        Student found = null;
        for (Student s : students) {
            if (s.getId().equals(studentId)) {
                found = s;
                break;
            }
        }

        if (found == null) {
            JOptionPane.showMessageDialog(this, "Student not found.");
            return;
        }

        List<String> courses = new ArrayList<>();
        List<Double> values = new ArrayList<>();
        prepareGradeData(found, courses, values);

        CategoryChart chart = createGradeChart(courses, values, found);
        displayChart(chart);

        visualizeButton.setVisible(false);
        backButton.setVisible(true);
    }

    /**
     * Prepares the grade data for the selected student.
     */
    private void prepareGradeData(Student student, List<String> courses, List<Double> values) {
        String[] gradeScale = { "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "F1", "F2", "F3" };
        double[] gradeValues = { 4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 0.0 };

        for (Grade g : student.getcourses()) {
            courses.add(g.getCourse());
            double val = 0.0;
            for (int i = 0; i < gradeScale.length; i++) {
                if (gradeScale[i].equals(g.getGrade())) {
                    val = gradeValues[i];
                    break;
                }
            }
            values.add(val);
        }
    }

    /**
     * Creates a grade chart for the selected student's grades.
     */
    private CategoryChart createGradeChart(List<String> courses, List<Double> values, Student student) {
        CategoryChart chart = new CategoryChartBuilder()
            .width(800)
            .height(400)
            .title("Grades for Student ID: " + student.getId())
            .xAxisTitle("Courses")
            .yAxisTitle("GPA")
            .build();

        chart.addSeries("GPA", courses, values);
        var series = chart.getSeriesMap().get("GPA");
        if (series != null) {
            series.setFillColor(StyledPanel.SIDEBAR_BACKGROUND);
        }

        // Apply consistent OpenRunde fonts
        chart.getStyler().setChartTitleFont(Fonts.OPEN_RUNDE.deriveFont(Font.BOLD, 14f));
        chart.getStyler().setAxisTitleFont(Fonts.OPEN_RUNDE.deriveFont(Font.PLAIN, 14f));
        chart.getStyler().setAxisTickLabelsFont(Fonts.OPEN_RUNDE.deriveFont(Font.PLAIN, 14f));

        // Apply colors and other styles
        chart.getStyler().setChartBackgroundColor(StyledPanel.MAIN_BACKGROUND);
        chart.getStyler().setPlotBackgroundColor(StyledPanel.MAIN_BACKGROUND);
        chart.getStyler().setChartFontColor(StyledPanel.TEXT_WHITE);
        chart.getStyler().setAxisTickLabelsColor(StyledPanel.TEXT_WHITE);
        chart.getStyler().setPlotGridLinesColor(StyledPanel.TEXT_GRAY);
        chart.getStyler().setLegendVisible(false);
        chart.getStyler().setXAxisLabelRotation(45);
        chart.getStyler().setAvailableSpaceFill(0.8);
        
        return chart;
    }

    /**
     * Displays the grade chart in the UI.
     */
    private void displayChart(CategoryChart chart) {
        JPanel chartPanel = new XChartPanel<>(chart);
        chartPanel.setOpaque(false);
        centerPanel.add(chartPanel, "CHART");
        cardLayout.show(centerPanel, "CHART");
    }
}
