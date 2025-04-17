package util;


import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * The {@code Fonts} class is responsible for loading and providing custom fonts
 * used throughout the application. It loads the "OpenRunde-Semibold.otf" font
 * from the assets directory. If the font loading fails, it falls back to a default "SansSerif" font.
 */
public class Fonts {

    /**
     * A static final {@code Font} object representing the "OpenRunde-Semibold" font,
     * loaded when the class is initialized.
     */
    public static final Font OPEN_RUNDE = loadFont();

    /**
     * Loads the custom font "OpenRunde-Semibold.otf" from the assets directory.
     * If the font file is not found or is in an invalid format, or if an I/O error occurs,
     * it catches the exceptions, prints the stack trace, and returns a default "SansSerif" font.
     *
     * @return The loaded "OpenRunde-Semibold" {@code Font} with a size of 20f,
     * or a default "SansSerif" {@code Font} if loading fails.
     */
    private static Font loadFont() {
        try {
            Path fontPath = Paths.get("assets", "OpenRunde-Semibold.otf");
            return Font.createFont(Font.TRUETYPE_FONT, new File(fontPath.toString())).deriveFont(20f);
        } catch (FontFormatException | IOException e) {
            e.printStackTrace();
            return new Font("SansSerif", Font.PLAIN, 20);
        }
    }
}