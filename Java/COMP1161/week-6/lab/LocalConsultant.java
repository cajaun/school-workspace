

class LocalConsultant extends LocalResource implements Citizen, Consultant {
  private double skillPrice, permitTax;

  public LocalConsultant(String dob, String sector, double skillPrice, double taxRate) {
      super(dob, sector);
      this.skillPrice = skillPrice;
      this.permitTax = skillPrice * taxRate;
  }

  @Override
  public double earnFromSkill() {
      return skillPrice;
  }

  @Override
  public double getPay() {
      return skillPrice - permitTax;
  }

  @Override
  public String getContact() {
      return "LocalConsultant#" + getId();
  }
}