package util;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import models.Student;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * The {@code StudentUtils} class provides utility methods for saving and loading
 * student data to and from a JSON file. It uses the Gson library for JSON serialization
 * and deserialization.
 */
public class StudentUtils {
    private static final Path path = Paths.get("data", "students.json");
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();

    /**
     * Saves the list of {@code Student} objects to the students.json file.
     * The student data is serialized into JSON format with pretty printing for readability.
     * Any {@code IOException} during the writing process is caught and its stack trace is printed.
     *
     * @param students The list of {@code Student} objects to be saved.
     */
    public static void saveStudents(List<Student> students) {
        try (Writer writer = new FileWriter(path.toString())) {
            GSON.toJson(students, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Loads the list of {@code Student} objects from the students.json file.
     * The JSON data is deserialized into a list of {@code Student} objects.
     * If the file is not found, an empty list is returned. Any other {@code IOException}
     * during the reading process is caught, its stack trace is printed, and an empty list is returned.
     *
     * @return A {@code List} of {@code Student} objects loaded from the file,
     * or an empty list if the file does not exist or an error occurs during reading.
     */
    public static List<Student> loadStudents() {
        try (Reader reader = new FileReader(path.toString())) {
            Type studentListType = new TypeToken<List<Student>>() {
            }.getType();
            return GSON.fromJson(reader, studentListType);
        } catch (FileNotFoundException e) {
            // If file doesn't exist, return an empty list
            return new ArrayList<>();
        } catch (IOException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
}