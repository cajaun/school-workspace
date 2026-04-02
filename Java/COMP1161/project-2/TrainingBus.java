
import java.util.Scanner;

public class TrainingBus extends Bus {
    private int teacherArea;

    /**
     * Represents a TrainingBus designed to support educational trips, with
     * additional features for teachers.
     * This class extends the general Bus class and adds a specific attribute for
     * the teacher's area.
     *
     * @param b           the base Bus object containing shared attributes
     * @param teacherArea the area designated for teachers within the bus (e.g.,
     *                    number of seats or space allocation)
     */
    public TrainingBus(Bus b, int teacherArea) {
        super(b.getName(), b.getSize(), b.getPrice(), b.getLevel(), b.getMinistry());
        this.teacherArea = teacherArea;
    }

    public int getEstimate(String type) {
        int price = super.getPrice();
        // System.out.println(this.getName()+":estimate to hold a "+type +" is "+
        // price);
        return price;

    }

    /**
     * Updates the local data of the TrainingBus based on user input.
     * This method prompts the user to update the teacher area, which represents the space allocated for the teacher(s) within the bus.
     * It reads input from the console and updates the corresponding attribute.
     *
     * @param scan the Scanner object used to read user input from the console
     * @throws NumberFormatException if the input is not a valid integer
     */

    @Override
    public void updateLocalData(Scanner scan) {
        super.updateLocalData(scan);
        System.out.println("Update Teacher Area [" + teacherArea + "]:");
        teacherArea = Integer.parseInt(scan.next());
    }

    public int getTeacherArea() {
        return teacherArea;
    }

    public void setTeacherArea(int instructorArea) {
        this.teacherArea = teacherArea;
    }

    public String toString() {
        return "ID:" + this.getId() + ";" + this.getName() + ";#Price:" + this.getPrice() + ";Teacher Area:"
                + teacherArea + "";
    }

    public String toFile() {
        return "" + this.getId() + ";" + this.getName() + ";" + this.getPrice() + ";" + teacherArea;
    }

}
