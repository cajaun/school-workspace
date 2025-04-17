package util;

import javax.swing.*;
import javax.swing.text.JTextComponent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.List;

/**
 * The {@code ComboBoxUtils} class provides a utility method to make a {@code JComboBox} searchable.
 * As the user types in the editable combo box, the dropdown list is filtered to show only items
 * that contain the typed text (case-insensitive).
 */
public class ComboBoxUtils {

    /**
     * Makes a {@code JComboBox} searchable based on user input.
     * It adds a {@code KeyListener} to the text component of the combo box's editor.
     * On each key release, it filters the items in the combo box to display only those
     * that contain the current text entered by the user. The filtering is case-insensitive.
     * The dropdown popup is shown automatically after filtering.
     *
     * @param comboBox The {@code JComboBox} to make searchable. The combo box must be editable.
     * @param fullList The complete {@code List} of items that the combo box should initially contain
     * and from which the search will be performed.
     */
    public static void makeSearchable(JComboBox<String> comboBox, List<String> fullList) {
        JTextComponent editor = (JTextComponent) comboBox.getEditor().getEditorComponent();
        editor.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                String input = editor.getText();
                comboBox.removeAllItems();
                for (String item : fullList) {
                    if (item.toLowerCase().contains(input.toLowerCase())) {
                        comboBox.addItem(item);
                    }
                }
                editor.setText(input); // Keep the typed text in the editor
                comboBox.showPopup();
            }
        });
    }
}