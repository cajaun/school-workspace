package util;

import javax.swing.*;
import ui.MainMenu;

/**
 * The {@code StudentValidator} class provides utility methods for validating student data.
 */
public class StudentValidator {

    /**
     * Validates the provided student ID to ensure it is not already taken in the system.
     * If the ID is already taken, it displays an error message to the user.
     *
     * @param id       The student ID to validate.
     * @param mainMenu The {@code MainMenu} instance to access the list of existing student IDs and the main frame for displaying messages.
     * @return {@code true} if the student ID is valid (not already taken), {@code false} otherwise.
     */
    public static boolean validateStudentData(String id, MainMenu mainMenu) {
        if (mainMenu.isStudentIdTaken(id)) {
            JOptionPane.showMessageDialog(mainMenu.getFrame(), "This Student ID is already taken.");
            return false;
        }
        return true;
    }
}