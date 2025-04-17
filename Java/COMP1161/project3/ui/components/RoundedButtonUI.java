package ui.components;

import javax.swing.*;
import javax.swing.plaf.basic.BasicButtonUI;
import java.awt.*;

/**
 * A custom UI for {@code AbstractButton} components that renders the button with rounded corners
 * and provides visual feedback for pressed and rollover states.
 */
public class RoundedButtonUI extends BasicButtonUI {
    /**
     * Installs default properties for the button.
     * Overrides the default to set the button as non-opaque, allowing the rounded background to be visible.
     *
     * @param b The {@code AbstractButton} to install defaults for.
     */
    @Override
    public void installDefaults(AbstractButton b) {
        super.installDefaults(b);
        b.setOpaque(false);
    }

    /**
     * Paints the button's background and text with rounded corners and visual effects for different states.
     *
     * @param g The {@code Graphics} object to paint with.
     * @param c The {@code JComponent} being painted (the button).
     */
    @Override
    public void paint(Graphics g, JComponent c) {
        AbstractButton b = (AbstractButton) c;
        Graphics2D g2 = (Graphics2D) g.create();

        // Enable anti-aliasing for smooth rounded corners
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Set the background color based on the button's state
        if (b.getModel().isPressed()) {
            g2.setColor(b.getBackground().darker());
        } else if (b.getModel().isRollover()) {
            g2.setColor(Color.decode("#636B75"));
        } else {
            g2.setColor(b.getBackground());
        }

        // Fill the button area with a rounded rectangle
        int arc = 16; // The radius of the corners
        g2.fillRoundRect(0, 0, b.getWidth(), b.getHeight(), arc, arc);

        // Paint the button's text
        g2.setColor(b.getForeground());
        FontMetrics fm = g2.getFontMetrics();
        String text = b.getText();

        int textWidth = fm.stringWidth(text);
        int textHeight = fm.getHeight();

        int textX;
        // Adjust text position for left alignment
        if (b.getHorizontalAlignment() == SwingConstants.LEFT) {
            textX = 10;
        } else {
            // Center the text horizontally
            textX = (b.getWidth() - textWidth) / 2;
        }

        // Center the text vertically
        int textY = (b.getHeight() + fm.getAscent() - fm.getDescent()) / 2;

        g2.drawString(text, textX, textY);

        g2.dispose(); // Dispose of the graphics context
    }
}