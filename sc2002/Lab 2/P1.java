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

            int a, b;
            long n;
            switch (choice) {
                case 1:
                    mulTest();
                    break;
                case 2:
                    System.out.println("a / b");
                    System.out.print("a: ");
                    a = sc.nextInt();
                    System.out.print("b: ");
                    b = sc.nextInt();
                    divide(a, b);

                    // divide(4, 7);
                    // divide(7, 7);
                    // divide(25, 7);
                    break;
                case 3:
                    System.out.println("a % b");
                    System.out.print("a: ");
                    a = sc.nextInt();
                    System.out.print("b: ");
                    b = sc.nextInt();
                    modulus(a, b);
                    // modulus(4, 7);
                    // modulus(7, 7);
                    // modulus(25, 7);
                    break;
                case 4:
                    System.out.println("Count digits of a");
                    System.out.print("a: ");
                    a = sc.nextInt();

                    countDigits(a);
                    break;
                case 5:
                    System.out.println("Position of digit digit in n");
                    System.out.print("n: ");
                    a = sc.nextInt();
                    System.out.print("digit: ");
                    b = sc.nextInt();

                    position(a, b);
                    break;
                case 6:
                    System.out.println("Odd digits in n");
                    System.out.print("n: ");
                    n = sc.nextLong();

                    extractOddDigits(n);
                    break;
                case 7:
                    System.out.println("Program terminating...");
            }
        } while (choice < 7);
        sc.close();
    }

    public static void mulTest() {
        Scanner sc = new Scanner(System.in);
        int correct = 0;
        int qns = 5;
        for (int i = 1; i <= qns; i++) {
            int a = (int) (Math.random() * 10); // Round down, does not include 10.    
            int b = (int) (Math.random() * 10); // Round down, does not include 10.    
            System.out.println("Q" + i + ": What is " + a + " * " + b + "? ");
            if (sc.hasNextInt()) {
                int ans = sc.nextInt();
                if (ans == (a * b)) {
                    correct++;
                }
            }
        }
        System.out.println(correct + " / " + qns + " were right.");
    }

    public static void divide(int a, int b) {
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
        System.out.println(a + " / " + b + " = " + quotient);
    }

    public static void modulus(int a, int b) {
        if (b == 0) {
            System.out.println("Division by zero is not allowed!");
            return;
        }
        if (a < 0 || b < 0) {
            System.out.println("a and b must be positive.");
            return;
        }
        
        int remainder = a;
        while (remainder >= b) {
            remainder -= b;
        }
        System.out.println(a + " % " + b + " = " + remainder);
    }

    public static void countDigits(int a) {
        int count = 0;
        do {
            a = a / 10; // int truncates.
            count++;
        }
        while (a > 0);

        System.out.println("Total digits of a: " + count);
    }

    public static void position(int n, int digit) {
        char digitChar = (char) (digit + '0');
        String nStr = n + "";

        String posStr = "";
        for (int i = 0; i < nStr.length(); i++) {
            char charAtI = nStr.charAt(i);

            if (charAtI < '0' || charAtI > '9') {
                System.out.println("Invalid b value. b must be a number.");
                return;
            }
            
            if (charAtI == digitChar) {
                if (posStr == "") {
                    posStr = i + "";
                } else {
                    posStr += ", " + i;
                }
            }
        }

        System.out.println("Positions of " + digit +" in " + n + ": " + posStr);
    }

    public static void extractOddDigits(long n) {
        String nStr = n + "";

        String posStr = "";
        for (int i = 0; i < nStr.length(); i++) {
            char charAtI = nStr.charAt(i);

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

        System.out.println("Odd digits of " + n +": " + posStr);
    }

}
