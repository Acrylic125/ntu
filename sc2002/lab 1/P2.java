import java.util.Scanner;

public class P2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Salary: ");
        int salary = sc.nextInt();
        System.out.print("Merit: ");
        int merit = sc.nextInt();

        char grade = ' ';
        if (salary >= 700 && salary <= 899) {
            grade = 'A';
            if (salary <= 799 && merit < 20) {
                grade = 'B';
            }
        } 
        else if (salary >= 600 && salary <= 699) {
            grade = 'B';
            if (salary <= 649 && merit < 10) {
                grade = 'C';
            }
        }
        else if (salary >= 500 && salary <= 599) {
            grade = 'C';
        }

        System.out.println("Grade: " + grade);
    }
}
