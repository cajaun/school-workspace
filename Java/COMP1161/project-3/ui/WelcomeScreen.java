package ui;

import javax.swing.*;
import ui.components.RoundedButtonUI;
import ui.components.StyledPanel;
import util.Fonts;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * The {@code WelcomeScreen} class displays the initial welcome interface of the "Marked" application.
 * It shows a logo, a welcome message, the application name, and a button to navigate to the main menu.
 */
public class WelcomeScreen {

    private JFrame frame;

    /**
     * Constructs a new {@code WelcomeScreen}.
     * Initializes the frame, sets its properties, and creates and displays the welcome panel.
     */
    public WelcomeScreen() {
        frame = new JFrame("Marked");
        frame.setSize(900, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel contentPanel = StyledPanel.createWelcomePanel();
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));

        Path logoPath = Paths.get("assets", "logo.png");
        ImageIcon logoIcon = new ImageIcon(logoPath.toString());
        Image logoImage = logoIcon.getImage().getScaledInstance(200, 200, Image.SCALE_SMOOTH);
        JLabel logoLabel = new JLabel(new ImageIcon(logoImage));
        logoLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel welcomeLabel = new JLabel("Welcome to");
        welcomeLabel.setFont(Fonts.OPEN_RUNDE.deriveFont(16f));
        welcomeLabel.setForeground(Color.decode("#ABB3BA"));
        welcomeLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        welcomeLabel.setBorder(BorderFactory.createEmptyBorder(20, 0, 5, 0));

        JLabel appNameLabel = new JLabel("Marked");
        appNameLabel.setFont(Fonts.OPEN_RUNDE.deriveFont(32f));
        appNameLabel.setForeground(Color.decode("#E6E6EA"));
        appNameLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        appNameLabel.setBorder(BorderFactory.createEmptyBorder(0, 0, 30, 0));

        JButton getStartedButton = new JButton("Get started →");
        getStartedButton.setFont(Fonts.OPEN_RUNDE.deriveFont(18f));
        getStartedButton.setForeground(Color.WHITE);
        getStartedButton.setBackground(Color.decode("#505D6A"));
        getStartedButton.setFocusPainted(false);
        getStartedButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        getStartedButton.setPreferredSize(new Dimension(160, 40));
        getStartedButton.setMaximumSize(new Dimension(160, 40));
        getStartedButton.setUI(new RoundedButtonUI());
        getStartedButton.setAlignmentX(Component.CENTER_ALIGNMENT);

        getStartedButton.addActionListener(e -> {
            new MainMenu(frame);
        });

        contentPanel.add(Box.createVerticalGlue());
        contentPanel.add(logoLabel);
        contentPanel.add(welcomeLabel);
        contentPanel.add(appNameLabel);
        contentPanel.add(getStartedButton);
        contentPanel.add(Box.createVerticalGlue());

        frame.add(contentPanel, BorderLayout.CENTER);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    /**
     * The main method that launches the {@code WelcomeScreen} on the Event Dispatch Thread.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(WelcomeScreen::new);
    }
}
