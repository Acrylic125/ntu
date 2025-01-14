import java.util.Scanner;

public class P4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int height = sc.nextInt();
        if (height <= 0) {
            System.out.println("Invalid input.");
            return;
        }

        for (int i = 1; i <= height; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(j % 2 == 0 ? "AA" : "BB"); 
            }
            System.out.print("\n");
        }
    }
}
