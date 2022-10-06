package practica3.controllers;

import practica3.model.User;
import practica3.services.impl.OccasionalBuyer;
import practica3.services.impl.WholesaleBuyer;
import practica3.services.UserService;
import practica3.services.WelcomeUser;
import practica3.services.impl.UserServiceImp;

import javax.swing.*;
import javax.xml.namespace.QName;

public class UserController {

    UserService userService = new UserServiceImp();

    public UserController() {
    }

    public UserController(UserService userService) {
        this.userService = userService;
    }

    //METHODS

    public void addUser() {
        String name;
        String id;
        String address;
        String phoneNumber;
        String email;
        do {
            name = JOptionPane.showInputDialog("Write the name");
        } while (validateField(name));
        do {
            id = JOptionPane.showInputDialog("Write the id");
        } while (validateField(id));
        do {
            address = JOptionPane.showInputDialog("Write the address");
        } while (validateField(address));
        do {
            phoneNumber = JOptionPane.showInputDialog("Write the phone number");
        } while (validateField(phoneNumber));
        do {
            email = JOptionPane.showInputDialog("Write the email");
        } while (validateField(email));
        WelcomeUser userType = showUserTypeMenu();
        userService.addUser(name, id, address, phoneNumber, email, userType);
    }

    public void updateUser() {
        User user;
        do {
            user = findUser();
        } while (user == null);
        String name = (String)JOptionPane.showInputDialog(null, "Please enter the new name","Update "+user.getName()
                ,JOptionPane.QUESTION_MESSAGE,null,null,user.getName());
        String id = (String)JOptionPane.showInputDialog(null, "Please enter the new id","Update "+user.getName()
                , JOptionPane.QUESTION_MESSAGE,null,null,user.getId());
        String address = (String)JOptionPane.showInputDialog(null, "Please enter the new address","Update "+user.getName()
                , JOptionPane.QUESTION_MESSAGE,null,null,user.getAddress());
        String phoneNumber = (String)JOptionPane.showInputDialog(null, "Please enter the new phoneNumber","Update "+user.getName()
                , JOptionPane.QUESTION_MESSAGE,null,null,user.getPhoneNumber());
        String email = (String)JOptionPane.showInputDialog(null, "Please enter the new email","Update "+user.getName()
                , JOptionPane.QUESTION_MESSAGE,null,null,user.getEmail());
        userService.updateUser(name, id, address, phoneNumber, email, user);
    }

    private User findUser() {
        String id = JOptionPane.showInputDialog("Write the id to search the user");
        return userService.findUser(id);
    }

    private boolean validateField(String data) {
        if(data.isBlank()){
            JOptionPane.showMessageDialog(null, "You have to enter a name","ERROR",JOptionPane.ERROR_MESSAGE );
            return true;
        }else {
            return false;
        }
    }

    public void deleteUser(){
        String id = JOptionPane.showInputDialog("Write the id to search the user you want to delete");
        User user = userService.findUser(id);
        userService.deleteUser(user);
    }

    private WelcomeUser showUserTypeMenu () {
            WelcomeUser type = null;
            String[] options = new String[]{"Occasional User", "Wholesale Buyer"};
            int response = JOptionPane.showOptionDialog(null, "Please select an option", "Te Lo Consigo Store",
                    JOptionPane.PLAIN_MESSAGE, JOptionPane.PLAIN_MESSAGE,
                    null, options, options[0]);

            switch (response) {
                case 0:
                    return new OccasionalBuyer();
                case 1:
                    return new WholesaleBuyer();
            }
            return null;
    }
}
