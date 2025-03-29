
//import java.io.*;
//import java.nio.file.*;
import java.util.zip.*;

import java.util.Scanner;
import java.util.Collections;
import java.util.stream.Stream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;

public class Tester{
    private static double jdocScore =0;
    private static boolean bfound, pbfound, tbfound, sbfound;
    private int caseNo;
    private static boolean invalidCase = false;

    //private static double [] caseScores={2,3, 20,5,5,5,5,15,15, 20, 5};
    private static double [] caseScores={2, 3, 20, 5, 5, 5, 5, 15,15,20,5};

    public Tester(int caseNo)
    {
        this.caseNo= caseNo;
    }

    public int getCaseNo()
    {
        return caseNo;

    }

    public String getPlanInFile()
    {
        return "./cases/Plan."+caseNo+".txt";

    }

    public String getBusInFile()
    {
        return "./cases/Bus."+caseNo+".txt";

    }

    public String getTripInFile()
    {
        return "./cases/Trip."+caseNo+".txt";

    }

    public String getTestOutFile()
    {
        return "./cases/TestCase"+caseNo+".myOutput.txt";
    }

    public double score()
    {
        String testfile = "./cases/TestCase"+caseNo+".myOutput.txt";
        String valfile = "./cases/output"+caseNo+".txt";
        String tString="", vString=""; 
        try{
            Scanner tscan = new Scanner(new File(testfile));
            while (tscan.hasNext())
                tString +=tscan.nextLine();
        }
        catch(IOException ioe)
        {}
        try{
            Scanner vscan = new Scanner(new File(valfile));
            while (vscan.hasNext())
                vString +=vscan.nextLine();
        }
        catch(IOException ioe)
        {}
        //System.out.println("Comparing ["+tString+"]");
        //System.out.println(" with ["+vString+"]");

        double sc = 0;
        try{
            sc = caseScores[getCaseNo()]*similarity(tString.substring(1), vString.substring(1));
        }
        catch (StringIndexOutOfBoundsException sib){
            System.out.println("Please make sure you save cases before running tests");
        }
        return  sc; 

    }

    public static double similarity(String s1, String s2) {
        String longer = s1, shorter = s2;
        if (s1.length() < s2.length()) { // longer should always have greater length
            longer = s2; shorter = s1;
        }
        int longerLength = longer.length();
        if (longerLength == 0) { return 1.0; /* both strings are zero length */ }
        /* // If you have Apache Commons Text, you can use it to calculate the edit distance:
        LevenshteinDistance levenshteinDistance = new LevenshteinDistance();
        return (longerLength - levenshteinDistance.apply(longer, shorter)) / (double) longerLength; */
        return (longerLength - editDistance(longer, shorter)) / (double) longerLength;

    }

    // Example implementation of the Levenshtein Edit Distance
    // See http://rosettacode.org/wiki/Levenshtein_distance#Java
    public static int editDistance(String s1, String s2) {
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();
        int startpos=0;

        int[] costs = new int[s2.length() + 1];
        for (int i = startpos; i <= s1.length(); i++) {
            int lastValue = i;
            for (int j = startpos; j <= s2.length(); j++) {
                if (i == startpos)
                    costs[j] = j;
                else {
                    if (j > startpos) {
                        int newValue = costs[j - 1];
                        if (s1.charAt(i - 1) != s2.charAt(j - 1))
                            newValue = Math.min(Math.min(newValue, lastValue),
                                costs[j]) + 1;
                        costs[j - 1] = lastValue;
                        lastValue = newValue;
                    }
                }
            }
            if (i > startpos)
                costs[s2.length()] = lastValue;
        }
        return costs[s2.length()];
    }

