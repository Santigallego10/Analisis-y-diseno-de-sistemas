package practica3.controllers;

import practica3.model.User;
import practica3.services.impl.OccasionalBuyer;
import practica3.services.impl.WholesaleBuyer;
import practica3.services.UserService;
import practica3.services.WelcomeUser;
import practica3.services.impl.UserServiceImp;

import javax.swing.*;

public class UserController {

    UserService userService = new UserServiceImp();

    public UserController() {
    }

    public UserController(UserService userService) {
        this.userService = userService;
    }

    //METHODS


    public void addUser(){
        String name = JOptionPane.showInputDialog("Write the name");
        String id = JOptionPane.showInputDialog("Write the id");
        String address = JOptionPane.showInputDialog("Write the address");
        String phoneNumber = JOptionPane.showInputDialog("Write the phone number");
        String email = JOptionPane.showInputDialog("Write the email");
        WelcomeUser userType = showUserTypeMenu();
        userService.addUser(name, id, address, phoneNumber, email, userType);
    }

    public void updateUser(){
        User user = findUser();
        userService.updateUser();
    }

    private User findUser() {
        User user = null;
        String id = JOptionPane.showInputDialog("Write the id to find an user to update");



        return user;
    }

    public void deleteUser(){
        userService.deleteUser();
    }

    private WelcomeUser showUserTypeMenu() {
        WelcomeUser type = null;
        String[] options = new String[] {"Occasional User", "Wholesale Buyer"};
        int response = JOptionPane.showOptionDialog(null, "Please select an option", "Te Lo Consigo Store",
                JOptionPane.PLAIN_MESSAGE, JOptionPane.PLAIN_MESSAGE,
                null, options, options[0]);

        switch (response){
            case 0:
                return new OccasionalBuyer();
            case 1:
                return new WholesaleBuyer();
        }
        return null;
    }






}
