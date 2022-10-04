package practica2.Model;

public class JuniorDeveloper extends Employee {

    private String address;

    public JuniorDeveloper() {
    }

    public JuniorDeveloper(Double salary, String address) {
        super(salary, new MinBonus());
        this.address = address;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
