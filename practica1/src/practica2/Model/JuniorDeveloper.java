package practica2.Model;

public class JuniorDeveloper extends Employee {

    private String address;

    public JuniorDeveloper() {
    }

    public JuniorDeveloper(Double salary, Bonus bonus, String address) {
        super(salary, bonus);
        this.address = address;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
