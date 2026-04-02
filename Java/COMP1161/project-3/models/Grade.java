package models;

/**
 * This class represents the grades of each student
 * @param courseCode The code for a course that a student previously took
 * @param grade The letter grade for a course
 */
public class Grade {
    private String courseCode;
    private String grade;

    public Grade(String courseCode, String grade) {
        this.courseCode = courseCode;
        this.grade = grade;
    }
    
    public String getCourse() {
        return courseCode;
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public void setCourse (String course) {
        this.courseCode = course;
    }
}
