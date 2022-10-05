package practica3.services;

public interface UserService {

    public void addUser(String name, String id, String address, String phoneNumber, String email, WelcomeUser userType);

    public void updateUser();

    public void deleteUser();
}
