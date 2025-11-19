package Java.COMP1161.exam.july2023.question1;

public class Order implements Comparable<Order>{

  private int orderNumber;
  private String date;
  private static int counter = 0;

  public Order(String date) {
    orderNumber = counter++;
    this.date = date;
  }

  @Override
  public int compareTo(Order other) {
      return Integer.compare(this.orderNumber, other.orderNumber);
  }
  
}
