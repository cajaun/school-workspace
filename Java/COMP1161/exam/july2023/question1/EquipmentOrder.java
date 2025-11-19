package Java.COMP1161.exam.july2023.question1;

public class EquipmentOrder extends Order {

  private String serialNumber;
  private double deliveryCharge;

  public EquipmentOrder(String date, String serialNumber, double deliveryCharge) {
    super(date);
    this.serialNumber = serialNumber;
    this.deliveryCharge = deliveryCharge;
  }


  
}
