import java.util.Scanner;

public class MyFirstProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char action = sc.next().charAt(0);
        System.out.println("You entered: " + action);


        System.out.println("Hello! This is my first program.");
        System.out.println("Bye Bye!");
    }
}
