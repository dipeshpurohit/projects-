import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class convert {
    public static void Currency() {

        // creating a frame
        JFrame frame = new JFrame("Currency convertor");

        // creating two textfields to show currency
        TextField T1 = new TextField("0");
        T1.setBounds(100, 150, 90, 20);

        // drop down option
        String[] OptionToChoose = { "Rupee", "Euro", "Dollar", "Pounds" };
        JComboBox<String> C1 = new JComboBox<>(OptionToChoose);
        C1.setBounds(100, 100, 90, 20);
        C1.setForeground(Color.BLUE);
        C1.setBackground(Color.lightGray);

        JComboBox<String> C2 = new JComboBox<>(OptionToChoose);
        C2.setBounds(100, 250, 90, 20);
        C2.setForeground(Color.BLUE);
        C2.setBackground(Color.lightGray);

        // button
        JButton B1 = new JButton("convert");
        B1.setBounds(200, 350, 90, 20);

        // displaying objects in frame
        frame.add(C1);
        frame.add(C2);
        frame.add(B1);
        frame.add(T1);

        // displaying frame
        frame.setSize(500, 500);
        frame.setLayout(null);
        frame.setVisible(true);

        B1.addActionListener(new ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Double tot;
                Double amount = Double.parseDouble(T1.getText());
                // coverting dollar to other currency
                if (C1.getSelectedItem().toString() == "Dollar" && C2.getSelectedItem().toString() == "Euro") {
                    tot = amount * 1;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be " + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Dollar" && C2.getSelectedItem().toString() == "Rupee") {
                    tot = amount * 79.62;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be " + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Dollar" && C2.getSelectedItem().toString() == "Pounds") {
                    tot = amount * 0.86;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                }
                // coverting rupee to other currency
                else if (C1.getSelectedItem().toString() == "Rupee" && C2.getSelectedItem().toString() == "Euro") {
                    tot = amount * 0.013;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Rupee" && C2.getSelectedItem().toString() == "Pounds") {
                    tot = amount * 0.011;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Rupee" && C2.getSelectedItem().toString() == "Dollar") {
                    tot = amount * 0.013;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                }
                // coverting euro to other currency
                else if (C1.getSelectedItem().toString() == "Euro" && C2.getSelectedItem().toString() == "Rupee") {
                    tot = amount * 79.76;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Euro" && C2.getSelectedItem().toString() == "Dollar") {
                    tot = amount * 1;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Euro" && C2.getSelectedItem().toString() == "Pounds") {
                    tot = amount * 0.86;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                }

                // coverting pounds into other currency
                else if (C1.getSelectedItem().toString() == "Pounds" && C2.getSelectedItem().toString() == "Euro") {
                    tot = amount * 1.16;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Pounds" && C2.getSelectedItem().toString() == "Rupee") {
                    tot = amount * 92.70;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                } else if (C1.getSelectedItem().toString() == "Pounds" && C2.getSelectedItem().toString() == "Dollar") {
                    tot = amount * 1.16;
                    JOptionPane.showMessageDialog(B1, "Your Amount will be" + tot.toString());
                }

                else {
                    JOptionPane.showMessageDialog(B1, "invaild");
                }

            }
        });
    }

    public static void main(String args[]) {
        Currency();

    }

}