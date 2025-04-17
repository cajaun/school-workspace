package util;


import javax.swing.plaf.basic.BasicComboBoxUI;
import javax.swing.plaf.basic.BasicComboPopup;
import java.awt.*;
import javax.swing.plaf.basic.ComboPopup;

/**
 * A custom UI for {@code JComboBox} that allows setting a fixed height for the dropdown popup.
 * This is useful when the default calculated height of the popup is not desired.
 */
public class CustomHeightComboBoxUI extends BasicComboBoxUI {
    private final int popupHeight;

    /**
     * Constructs a {@code CustomHeightComboBoxUI} with the specified height for the dropdown popup.
     *
     * @param popupHeight The desired height (in pixels) of the combo box popup.
     */
    public CustomHeightComboBoxUI(int popupHeight) {
        this.popupHeight = popupHeight;
    }

    /**
     * Overrides the {@code createPopup()} method to return a custom {@code BasicComboPopup}.
     * The custom popup overrides the {@code getPreferredSize()} method to set a fixed height.
     *
     * @return A {@code ComboPopup} with a preferred height set to the value provided in the constructor.
     */
    @Override
    protected ComboPopup createPopup() {
        BasicComboPopup popup = new BasicComboPopup(comboBox) {
            @Override
            public Dimension getPreferredSize() {
                Dimension d = super.getPreferredSize();
                d.height = popupHeight;
                return d;
            }
        };
        popup.getAccessibleContext().setAccessibleParent(comboBox);
        return popup;
    }
}