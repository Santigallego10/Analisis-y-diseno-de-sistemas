package practica3.services;

import practica3.model.User;

public interface UserService {

    public void addUser(String name, String id, String address, String phoneNumber, String email, WelcomeUser userType);

    public void updateUser(String name, String id, String address, String phoneNumber, String email, User user);

    public void deleteUser(User user);

    User findUser(String id);
}
