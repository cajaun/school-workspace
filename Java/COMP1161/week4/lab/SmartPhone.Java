class SmartPhone extends InternetThing {
  private String model;
  private int megaPixels;
  private boolean locked;

  public SmartPhone(String manufacturer, String serialNumber, String model, int megaPixels) {
      super(manufacturer, serialNumber);
      this.model = model;
      this.megaPixels = megaPixels;
      this.locked = true;
      System.out.println("Created " + this);
  }

  public void lock() {
      locked = true;
      System.out.println("Locked " + this);
  }

  public void unlock(String pw) {
      if (password.equals(pw)) {
          locked = false;
          System.out.println("Unlocked " + this);
      }
  }

  public void setPassword(String oldPassword, String newPassword) {
      if (password.equals(oldPassword)) {
          password = newPassword;
          System.out.println("Successfully changed password for " + this);
      }
  }

  public String toString() {
      return "Thing#" + getId() + "::PHONE made by " + getManufacturer() + ":Model=" + model + "@IP:" + getIPAddress();
  }
}