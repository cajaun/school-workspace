package models;

/**
 * This class calculates the letter grade of each numerical grade
 * Afterwhich, it calculates the individual GPA per course
 * Then adds it together to ger the overall GPA
 * @return The quotient of the total GPA and the number of courses
*/
public class InnercalcGPA {
    private Student student;

    public InnercalcGPA(Student student) {
        this.student = student;
    }


    public double getGPAFromGrade(Grade grade) {
        String letterGrade = grade.getGrade(); 
        switch (letterGrade) {
            case "A+": return 4.3;
            case "A":  return 4.0;
            case "A-": return 3.7;
            case "B+": return 3.3;
            case "B":  return 3.0;
            case "B-": return 2.7;
            case "C+": return 2.3;
            case "C":  return 2.0;
            case "F1": return 1.0;
            case "F2": return 0.5;
            case "F3": return 0.0;
            default:   return 0.0;
        }
    }

  
    public double calcOverallGPA() {
        double totalGPA = 0;
        int numOfcourses = 0;

        for (Grade currentGrade : student.getcourses()) {
            totalGPA += getGPAFromGrade(currentGrade);
            numOfcourses++;
        }

        if (numOfcourses == 0) {
            return 0;
        }

        return totalGPA / numOfcourses;
    }
}
