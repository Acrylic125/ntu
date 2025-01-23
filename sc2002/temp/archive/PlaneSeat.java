package lab;

public class PlaneSeat {
    private int seatId;
    private boolean assigned;
    private int customerId;

    public PlaneSeat(int seat_id) {
        this.seatId = seat_id;
    }

    public int getSeatId() {
        return seatId;
    }

    public int getCustomerId() {
        return customerId;
    }

    public boolean isOccupied() {
        return assigned;
    }

    public void assign(int customerId) {
        this.customerId = customerId;
        this.assigned = true;
    }

    public void unAssign() {
        this.assigned = false;
    }

}

