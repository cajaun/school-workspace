import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("input06.txt"));


        SmartHome sh = new SmartHome();
        String mode= "SMARTHOME";

        String[] primingInput = bufferedReader.readLine().replaceAll("\\s+$","").split(" ");
        int t = Integer.parseInt(primingInput[0]);
        for(int i=0;i<t;i++) {
            try {
                String inLine = bufferedReader.readLine().replaceAll("\\s+$","");
                String[] inputLine= inLine.split(" ");
                int itemId = sh.addThing(inputLine);
                mode = inputLine[0];
                String actionCount = bufferedReader.readLine();
                int numActions = Integer.parseInt(actionCount);
                for (int j=0; j<numActions;j++)
                {
                    String actionItem[] = bufferedReader.readLine().replaceAll("\\s+$","").split(" ");
                    {
                        if (actionItem[0].equals("Insert"))
                        {
                            int actionval = Integer.parseInt(actionItem[1]);
                            ((Refrigerator)sh.things[itemId]).insertItem(actionval);
                        }
                        if (actionItem[0].equals("Remove"))
                        {
                            int actionval = Integer.parseInt(actionItem[1]);
                            ((Refrigerator)sh.things[itemId]).removeItem(actionval);
                        }
                    }
                    {              
                        if (actionItem[0].equals("lock"))
                        {
                            ((SmartPhone)sh.things[itemId]).lock();
                        }
                        if (actionItem[0].equals("unlock"))
                        {
                            String pw = actionItem[1];
                            ((SmartPhone)sh.things[itemId]).unlock(pw);
                        }                    
                        if (actionItem[0].equals("setpassword"))
                        {
                            String oldpw = actionItem[1];
                            String newpw = actionItem[2];
                            ((SmartPhone)sh.things[itemId]).setPassword(oldpw,newpw);

                        }
                    }
                    {
                        if (actionItem[0].equals("turnOn"))
                        {
                            ((LightBulb)sh.things[itemId]).turnOn();

                        }
                        if (actionItem[0].equals("turnOff"))
                        {
                            ((LightBulb)sh.things[itemId]).turnOff();

                        }
                        if (actionItem[0].equals("showpower"))
                        {
                            sh.showItemPower(itemId);

                        }

                    }


                }

            }
            catch (IOException ex) {
                throw new RuntimeException(ex);
            }



        }
        String finalMode = bufferedReader.readLine();
        if (finalMode.length()>0)
        {
            String actionCount = bufferedReader.readLine();
            int numActions = Integer.parseInt(actionCount);
            for (int j=0; j<numActions;j++)
            {
                String actionItem[] = bufferedReader.readLine().replaceAll("\\s+$","").split(" ");
                //System.out.println(actionItem[1]);
                if (actionItem[0].equals("showAllPower"))
                {

                    sh.showAllPower();
                }
                if (actionItem[0].equals("showAllThings"))
                {
                    sh.showAllThings();     
                }
            }
        }
    }
}