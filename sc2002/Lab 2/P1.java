import java.util.Scanner;

public class P1 {
    public static void main(String[] args) {
        int choice;
        Scanner sc = new Scanner(System.in);

        do {
            System.out.println("Perform the following methods:");
            System.out.println("1: miltiplication test");
            System.out.println("2: quotient using division by subtraction");
            System.out.println("3: remainder using division by subtraction");
            System.out.println("4: count the number of digits");
            System.out.println("5: position of a digit");
            System.out.println("6: extract all odd digits");
            System.out.println("7: quit");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    mulTest();
                    break;
                case 2:
                    divide();
                    break;
                case 3:
                    modulus();
                    break;
                case 4:
                    countDigits();
                    break;
                case 5:
                    position();
                    break;
                case 6:
                    extractOddDigits();
                    break;
                case 7:
                    System.out.println("Program terminating...");
            }
        } while (choice < 7);
    }

    public static void mulTest() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Test a * b");
        System.out.print("a: ");
        double a = sc.nextDouble();
        System.out.print("b: ");
        double b = sc.nextDouble();
        System.out.println("a * b = " + (a * b));
    }

    public static void divide() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Test division (quotient) a / b");
        System.out.print("a: ");
        double a = sc.nextDouble();
        System.out.print("b: ");
        double b = sc.nextDouble();
        if (b == 0) {
            System.out.println("Division by zero is not allowed!");
            return;
        }
        if (a < 0 || b < 0) {
            System.out.println("a and b must be positive.");
            return;
        }
        
        int quotient = 0;
        while (a >= b) {
            a -= b;
            quotient++;
        }
        System.out.println("a / b (quotient) = " + quotient);
    }

    public static void modulus() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Test division (remainder) a % b");
        System.out.print("a: ");
        double a = sc.nextDouble();
        System.out.print("b: ");
        double b = sc.nextDouble();
        if (b == 0) {
            System.out.println("Division by zero is not allowed!");
            return;
        }
        if (a < 0 || b < 0) {
            System.out.println("a and b must be positive.");
            return;
        }
        
        while (a >= b) {
            a -= b;
        }
        System.out.println("a % b = " + a);
    }

    public static void countDigits() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Count digits of a");
        System.out.print("a: ");
        int a = sc.nextInt();

        int count = 0;
        do {
            a = a / 10; // int truncates.
            count++;
        }
        while (a > 0);

        System.out.println("Total digits of a: " + count);
    }

    public static void position() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Position of digit a in b");
        System.out.print("a: ");
        int a = sc.nextInt();
        System.out.print("b: ");
        String bStr = sc.next();

        char aChar = (char) (a + '0');

        String posStr = "";
        for (int i = 0; i < bStr.length(); i++) {
            char charAtI = bStr.charAt(i);

            if (charAtI < '0' || charAtI > '9') {
                System.out.println("Invalid b value. b must be a number.");
                return;
            }
            
            if (charAtI == aChar) {
                if (posStr == "") {
                    posStr = i + "";
                } else {
                    posStr += ", " + i;
                }
            }
        }

        System.out.println("Positions of a in b: " + posStr);
    }

    public static void extractOddDigits() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Odd digits of a");
        System.out.print("a: ");
        String aStr = sc.next();

        String posStr = "";
        for (int i = 0; i < aStr.length(); i++) {
            char charAtI = aStr.charAt(i);

            if (charAtI < '0' || charAtI > '9') {
                System.out.println("Invalid b value. b must be a number.");
                return;
            }
            
            if (charAtI == '1' || charAtI == '3' || charAtI == '5' || charAtI == '7' || charAtI == '9') {
                if (posStr == "") {
                    posStr = i + "";
                } else {
                    posStr += ", " + i;
                }
            }
        }

        System.out.println("Odd digits of a: " + posStr);
    }

}
