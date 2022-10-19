package practica3.model;

import practica3.services.WelcomeUser;

public class User {

    private String name;
    private String id;
    private String address;
    private String phoneNumber;
    private String email;
    private WelcomeUser welcomeUserType;

    public User() {
    }

    public User(String name, String id, String address,
                String phoneNumber, String email, WelcomeUser welcomeUserType) {
        this.name = name;
        this.id = id;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.welcomeUserType = welcomeUserType;
    }

    public void welcome(){
        welcomeUserType.welcomeUser(this.name);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public WelcomeUser getBuyerType() {
        return welcomeUserType;
    }

    public void setBuyerType(WelcomeUser welcomeUserType) {
        this.welcomeUserType = welcomeUserType;
    }

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", id='" + id + '\'' +
                ", address='" + address + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", email='" + email + '\'' +
                ", welcomeUserType=" + welcomeUserType +
                '}';
    }
}
