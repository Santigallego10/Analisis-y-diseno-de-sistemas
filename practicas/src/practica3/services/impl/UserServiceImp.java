package practica3.services.impl;

import practica3.model.User;
import practica3.services.UserService;
import practica3.services.WelcomeUser;

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
        for (User user: userList) {
            System.out.println(user.toString());
        }
    }

    @Override
    public void updateUser() {

    }

    @Override
    public void deleteUser() {

    }
}
