enum Gender{male,female}

public class Person {

  private String initials;
  private String lastname;
  private Gender gender;
  private int dob;
  private double netWorth;
  private Address homeAddress;

  public Person () {

  }

  public Person(String init, String lname, int yearOfBirth, int genderValue, int streetNumber, String streetName, String city, String country) {

    this.initials = init;
    this.lastname = lname;
    this.dob = dob;
    this.netWorth = 0.0;
    this.gender = gender;
    this.homeAddress = new Address(streetNumber, streetName, city, country);

  }


  public updateNetWorth (double value) {

    this.netWorth += value

  }
}


public class Address {
  public int streetNumber;
  public String streetName;
  public String city;
  public String country;

  public Address () {

  }

  public Address (int streetNumber, String streetName, String city, String country) {
    this.streetNumber = streetName;
    this.streetName = streetName;
    this.city = city;
    this.country = country;
  }

  public int getStreetNumber() { return streetNumber; }
  public String getStreetName() { return streetName; }
  public String getCity() { return city; }
  public String getCountry() { return country; }



} 