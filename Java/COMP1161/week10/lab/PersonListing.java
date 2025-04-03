package Java.COMP1161.week10.lab;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;
import javax.swing.JButton;
import javax.swing.table.*;
import javax.swing.table.DefaultTableModel;
import java.util.Comparator;
import java.util.Collections;
import java.awt.Color;

public class PersonListing extends JPanel {
    private JButton cmdAddPerson;
    private JButton cmdClose;
    private JButton cmdSortAge;
    private JButton cmdSortFirstName;

    private JPanel pnlCommand;
    private JPanel pnlDisplay;
    private ArrayList<Person> plist;
    private PersonListing thisForm;
    private JScrollPane scrollPane;

    private JTable table;
    private DefaultTableModel model;

    public PersonListing() {
        super(new GridLayout(2, 1));
        thisForm = this;

        pnlCommand = new JPanel();
        pnlDisplay = new JPanel();

        plist = loadPersons("person.data");
        String[] columnNames = { "First Name",
                "Last Name",
                "Age",
                "Will Publish" };
        model = new DefaultTableModel(columnNames, 0);
        table = new JTable(model);
        showTable(plist);

        table.setPreferredScrollableViewportSize(new Dimension(500, plist.size() * 15 + 50));
        table.setFillsViewportHeight(true);

        scrollPane = new JScrollPane(table);

        add(scrollPane);

        cmdAddPerson = new JButton("Add Person");

        // cmdAddPerson.setBackground(Color.CYAN);
        // change the color of the buttosn for the last question I guess

        cmdSortAge = new JButton("Sort by Age");
        cmdSortFirstName = new JButton("Sort by First Name");
        cmdClose = new JButton("Close");

        cmdClose.addActionListener(new CloseButtonListener());
        cmdAddPerson.addActionListener(e -> new PersonEntry(this));

        cmdSortAge.addActionListener(e -> {
            Collections.sort(plist, Comparator.comparingInt(Person::getAge));
            refreshTable();
        });

        cmdSortFirstName.addActionListener(e -> {
            Collections.sort(plist, Comparator.comparing(p -> p.getName().split(" ")[0]));
            refreshTable();
        });

        pnlCommand.add(cmdAddPerson);
        pnlCommand.add(cmdSortAge);
        pnlCommand.add(cmdSortFirstName);
        pnlCommand.add(cmdClose);

        add(pnlCommand);
    }

    private void showTable(ArrayList<Person> plist) {
        for (Person p : plist) {
            addToTable(p);
        }
    }

    private void refreshTable() {
        model.setRowCount(0);
        showTable(plist);
    }

    private void addToTable(Person p) {
        String[] name = p.getName().split(" ");
        String[] item = { name[0], name[1], "" + p.getAge(), "" + p.getPublish() };
        model.addRow(item);

    }

    private static void createAndShowGUI() {

        JFrame frame = new JFrame("List of persons who are requesting a vaccine");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        PersonListing newContentPane = new PersonListing();
        newContentPane.setOpaque(true);
        frame.setContentPane(newContentPane);

        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) {

        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }

    public void addPerson(Person p) {
        plist.add(p);
        addToTable(p);

    }

    private ArrayList<Person> loadPersons(String pfile) {
        Scanner pscan = null;
        ArrayList<Person> plist = new ArrayList<Person>();
        try {
            pscan = new Scanner(new File(pfile));
            while (pscan.hasNext()) {
                String[] nextLine = pscan.nextLine().split(" ");
                String name = nextLine[0] + " " + nextLine[1];
                int age = Integer.parseInt(nextLine[2]);
                boolean publish = false;
                if (nextLine[3].equals("0"))
                    publish = false;
                else
                    publish = true;
                Person p = new Person(name, age, publish);
                plist.add(p);
            }

            pscan.close();
        } catch (IOException e) {
        }
        return plist;
    }

    private class CloseButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.exit(0);
        }

    }

}