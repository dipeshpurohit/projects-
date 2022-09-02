package com.mkyong.date;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.BorderLayout;
import java.awt.Font;

public class CountryTime {

    public static void main(String args[]) {
        JFrame frame = new JFrame("conunties time zone and date");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        String[] OptionTochoose = { "Kolkata", "Chicago", "London", "Singapore" };
        JComboBox<String> C1 = new JComboBox<>(OptionTochoose);
        C1.setBounds(200, 300, 100, 50);

        // creating label to display time
        JLabel L1 = new JLabel("", SwingConstants.CENTER);
        L1.setBounds(20, 100, 500, 100);
        L1.setFont(new Font("Calibri", Font.BOLD, 35));

        frame.getContentPane().add(L1, BorderLayout.CENTER);
        frame.add(C1);

        frame.setSize(500, 500);
        frame.setLayout(null);
        frame.setVisible(true);

        C1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy hh:mm:ss a");
                LocalDateTime now = LocalDateTime.now();
                Instant nowUtc = Instant.now();

                if (C1.getSelectedItem().toString() == "London") {
                    String dateInString = now.format(formatter);
                    L1.setText(dateInString);
                } else if (C1.getSelectedItem().toString() == "Kolkata") {
                    ZoneId IndiaZoneId = ZoneId.of("Asia/Kolkata");
                    ZonedDateTime asiaZonedDateTime = ZonedDateTime.ofInstant(nowUtc, IndiaZoneId);
                    String dateinstring = asiaZonedDateTime.format(formatter);
                    L1.setText(dateinstring);

                } else if (C1.getSelectedItem().toString() == "Chicago") {
                    ZoneId newyorkZoneId = ZoneId.of("America/Chicago");
                    ZonedDateTime newyorkZonedDateTime = ZonedDateTime.ofInstant(nowUtc, newyorkZoneId);
                    String dateinstring = newyorkZonedDateTime.format(formatter);
                    L1.setText(dateinstring);

                } else if (C1.getSelectedItem().toString() == "Singapore") {
                    ZoneId singaporeZoneId = ZoneId.of("Asia/Singapore");
                    ZonedDateTime asiaZonedDateTime = ZonedDateTime.ofInstant(nowUtc, singaporeZoneId);
                    String dateInString = asiaZonedDateTime.format(formatter);
                    L1.setText(dateInString);

                }

            }
        });

    }

}
