package models;
import java.util.ArrayList;
import java.util.List;

/**
 * This constructor for the student class
 * @param firstName The student's first name
 * @param lastName The student's last name
 * @param id The student's ID number
 * @param faculty The student's main faculty
 * @param program The student's major
 * @param enrollmentYear The year the student began studies at the school
 */
public class Student {
    private String firstName;
    private String lastName;
    private String id;
    private String faculty; 
    private String program; 
    private int enrollmentYear; 
    private double gpa; 
    private List<Grade> courses; 


    public Student(String firstName, String lastName, String id, String faculty, String program, int enrollmentYear) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.id = id;
        this.faculty = faculty;
        this.program = program;
        this.enrollmentYear = enrollmentYear;
        this.courses = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public String getFaculty() {
        return faculty;
    }

    public void setFaculty(String faculty) {
        this.faculty = faculty;
    }

    public String getProgram() {
        return program;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setProgram(String program) {
        this.program = program;
    }

    public int getEnrollmentYear() {
        return enrollmentYear;
    }

    public void setEnrollmentYear(int enrollmentYear) {
        this.enrollmentYear = enrollmentYear;
    }


    public double getGpa() {
        return gpa;
    }

    public void setGpa(double gpa) {
        this.gpa = gpa;
    }

    public List<Grade> getcourses() {
        return courses;
    }
    /**
     * For loop that obtains the grade per course for each student
     * @param course The student's course
     * @return The grade for the course, else nothing
     */
    public Grade getGradeByCourse(String course) {
        for (Grade grade : courses) {
            if (grade.getCourse().equals(course)) {
                return grade;
            }
        }
        return null;
    }

    public void addGrade(Grade grade) {
        courses.add(grade);
    }

   
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setId(String id) {
        this.id = id;
    }


}
