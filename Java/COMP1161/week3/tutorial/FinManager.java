package Java.COMP1161.week3.tutorial;

public class FinManager {
  public static boolean approvePaymentPlan(student student) {
    double amountOwed = student.sumCourses();  // Total amount owed by the student
    double amountPaid = student.sumPayments();      // Total amount paid by the student

    // Approve the plan if the student has paid at least 50% of what is owed
    return amountPaid >= 0.5 * amountOwed;
}

  
}
