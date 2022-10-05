package practica3.services.impl;

import practica3.services.WelcomeUser;

import javax.swing.*;

public class OccasionalBuyer implements WelcomeUser {

    @Override
    public void welcomeUser(String name) {
        JOptionPane.showMessageDialog(null, name + " you have successfully registered\n COMING SOON: web catalog of technology products.");
    }
}
