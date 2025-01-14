import java.util.Scanner;

public class P1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char action = sc.next().charAt(0);

        switch (action) {
            case 'A':
            case 'a':
                System.out.println("Action movie fan");
                break;
            case 'C':
            case 'c':
                System.out.println("Comedy movie fan");
                break;
            case 'D':
            case 'd':
                System.out.println("Drama movie fan");
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
