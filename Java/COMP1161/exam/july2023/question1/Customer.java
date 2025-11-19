package Java.COMP1161.exam.july2023.question1;

import java.util.ArrayList;

public class Customer {

  private String firstName, lastName, phone;
  private ArrayList<Order> orders;

  public Customer(String firstName, String lastName, String phone, ArrayList<Order> orders) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.phone = phone;
    this.orders = orders;

  }

  public String getName() {
    return lastName  + firstName;
  }

  public void updatePhone(String newPhone) {
    this.phone = newPhone;

  }

  private void addOrder(String date) {
    Order order = new Order(date);
    orders.add(order);

  }


  
}
