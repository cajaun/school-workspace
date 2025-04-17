package ui;

import javax.swing.*;
import com.formdev.flatlaf.FlatDarkLaf;

import models.Student;
import ui.components.RoundedButtonUI;
import ui.components.StyledPanel;
import ui.panels.AddStudent.AddStudentMenu;
import ui.panels.EditStudent.EditStudentMenu;
import ui.panels.ViewStudents.ViewStudentsMenu;
import util.Fonts;
import util.StudentUtils;

import java.awt.*;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * The {@code MainMenu} class represents the main interface of the Student Grade System application.
 * It provides a sidebar navigation to different functionalities such as adding, viewing, and editing students.
 */
public class MainMenu {
    private JFrame frame;
    private JPanel mainPanel;
    private CardLayout cardLayout;
    private List<Student> students;
    private Set<String> studentIDs = new HashSet<>();
    private JButton activeButton;

    private EditStudentMenu editStudentMenu;

    /**
     * Constructs a new {@code MainMenu} associated with an existing {@code JFrame}.
     * Initializes the UI components, sets up the layout, loads student data, and applies the look and feel.
     *
     * @param existingFrame The existing {@code JFrame} to be used for the main menu.
     */
    public MainMenu(JFrame existingFrame) {
        this.frame = existingFrame;
        frame.getContentPane().removeAll();
        frame.setTitle("Student Grade System");
        students = StudentUtils.loadStudents();
        try {
            UIManager.setLookAndFeel(new FlatDarkLaf());
        } catch (Exception e) {
            e.printStackTrace();
        }

        frame.setLayout(new BorderLayout());
        frame.add(createSidebar(), BorderLayout.WEST);
        initializeMainPanel();

        frame.setVisible(true);
        setActiveButton((JButton) ((JPanel) frame.getContentPane().getComponent(0)).getComponent(0));
    }

