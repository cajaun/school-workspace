package Java.COMP1161.week3.lab;



class Song {

    private String title, genre;
    Singer singer;
    private Studio studio;

    public Song(String title, String genre, Singer singer) {

        this.studio = null;
        this.genre = genre;
        this.singer = singer;
        this.title = title;

    }


    public int getEstEarnings() {

        int titleLength = title.length();
        int songPartEst = singer.getMinistry().getSongPartEst();
        return titleLength * songPartEst;
    }

    public int getClaimableEarnings() {
        int est = getEstEarnings();
        if (est > singer.getMinistry().getMinClaimable())
            return est;
        else
            return 0;
    }

    public String getTitle() {
        return title;
    }

    /* Q4A. you will implement setStudio somewhere around here */
    public void setStudio(Studio studio) {
        this.studio = studio;
    }

    public Studio getStudio() {
        return studio;
    }

  

    private boolean isBestSeller() {
        return getEstEarnings() > singer.getMinistry().getBestSellLimit();
    }

    public boolean hasStudio() {
        return (!(studio == null));
    }

    public String toString() {
        String outval = "Released ";
        if (isBestSeller())
            outval += "**";
        int cost = 0;
        if (!(studio == null))
            cost = studio.getCost();
        outval += title + " as a " + genre + " single to earn $" + String.format("%,d", getEstEarnings()) + ".";

        return outval;
    }
}