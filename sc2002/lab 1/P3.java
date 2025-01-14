import java.util.Scanner;

public class P3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Start: ");
        int start = sc.nextInt();
        System.out.print("End: ");
        int end = sc.nextInt();
        System.out.print("Increment: ");
        int increment = sc.nextInt();

        if (end < start) {
            System.out.println("Invalid input");
            return;
        }

        // For loop implementation
        System.out.printf("%-10s %10s", "US$", "S$");
        System.out.println("\n---------------------");
        for (int i = start; i <= end; i += increment) {
            double sgd = i * 1.82;
            System.out.printf("\n%-10d %10.2f", i, sgd);
        }

        // While loop implementation
        System.out.printf("\n \n%-10s %10s", "US$", "S$");
        System.out.println("\n---------------------");
        int i2 = start;
        while (i2 <= end) {
            double sgd = i2 * 1.82;
            System.out.printf("\n%-10d %10.2f", i2, sgd);
            i2 += increment;
        }

        // Do While loop implementation
        System.out.printf("\n \n%-10s %10s", "US$", "S$");
        System.out.println("\n---------------------");
        int i3 = start;
        do {
            double sgd = i3 * 1.82;
            System.out.printf("\n%-10d %10.2f", i3, sgd);
            i3 += increment;
        }
        while (i3 <= end);
    }
}
