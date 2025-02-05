import java.util.Scanner;

class Main {

    public static void bubble(int[] arr, int n) {
        for (int i = n-2; i > -1; i--) {
           for (int j = 0; j < i + 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int jEle = arr[j];
                    int jP1Ele = arr[j + 1];
                    arr[j + 1] = jEle;
                    arr[j] = jP1Ele;
                } 
           } 
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements to be sorted: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Number: ");
            arr[i] = sc.nextInt();
        }

        bubble(arr, n);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]); 
        }

    }
}
