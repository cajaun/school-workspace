
class Refrigerator extends InternetThing {
  private double basePower;
  private double powerRating;
  private int capacity;
  private int contents = 0;

  public Refrigerator(String manufacturer, String serialNumber, double basePower, double powerRating, int capacity) {
      super(manufacturer, serialNumber);
      this.basePower = basePower;
      this.powerRating = powerRating;
      this.capacity = capacity;
      System.out.println("Created " + this.toString());
  }

  public void insertItem(int size) {
      if (contents + size < capacity) {
          contents += size;
          System.out.println("Inserted to " + this.toString());
      }
  }

  public void removeItem(int size) {
      if (contents - size > 0) {
          contents -= size;
          System.out.println("Removed from " + this.toString());
      }
  }

  @Override
  public int getPowerUse() {
      return (int) (basePower + capacity * powerRating);
  }

  public String toString() {
      return "Thing#" + getId() + "::REFRIGERATOR, made by " + getManufacturer() + ":BasePower=" + basePower +
             ":Rating=" + powerRating + "@IP:" + getIPAddress();
  }
}