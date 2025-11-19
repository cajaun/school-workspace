package Java.COMP1161.exam.july2017;

public  abstract class StaffMember {

  private int id;
  private String name;
  private String address;

  public StaffMember(int id, String name, String address) {
    this.id = id;
    this.name = name;
    this.address = address;
  }

  // getters

  public int getId() { return id; }
  public String getName() {return name;}
  public String getAddress() {return address;}


  // setters

  public void setId(int id) { this.id = id; }
  public void setName(String name) { this.name = name; }
  public void setAddress(String address) { this.address = address; }

  public abstract double pay();

  public String toString() {
    return "ID: " + id + "\nName: " + name + "\nAddress: " + address;
  }
  
}
