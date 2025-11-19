package Java.COMP1161.exam.may2023.question3;

import java.util.ArrayList;

public class Climate {

  private ArrayList<Double> temps;

  public Climate() {
    temps = new ArrayList<Double>();
  }

  public void addTemp(Double number) {
    temps.add(number);
  }

  public double avg() {
    double sum = 0;
    for (Double temp : temps) {
      sum += temp;

    }
    double result = sum / temps.size();

    return result;
  }

  public ArrayList<Double> warmer() {

    ArrayList<Double> result = new ArrayList<>();

    for (Double temp : temps) {
      if (temp > avg()) {
        result.add(temp);
      }
    }

    return result;
  }


}
