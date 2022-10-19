package practica3.services.impl;

import practica3.services.WelcomeUser;

import javax.swing.*;

public class WholesaleBuyer implements WelcomeUser {

    @Override
    public void welcomeUser(String name) {
        JOptionPane.showConfirmDialog(null, name+" We have send you and email ;Do you accept the terms and conditions?");
    }
}
