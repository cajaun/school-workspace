class ApprovalRequest {
    private Trip trip;
    private Bus bus;
    private int id;
    private static int nextid = 0;
    private String comment;

    public ApprovalRequest(Trip trip, Bus bus) {
        this.trip = trip;
        this.bus = bus;
        id = nextid;
        nextid++;
    }

    public int getId() {
        return id;
    }

    public Trip getTrip() {
        return trip;
    }

    public Bus getBus() {
        return bus;
    }

    public void setComment(String info) {
        this.comment = info + ":" + trip.toString();
    }

    public String toString() {
        return comment;
    }
}
