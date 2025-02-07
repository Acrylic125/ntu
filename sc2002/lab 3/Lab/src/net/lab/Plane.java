package com.lab;

import java.util.Arrays;

public class Plane {
    private PlaneSeat[] seat;
    private int numEmptySeat;

    public Plane() {
        this.seat = new PlaneSeat[12];
        for (int i = 0; i < seat.length; i++) {
            seat[i] = new PlaneSeat(i + 1);
        }
        numEmptySeat = seat.length;
    }

    public PlaneSeat[] sortSeats() {
        PlaneSeat[] sortedSeats = Arrays.copyOf(seat, seat.length);
        Arrays.sort(sortedSeats, (PlaneSeat a, PlaneSeat b) -> {
            return a.getCustomerID() - b.getCustomerID();
        });
        return sortedSeats;
    }

    private PlaneSeat[] sortSeatsByID() {
        PlaneSeat[] sortedSeats = Arrays.copyOf(seat, seat.length);
        Arrays.sort(sortedSeats, (PlaneSeat a, PlaneSeat b) -> {
            return a.getSeatID() - b.getSeatID();
        });
        return sortedSeats;
    }

    public void showNumEmptySeats() {
        System.out.println("Number of empty seats: " + numEmptySeat);
    }

    public void showEmptySeats() {
        System.out.println("The following seats are empty: ");
        for (int i = 0; i < seat.length; i++) {
            PlaneSeat _seat = seat[i];
            if (!_seat.isOccupied()) {
                System.out.println("SeatID " + _seat.getSeatID());
            }
        }
    }

    public void showAssignedSeats(boolean bySeatId) {
        System.out.println("The seat assignments are as follow: ");
        PlaneSeat[] sortedSeats = bySeatId ? sortSeatsByID() : sortSeats();
        for (int i = 0; i < sortedSeats.length; i++) {
            PlaneSeat _seat = sortedSeats[i];
            if (_seat.isOccupied()) {
                System.out.println("SeatID " + _seat.getSeatID() + " assigned to CustomerID " + _seat.getCustomerID() + ". ");
            }
        }
    }

    public void assignSeat(int seatId, int cust_id) {
        PlaneSeat foundSeat = null;
        for (int i = 0; i < seat.length; i++) {
            PlaneSeat _seat = seat[i];

            if (_seat.getSeatID() == seatId) {
                foundSeat = _seat;
                break;
            }
        }

        if (foundSeat == null) {
            System.out.println("Seat does not exist. ");
            return;
        }

        if (foundSeat.isOccupied()) {
            System.out.println("Seat already assigned to a customer. ");
            return;
        }

        foundSeat.assign(cust_id);
        numEmptySeat--;
        System.out.println("Seat Assigned! ");
    }

    public void unAssignSeat(int seatId) {
        PlaneSeat foundSeat = null;
        for (int i = 0; i < seat.length; i++) {
            PlaneSeat _seat = seat[i];

            if (_seat.getSeatID() == seatId) {
                foundSeat = _seat;
                break;
            }
        }

        if (foundSeat == null) {
            System.out.println("Seat does not exist. ");
            return;
        }

        if (!foundSeat.isOccupied()) {
            System.out.println("Seat is already empty. ");
            return;
        }

        foundSeat.unAssign();
        numEmptySeat++;
        System.out.println("Seat Unassigned! ");
    }


}
