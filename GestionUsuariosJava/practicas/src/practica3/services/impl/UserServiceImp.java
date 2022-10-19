package practica3.services.impl;

import practica3.model.User;
import practica3.services.UserService;
import practica3.services.WelcomeUser;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class UserServiceImp implements UserService {

    List<User> userList = new ArrayList<>();

    @Override
    public void addUser(String name, String id, String address, String phoneNumber, String email, WelcomeUser userType) {
        User user = new User(name, id, address, phoneNumber, email, userType);
        userList.add(user);
        user.welcome();
        printList(userList);
    }


    private void printList(List<User> userList) {
        System.out.println("Print: ");
        for (User user: userList) {
            System.out.println(user.toString());
        }
    }

    @Override
    public void updateUser(String name, String id, String address, String phoneNumber, String email, User user) {
        user.setName(name);
        user.setId(id);
        user.setAddress(address);
        user.setPhoneNumber(phoneNumber);
        user.setEmail(email);
        printList(userList);
        JOptionPane.showMessageDialog(null, "The user "+user.getName()+" has been updated", "Updated", JOptionPane.INFORMATION_MESSAGE, null);
    }

    @Override
    public void deleteUser(User user) {
        System.out.println("Delete user service");
        userList.remove(user);
        printList(userList);
    }

    @Override
    public User findUser(String id) {
        for (User user:userList) {
            if(user.getId().equals(id)){
                return user;
            }
        }
        return null;
    }
}