    public static void runCases(WorkArea work, SystemInfo sys)
    {
        boolean header = false;
        ArrayList<Integer> manualTests=new ArrayList<Integer>();
        manualTests.add(0);
        manualTests.add(1);
        manualTests.add(7);
        manualTests.add(8);
        manualTests.add(9);
        manualTests.add(10);
        String stuId ="";
        try
        {
            Scanner sc = new Scanner(new File("id.txt"));
            stuId = sc.nextLine();
            sc.close();
        }
        catch (IOException ioe){}
        if (stuId.length()==0)
        {
            System.out.println("ID not set. Please enter your ID before proceeding.");
            return;
        }
        ArrayList<Tester> tests = new ArrayList<Tester>();
        invalidCase = false;

        for (int i=0; i< caseScores.length-1;i++)
        {
            Tester t = new Tester(i);
            work.clearData();
            work.loadData(i);
            if (i<7)
                if (!(validated(i)))
                {
                    invalidCase=true;
                    System.out.println("Test case "+i+ " is broken:: Please refresh it before running tests");
                    break;
                } 
               
            //tc.writeOut(vx.getPlist(),vx.getAPlist(),vx.getFVlist(),
            //    vx.getInitApproved(), outWriter);
            tests.add(t);
            int nonPrintable= getNonPrint(stuId);
            if (manualTests.indexOf(i)<0)
            {
                try{
                    PrintStream outStream = new PrintStream(new FileOutputStream(t.getTestOutFile()));
                    outStream.write(nonPrintable);
                    switch(i)
                    {case 0:

                        case 1:{
                                ReportScreen r = new ReportScreen();
                                r.listPlanners(work.planners, outStream);
                                break;
                            }

                        case 2:
                        case 3:
                        case 4:
                        case 5:
                        case 6:
                            {
                                ReportScreen r = new ReportScreen();
                                r.listBuses(work.buses, outStream);
                                break;
                            }

                        case 11:{
                                for(Bus b:work.buses)
                                    b.promoteTrips(outStream);
                                for(Planner p:work.planners)
                                    p.submitPlans();

                            }

                    }
                    outStream.close();
                }
                catch(IOException ioe){} 
            }
        }
        if (!(invalidCase))
        {
            double sumScore =0;
            for (Tester t:tests)
            {   if (t.getCaseNo() !=tests.size())
                {
                    double tcScore = t.score();
                    sumScore +=tcScore;
                    System.out.println( "Test "+t.getCaseNo() +"=>"+tcScore+"/"+caseScores[t.getCaseNo()]+"; Aggregate score is "+sumScore+"/100.0");
                }
            }
            //final case -look for javadocs
            jdocScore = 0;
            bfound=false; pbfound=false; tbfound=false; sbfound=false;
            try (Stream<Path> walkStream = Files.walk(Paths.get((System.getProperty("user.dir"))))) {
                walkStream.filter(p -> p.toFile().isFile()).forEach(f -> {
                        if (f.toString().endsWith("Bus.html")) {
                            bfound = true;;
                        }
                    });
            }
            catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

            try (Stream<Path> walkStream = Files.walk(Paths.get((System.getProperty("user.dir"))))) {
                walkStream.filter(p -> p.toFile().isFile()).forEach(f -> {
                        if (f.toString().endsWith("TrainingBus.html")) {
                            tbfound =true;

                        }
                    });
            }
            catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            try (Stream<Path> walkStream = Files.walk(Paths.get((System.getProperty("user.dir"))))) {
                walkStream.filter(p -> p.toFile().isFile()).forEach(f -> {
                        if (f.toString().endsWith("SportsBus.html")) {
                            sbfound =true;
                        }
                    });
            }
            catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            try (Stream<Path> walkStream = Files.walk(Paths.get((System.getProperty("user.dir"))))) {
                walkStream.filter(p -> p.toFile().isFile()).forEach(f -> {
                        if (f.toString().endsWith("PartyBus.html")) {
                            pbfound=true;
                        }
                    });
            }
            catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            if (bfound) jdocScore+=1.25;
            if (pbfound) jdocScore+=1.25;
            if (sbfound) jdocScore+=1.25;
            if (tbfound) jdocScore+=1.25;
            sumScore+=jdocScore;
            //System.out.println( "Score on test "+(tests.size()-1) +" is "+jdocScore+"; Aggregate score is "+sumScore);
            System.out.println( "Test "+(tests.size())  +"=>"+jdocScore+"/"+caseScores[tests.size()]+"; Aggregate score is "+sumScore+"/100.0");

            double modScore = moderate(sumScore, stuId);
            System.out.println( "==========Moderated Score:"+modScore+"/100.0===========");

            File dir = new File(System.getProperty("user.dir"));
            File[] scoreFiles = dir.listFiles((dir1, name)->name.startsWith("score"));
            for (File file:scoreFiles)
                file.delete();

            try{    
                PrintStream p=new PrintStream(new FileOutputStream("score_"+String.format("%.2f", modScore)+"_"+stuId+".tst"));
                p.write((int)sumScore);
                //p.println(sumScore);
                p.write(getHash(sumScore+""));
                p.write(getHash(stuId));

                p.close();
            }
            catch(IOException ioe){}
            zipFiles("score_"+String.format("%.2f", modScore)+"_"+stuId,sys);

        }
    }

