package com.lab;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Plane plane = new Plane();

        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("Seat Management System");
            System.out.println("(1) Show number of empty seats");
            System.out.println("(2) Show the list of empty seats");
            System.out.println("(3) Show the list of seat assignments by seat ID");
            System.out.println("(4) Show the list of seat assignments by customer ID");
            System.out.println("(5) Assign a customer to a seat");
            System.out.println("(6) Remove a seat assignment");
            System.out.println("(7) Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            int seatId, customerId;
            switch (choice) {
                case 1:
                    plane.showNumEmptySeats();
                    break;
                case 2:
                    plane.showEmptySeats();
                    break;
                case 3:
                    plane.showAssignedSeats(true);
                    break;
                case 4:
                    plane.showAssignedSeats(false);
                    break;
                case 5:
                    System.out.println("Assigning Seat ..");
                    System.out.println(" Please enter SeatID: ");
                    seatId = scanner.nextInt();
                    System.out.println(" Please enter Customer ID: ");
                    customerId = scanner.nextInt();
                    plane.assignSeat(seatId, customerId);
                    break;
                case 6:
                    System.out.println("Enter SeatID to unassign customer from: ");
                    seatId = scanner.nextInt();
                    plane.unAssignSeat(seatId);
                    break;
                case 7:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 7.");
            }
        } while (choice != 7);

        scanner.close();
    }
}