    /**
     * Creates the sidebar panel containing navigation buttons.
     *
     * @return A {@code JPanel} representing the sidebar.
     */
    private JPanel createSidebar() {
        JPanel sidebar = StyledPanel.createSidebarPanel();
        sidebar.setLayout(new BoxLayout(sidebar, BoxLayout.Y_AXIS));
        sidebar.setPreferredSize(new Dimension(200, frame.getHeight()));
        sidebar.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(StyledPanel.TEXT_GRAY, 1), // Colored border
                BorderFactory.createEmptyBorder(40, 10, 10, 10) // Padding inside
        ));

        JButton addStudentButton = createSidebarButton("Add Student", "add_icon.png");
        addStudentButton.addActionListener(e -> {
            showPanel("AddStudent");
            setActiveButton(addStudentButton);
        });

        JButton viewStudentsButton = createSidebarButton("View All Students", "view_icon.png");
        viewStudentsButton.addActionListener(e -> {
            reloadViewStudentsPanel();
            showPanel("ViewStudents");
            setActiveButton(viewStudentsButton);
        });

        JButton editStudentsButton = createSidebarButton("Edit Students", "edit_icon.png");
        editStudentsButton.addActionListener(e -> {
            if (students.size() > 0) {
                editStudentMenu.refresh();
                showPanel("EditStudents");
                setActiveButton(editStudentsButton);
            } else {
                JOptionPane.showMessageDialog(frame, "No students available to edit.");
            }
        });

        JButton logoutButton = createSidebarButton("Logout", "logout_icon.png");
        logoutButton.addActionListener(e -> logout());

        sidebar.add(addStudentButton);
        sidebar.add(Box.createVerticalStrut(3));
        sidebar.add(viewStudentsButton);
        sidebar.add(Box.createVerticalStrut(3));
        sidebar.add(editStudentsButton);
        sidebar.add(Box.createVerticalStrut(3));
        sidebar.add(logoutButton);

        return sidebar;
    }

    /**
     * Initializes the main panel with a {@code CardLayout} to manage different content panels.
     * Adds the initial panels for adding, viewing, and editing students.
     */
    private void initializeMainPanel() {
        cardLayout = new CardLayout();
        mainPanel = StyledPanel.createMainPanel();
        mainPanel.setLayout(cardLayout);
        mainPanel.setBackground(new Color(0, 0, 0, 0));
        frame.add(mainPanel, BorderLayout.CENTER);

        addPanel("AddStudent", createAddStudentPanel());
        addPanel("ViewStudents", new ViewStudentsMenu(students));

        editStudentMenu = new EditStudentMenu(this);
        addPanel("EditStudents", editStudentMenu);
    }

    /**
     * Creates the panel for adding new students.
     *
     * @return A {@code JPanel} containing the add student functionality.
     */
    private JPanel createAddStudentPanel() {
        return new AddStudentMenu(this, students);
    }

    /**
     * Reloads the view students panel with the latest student data.
     */
    public void reloadViewStudentsPanel() {
        students = StudentUtils.loadStudents();
        addPanel("ViewStudents", new ViewStudentsMenu(students));
    }

    /**
     * Retrieves the list of students currently loaded in the application.
     *
     * @return A {@code List} of {@code Student} objects.
     */
    public List<Student> getStudents() {
        return students;
    }

    /**
     * Adds a given component to the main panel with a specific name for the {@code CardLayout}.
     *
     * @param name  The name associated with the panel in the {@code CardLayout}.
     * @param panel The {@code JComponent} to be added to the main panel.
     */
    private void addPanel(String name, JComponent panel) {
        mainPanel.add(panel, name);
    }

    /**
     * Creates a styled button for the sidebar navigation.
     *
     * @param text     The text displayed on the button.
     * @param iconPath The path to the icon for the button (currently not used in the implementation).
     * @return A {@code JButton} with custom styling for the sidebar.
     */
    private JButton createSidebarButton(String text, String iconPath) {
        JButton button = new JButton(text);
        button.setHorizontalAlignment(SwingConstants.LEFT);
        button.setFont(Fonts.OPEN_RUNDE.deriveFont(16f));
        button.setFocusPainted(false);
        button.setForeground(StyledPanel.TEXT_WHITE);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
        button.setPreferredSize(new Dimension(200, 30));
        button.setMaximumSize(new Dimension(200, 30));
        button.setContentAreaFilled(false);
        button.setOpaque(true);
        button.setBackground(new Color(0, 0, 0, 0));
        button.setUI(new RoundedButtonUI());
        return button;
    }

    /**
     * Sets the currently active button in the sidebar, updating its background to indicate selection.
     *
     * @param button The {@code JButton} to be marked as active.
     */
    private void setActiveButton(JButton button) {
        if (activeButton != null) {
            activeButton.setBackground(new Color(0, 0, 0, 0));
        }
        activeButton = button;
        activeButton.setBackground(StyledPanel.TEXT_GRAY);
    }

    /**
     * Adds a new student to the system. Checks for duplicate student IDs before adding.
     * Saves the updated student list to persistent storage.
     *
     * @param student The {@code Student} object to be added.
     */
    public void addStudent(Student student) {
        if (studentIDs.contains(student.getId())) {
            JOptionPane.showMessageDialog(getFrame(), "Error: Student ID already exists!");
            return;
        }
        studentIDs.add(student.getId());
        students.add(student);
        StudentUtils.saveStudents(students);
    }

    /**
     * Checks if a given student ID is already taken in the system.
     *
     * @param id The student ID to check.
     * @return {@code true} if the ID is already taken, {@code false} otherwise.
     */
    public boolean isStudentIdTaken(String id) {
        return studentIDs.contains(id);
    }

    /**
     * Shows the panel with the specified name in the {@code CardLayout}.
     *
     * @param name The name of the panel to be displayed.
     */
    public void showPanel(String name) {
        cardLayout.show(mainPanel, name);
    }

    /**
     * Handles the logout functionality, displaying a message and exiting the application.
     */
    private void logout() {
        JOptionPane.showMessageDialog(frame, "You have been logged out.");
        System.exit(0);
    }

    /**
     * Retrieves the main {@code JFrame} of the application.
     *
     * @return The main {@code JFrame}.
     */
    public JFrame getFrame() {
        return frame;
    }

    /**
     * Retrieves the set of currently registered student IDs.
     *
     * @return A {@code Set} of student ID strings.
     */
    public Set<String> getStudentIDs() {
        return studentIDs;
    }
}
