package util;

import org.json.*;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

/**
 * The {@code CourseLoader} class provides a utility method to load a list of course codes
 * from a JSON file. The JSON file is expected to have a top-level key named "courseCodes"
 * whose value is a JSON array of course code strings.
 */
public class CourseLoader {

    /**
     * Loads a list of course codes from the JSON file specified by the file path.
     * It reads the JSON file, parses it, and extracts the strings from the "courseCodes" array.
     * If the file is not found, the JSON structure is incorrect, or any other exception occurs
     * during the process, it catches the exception, prints the stack trace, and returns an empty list.
     *
     * @param filePath The path to the JSON file containing the course codes.
     * @return A {@code List} of {@code String} objects representing the loaded course codes.
     * Returns an empty list if an error occurs during loading.
     */
    public static List<String> loadCourses(String filePath) {
        List<String> courseList = new ArrayList<>();
        try {
            JSONTokener tokener = new JSONTokener(new FileReader(filePath));
            JSONObject jsonObject = new JSONObject(tokener);

            if (jsonObject.has("courseCodes")) {
                JSONArray array = jsonObject.getJSONArray("courseCodes");
                for (int i = 0; i < array.length(); i++) {
                    String course = array.optString(i, null);
                    if (course != null) {
                        courseList.add(course);
                    }
                }
            } else {
                throw new JSONException("'courseCodes' field is missing.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return courseList;
    }
}