    public   static void saveTest(Scanner scan, WorkArea work) {
        System.out.println("Please enter the number the test that you would like to save [0, 1, 7, 8 or 9]");
        int testNo = Integer.parseInt(scan.next());
        String stuId ="";
        try
        {
            Scanner sc = new Scanner(new File("id.txt"));
            stuId = sc.nextLine();
            sc.close();
        }
        catch (IOException ioe){}
        if (stuId.length()==0)
        {
            System.out.println("ID not set. Please enter your ID before proceeding.");
            return;
        }
        Tester t = new Tester(testNo);
        int outkey=25;
        try{
            PrintStream outStream = new PrintStream(new FileOutputStream(t.getTestOutFile()));
            int nonPrintable= getNonPrint(stuId);
            outStream.write(nonPrintable);

            switch(testNo)

            {
                case 0:
                case 1:
                    {
                        ReportScreen r = new ReportScreen();
                        //Collections.sort(work.planners);
                        r.listPlanners(work.planners, outStream);

                        break;

                    }       

                case 7:    
                case 8:    
                case 9:    
                    {
                        ReportScreen r = new ReportScreen();
                        //Collections.sort(work.buses);
                        r.listBuses(work.buses, outStream);
                        break;
                    }
            }
            outStream.close();
        }
        catch(IOException ioe)
        {}
    }

