class LightBulb extends InternetThing {
  private int lumenCount;
  private boolean lightOn;

  public LightBulb(String manufacturer, String serialNumber, int lumenCount) {
      super(manufacturer, serialNumber);
      this.lumenCount = lumenCount;
      this.lightOn = false;
      System.out.println("Created " + this);
  }

  public void turnOn() {
      lightOn = true;
      System.out.println("Turned on " + this);
  }

  public void turnOff() {
      lightOn = false;
      System.out.println("Turned off " + this);
  }

  @Override
  public int getPowerUse() {
      return lightOn ? lumenCount * super.getPowerUse() : 0;
  }
}