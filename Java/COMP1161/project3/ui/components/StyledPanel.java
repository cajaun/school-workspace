package ui.components;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Rectangle2D;

/**
 * A custom {@code JPanel} with the ability to set a background color, border color,
 * and corner radius. It provides static factory methods for creating styled panels
 * for the sidebar, main content area, and welcome screen with predefined styles.
 */
public class StyledPanel extends JPanel {

    /**
     * The default background color for sidebar panels.
     */
    public static final Color SIDEBAR_BACKGROUND = Color.decode("#505D6A");
    /**
     * The default background color for the main content panels.
     */
    public static final Color MAIN_BACKGROUND = Color.decode("#636B75");
    /**
     * The default color for white text.
     */
    public static final Color TEXT_WHITE = Color.decode("#E6E6EA");
    /**
     * The default color for gray text.
     */
    public static final Color TEXT_GRAY = Color.decode("#ABB3BA");

    private Color backgroundColor = MAIN_BACKGROUND;
    private Color borderColor = new Color(60, 60, 60);
    private int cornerRadius = 12;

    /**
     * Constructs a new {@code StyledPanel} with default settings: non-opaque
     * and a preferred size of 600x400.
     */
    public StyledPanel() {
        setOpaque(false);
        setPreferredSize(new Dimension(600, 400));
    }

    /**
     * Overrides the {@code paintComponent} method to draw the background and border
     * of the panel with optional rounded corners.
     *
     * @param g The {@code Graphics} object to paint with.
     */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2d = (Graphics2D) g.create();
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        Rectangle2D.Float shape = new Rectangle2D.Float(
                0, 0, getWidth() - 1, getHeight() - 1);

        g2d.setColor(backgroundColor);
        g2d.fill(shape);

        g2d.setColor(borderColor);
        g2d.setStroke(new BasicStroke(1f));
        g2d.draw(shape);

        g2d.dispose();
    }

    /**
     * Creates a styled panel configured for use as a sidebar.
     * It sets the background color to {@code SIDEBAR_BACKGROUND}, the border color to a dark gray,
     * and a preferred width of 200 and height of 600. The corner radius is not explicitly set here.
     *
     * @return A {@code StyledPanel} with sidebar styling.
     */
    public static StyledPanel createSidebarPanel() {
        StyledPanel panel = new StyledPanel();
        panel.setBackgroundColor(SIDEBAR_BACKGROUND);
        panel.setBorderColor(new Color(50, 50, 50));
        panel.setPreferredSize(new Dimension(200, 600));
        return panel;
    }

    /**
     * Creates a styled panel configured for use as the main content area.
     * It sets the background color to {@code MAIN_BACKGROUND} and the border color to a darker gray.
     *
     * @return A {@code StyledPanel} with main panel styling.
     */
    public static StyledPanel createMainPanel() {
        StyledPanel panel = new StyledPanel();
        panel.setBackgroundColor(MAIN_BACKGROUND);
        panel.setBorderColor(new Color(40, 40, 40));
        return panel;
    }

    /**
     * Creates a styled panel configured for use as the welcome screen background.
     * It sets the background color to {@code MAIN_BACKGROUND} and the border color to a darker gray.
     *
     * @return A {@code StyledPanel} with welcome panel styling.
     */
    public static StyledPanel createWelcomePanel() {
        StyledPanel panel = new StyledPanel();
        panel.setBackgroundColor(MAIN_BACKGROUND);
        panel.setBorderColor(new Color(40, 40, 40));
        return panel;
    }

    /**
     * Gets the current background color of the panel.
     *
     * @return The background {@code Color}.
     */
    public Color getBackgroundColor() {
        return backgroundColor;
    }

    /**
     * Sets the background color of the panel and triggers a repaint.
     *
     * @param backgroundColor The new background {@code Color}.
     */
    public void setBackgroundColor(Color backgroundColor) {
        this.backgroundColor = backgroundColor;
        repaint();
    }

    /**
     * Gets the current border color of the panel.
     *
     * @return The border {@code Color}.
     */
    public Color getBorderColor() {
        return borderColor;
    }

    /**
     * Sets the border color of the panel and triggers a repaint.
     *
     * @param borderColor The new border {@code Color}.
     */
    public void setBorderColor(Color borderColor) {
        this.borderColor = borderColor;
        repaint();
    }

    /**
     * Gets the current corner radius of the panel.
     *
     * @return The corner radius as an integer.
     */
    public int getCornerRadius() {
        return cornerRadius;
    }

    /**
     * Sets the corner radius of the panel and triggers a repaint.
     * Note: The rounded corners are not currently implemented in the {@code paintComponent} method.
     *
     * @param cornerRadius The new corner radius as an integer.
     */
    public void setCornerRadius(int cornerRadius) {
        this.cornerRadius = cornerRadius;
        repaint();
    }
}