    private static void zipFiles(String zipname, SystemInfo sys) {
        try {
            File firstFile;
            File[] codeFilePaths, docFilePaths, testFilePaths;

            firstFile = new File(zipname);
            File codedir = new File(sys.getCodeFolder());
            File docdir = new File(sys.getJavaDocFolder());
            File testdir = new File(sys.getTestCaseFolder());

            codeFilePaths= codedir.listFiles((dir1, name)->name.endsWith("java"));
            docFilePaths= docdir.listFiles((dir2, name)->name.endsWith("html"));
            testFilePaths= testdir.listFiles((dir3, name)->name.endsWith("myOutput.txt"));
            System.out.println(sys.getTestCaseFolder());

            String zipFileName = firstFile.getName().concat(".zip");

            FileOutputStream fos = new FileOutputStream(zipFileName);
            ZipOutputStream zos = new ZipOutputStream(fos);

            zos.putNextEntry(new ZipEntry(zipname));

            for (File aFile : codeFilePaths) {

                zos.putNextEntry(new ZipEntry(aFile.getName()));
                System.out.println("Adding "+aFile + " to submission");
                //System.out.println(aFile.getPath()+aFile.getName());
                byte[] bytes = Files.readAllBytes(Paths.get(aFile.getPath()));
                //byte[] bytes = Files.readAllBytes(Paths.get(aFile.getName()));
                zos.write(bytes, 0, bytes.length);
                zos.closeEntry();
            }
            if (!(docFilePaths==null)){
                for (File aFile : docFilePaths) {

                    zos.putNextEntry(new ZipEntry(aFile.getName()));
                    System.out.println("Adding "+aFile + " to submission");
                    //System.out.println(aFile.getPath()+aFile.getName());
                    byte[] bytes = Files.readAllBytes(Paths.get(aFile.getPath()));
                    //byte[] bytes = Files.readAllBytes(Paths.get(aFile.getName()));
                    zos.write(bytes, 0, bytes.length);
                    zos.closeEntry();
                }
            }

            for (File aFile : testFilePaths) {

                zos.putNextEntry(new ZipEntry(aFile.getName()));
                System.out.println("Adding "+aFile + " to submission");
                //System.out.println(aFile.getPath()+aFile.getName());
                byte[] bytes = Files.readAllBytes(Paths.get(aFile.getPath()));
                //byte[] bytes = Files.readAllBytes(Paths.get(aFile.getName()));
                zos.write(bytes, 0, bytes.length);
                zos.closeEntry();
            }

            zos.close();
            System.out.println("============================================");
            System.out.println("===Successfully created submission file ====");
            System.out.println("===as "+zipFileName  +"=============");
            System.out.println("============================================");
            System.out.println("Remember you can submit to OurVLE as many times");
            System.out.println("as you wish before the deadline, so do not delay!!!");

        } catch (FileNotFoundException ex) {
            System.err.println("A file does not exist: " + ex);
        } catch (IOException ex) {
            System.err.println("I/O error: " + ex);
            ex.printStackTrace();

        } catch (Exception ex) {
            System.err.println("Some other exception...: " + ex);
            ex.printStackTrace();
        }
    }

    private static int getNonPrint(String id)
    {
        int retval = 0;
        for (int i=0; i<id.length();i++)
            try
            {
                retval+=i+Integer.parseInt(id.charAt(i)+"");
            }
            catch (NumberFormatException nfe)
            {
                retval+=i;
            }
        retval = retval%15+15;
        return retval;
    }

    private static double moderate(double score, String stuid){
        return score - Double.parseDouble(new String(new StringBuilder(stuid).reverse()))/1000000000*5;

    }

    private static int getHash(String txt)
    {
        int sumval = 20;
        int retval =0;
        for (int i=0; i<txt.length();i++)
            sumval+=((int)txt.charAt(i))%1371;
        retval = sumval%15+15;
        return retval;
    }

    private static String readPlanners(String pfile)
    {
        Scanner pscan = null;
        String plandata="";

        try
        {
            pscan  = new Scanner(new File(pfile));
            while(pscan.hasNext())
                plandata += pscan.nextLine();

            pscan.close();
        }
        catch(IOException e)
        {}

        return plandata;

    }

    private static String readBuses(String bfile)
    {
        Scanner bscan = null;
        String busdata="";

        try
        {
            bscan  = new Scanner(new File(bfile));
            while(bscan.hasNext())
                busdata += bscan.nextLine();

            bscan.close();
        }
        catch(IOException e)
        {}

        return busdata;

    }

    private static String getPlanFile(int caseNo)
    {
        return "cases/Planner."+caseNo+".txt";
    }

    private static String getBusFile(int caseNo)
    {
        return "cases/Bus."+caseNo+".txt";
    }

    
    private static String readData(int caseNo)
    {
        String busdata = readBuses(getBusFile(caseNo));
        String plandata  =  readPlanners(getPlanFile(caseNo));

        return busdata+plandata;    
    }

    private static boolean validated(int i)
    {
        String txt = readData(i);
        int hash = getHash(txt);

        int hashval =0;

        try
        {
            Scanner sc = new Scanner(new File("cases/c"+i+".chk"));
            hashval = Integer.parseInt(sc.nextLine());
            sc.close();
        }
        catch (IOException ioe){}

        return (hash == hashval);

    }
}

