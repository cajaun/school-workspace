package Java.COMP1161.week10.hackerrank;
 import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JCheckBox;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.BorderLayout;
import javax.swing.JFileChooser;
import javax.swing.ImageIcon;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.awt.Color;
import java.io.File;
import java.io.IOException;
import javax.swing.JButton;

import com.sun.speech.freetts.Voice; 
import com.sun.speech.freetts.VoiceManager; 

public class SampleApp extends JPanel {
    private JButton     cmdSelectFile;
    private JButton     cmdClose;
    private JPanel      pnlCommand;
    private JPanel      pnlFileName;
    private JLabel      lblFileName;

    private JLabel      lblImg;
    private JPanel      pnlDisplay;
    private JPanel      pnlSpeak;
    private JCheckBox chkSpeak;
    private SampleApp thisForm;
    private ImageIcon image;
    static private JFrame frame;
    private static boolean initComplete = false;
    public SampleApp() {
        super(new GridLayout(2,1));
        thisForm = this;

        pnlCommand = new JPanel();
        pnlDisplay = new JPanel();
        pnlFileName = new JPanel();

        pnlSpeak = new JPanel();

        pnlDisplay.setLayout(new GridLayout(2,1));

        cmdSelectFile  = new JButton("Select Picture File");
        cmdClose   = new JButton("Close");
        chkSpeak  = new JCheckBox("Voice Mode:SPEAKING");
        chkSpeak.setSelected(true);
        lblFileName = new JLabel("startPic.png");
        System.out.println("Selectedfile: " + lblFileName.getText());

        pnlDisplay.removeAll();
        image = new ImageIcon(lblFileName.getText());
        lblImg = new JLabel("", image, JLabel.CENTER);
        
        pnlDisplay.add( lblImg);
       // pnlDisplay.setPreferredSize(new Dimension(650,700));
        //pnlFileName.setPreferredSize(new Dimension(650,50));
        //pnlCommand.setPreferredSize(new Dimension(650,100));
        //pnlSpeak.setPreferredSize(new Dimension(650,50));

        pnlFileName.add(lblFileName);
        pnlCommand.add(cmdSelectFile);
        pnlCommand.add(cmdClose);
        pnlCommand.add(chkSpeak);

        pnlDisplay.add(pnlCommand);
        //pnlDisplay.add(pnlSpeak);
        add(pnlDisplay);
        //add(pnlFileName);

        cmdSelectFile.addActionListener(new FileSelectButtonListener());
        cmdClose.addActionListener(new CloseButtonListener());
        chkSpeak.addItemListener(new ChkListener());

        frame.pack();

    }

    private static void createAndShowGUI() {
        //Create and set up the window.
        frame = new JFrame("Sample app... Click the Voice Mode checkbox to hear me!!!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Create and set up the content pane.
        SampleApp newContentPane = new SampleApp();
        newContentPane.setOpaque(true); //content panes must be opaque
        frame.setContentPane(newContentPane);
        frame.pack();
        frame.setVisible(true);

        //Display the window.

    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.

        javax.swing.SwingUtilities.invokeLater(new Runnable() {
                public void run() {
                    createAndShowGUI();
                    System.setProperty("mbrola.base", ".//mbrola");
                    System.setProperty("freetts.voices", "com.sun.speech.freetts.en.us.cmu_us_kal.KevinVoiceDirectory");

                    initComplete = true;
                    //you can remove the lines below after completing the  ADT
                    System.out.println("Welcome to the Sample Demo. Please select a file, or click the close button.");
                    //say("Welcome to the Sample Demo. Please select a file, or click the close button.");

                }
            });
    }

    private static void say(String announcementMessage) {
        VoiceManager voiceManager = VoiceManager.getInstance();//.getVoice("kevin16");

        //VoiceManager voiceManager = VoiceManager.getInstance();
        //Voice helloVoice = voiceManager.getVoice("mbrola_us1");
        Voice voice = voiceManager.getVoice("kevin16");
        voice.allocate();
        voice.setRate(150);//Setting the rate of the voice
        voice.setPitch(120);//Setting the Pitch of the voice
        voice.setVolume(3);//Setting the volume of the voice
        voice.speak(announcementMessage);
        voice.deallocate();
    }

    private class FileSelectButtonListener implements ActionListener
    {
        public void actionPerformed(ActionEvent e)
        {
            String fname ="";
            JFileChooser fileChooser = new JFileChooser();

            fileChooser.setCurrentDirectory(new File(System.getProperty("user.home")));
            int result = fileChooser.showOpenDialog(thisForm);
            if (result == JFileChooser.APPROVE_OPTION) {
                File selectedFile = fileChooser.getSelectedFile();
                lblFileName.setText(selectedFile.getAbsolutePath());
                String [] fnameParts = lblFileName.getText().split("/");
                fname= selectedFile.getName();
                if (chkSpeak.isSelected())
                    say ("Looking at "+fname);
                System.out.println("Selected file: " + selectedFile.getAbsolutePath());

                pnlDisplay.removeAll();
                image = new ImageIcon(selectedFile.getAbsolutePath());
                lblImg = new JLabel("", image, JLabel.CENTER);
                pnlDisplay.add( lblImg );
                pnlDisplay.add(pnlCommand);
                

            }
            frame.pack();
        }

    }

    private class CloseButtonListener implements ActionListener
    {
        public void actionPerformed(ActionEvent e)
        {
            System.exit(0);
        }

    }

    private class ChkListener implements ItemListener
    {
        public void itemStateChanged(ItemEvent e)
        {
            if (chkSpeak.isSelected())
            {
                say("Voice mode turned on...");
                chkSpeak.setText("Voice Mode:SPEAKING");
            }
            else
            {
                say("Keeping quiet...");

                chkSpeak.setText("Voice Mode:QUIET!!!");
            }

        }

    }

}