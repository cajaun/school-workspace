
abstract class LocalResource extends Person implements Citizen {
  private static int nextId = 0;
  private int id;
  private String sector;

  public LocalResource(String date, String sector) {
      super();
      String[] parts = date.split("/");
      super.setDob(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), Integer.parseInt(parts[2]));
      this.sector = sector;
      this.id = nextId++;
  }

  public int getId() {
      return id;
  }

  public String getSector() {
      return sector;
  }

  public String getTRN() {
      return String.valueOf(100000000 + id);
  }
}