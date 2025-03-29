class SmartHome {
  InternetThing baseAddress, router;
  private final int MAX_THINGS = 252;
  int numThings = 0;
  public InternetThing[] things = new InternetThing[MAX_THINGS];

  public SmartHome() {
      baseAddress = new InternetThing("BASENET", "N00");
      router = new InternetThing("BASENET", "N01");
      things[baseAddress.getId()] = baseAddress;
      things[router.getId()] = router;
      System.out.println(baseAddress);
      System.out.println(router);
  }

  public int addThing(String[] args) {
      int returnval = -1;

      if (args[0].equals("REFRIGERATOR")) {
          String manufacturer = args[1];
          String serialNo = args[2];
          double basePower = Double.parseDouble(args[3]);
          double powerRating = Double.parseDouble(args[4]);
          int capacity = Integer.parseInt(args[5]);

          Refrigerator rf = new Refrigerator(manufacturer, serialNo, basePower, powerRating, capacity);
          things[rf.getId()] = rf;
          returnval = rf.getId();
      }

      if (args[0].equals("SMARTPHONE")) {
          String manufacturer = args[1];
          String serialNo = args[2];
          String model = args[3];
          int megaPix = Integer.parseInt(args[4]);

          SmartPhone sp = new SmartPhone(manufacturer, serialNo, model, megaPix);
          things[sp.getId()] = sp;
          returnval = sp.getId();
      }

      if (args[0].equals("LIGHTBULB")) {
          String manufacturer = args[1];
          String serialNo = args[2];
          int lumens = Integer.parseInt(args[3]);

          LightBulb lb = new LightBulb(manufacturer, serialNo, lumens);
          things[lb.getId()] = lb;
          returnval = lb.getId();
      }

      return returnval;
  }

  public void showItemPower(int id) {
      System.out.println(things[id].getPowerUse() + "mW\t" + things[id]);
  }

  public void showThing(int id) {
      System.out.println(things[id].toString());
  }

  public void showAllThings() {
      System.out.println("===============SHOWING ALL " + InternetThing.getNumThings() + " THINGS===============");
      for (int i = 0; i < InternetThing.getNumThings(); i++) {
          showThing(i);
      }
  }

  public void showAllPower() {
      System.out.println("===============SHOWING ALL POWER===============");
      int sumPower = 0;
      for (int i = 0; i < InternetThing.getNumThings(); i++) {
          int powerVal = things[i].getPowerUse();
          sumPower += powerVal;
          System.out.println(powerVal + "\t" + things[i]);
      }
      System.out.println("TOTAL POWER = " + sumPower + "mW");
  }
}