class Assignment {

  private int effort;
  private int resources;
  private int difficulty;
  private double expectedScore;

  public Assignment(int effort, int resources, int difficulty) {
    this.effort = effort;
    this.resources = resources;
    this.difficulty = difficulty;
    this.expectedScore = evaluatedExpectedScore();

  }

  private double evaluatedExpectedScore() {
    double pi = Math.PI; 
    
    return  0.1 * (effort * difficulty) + Math.pow(resources * effort, 2) / (pi * Math.sqrt(difficulty));
    
   
  }

  public int getEffort() {
    return effort;
  }

  public int getNumResources() {
    return resources;
  }

  public int getDifficulty() {
    return difficulty;
  }

  public double getExpectedScore() {
    return expectedScore;
  }

}