package practica2.Model;

public class SeniorDeveloper extends Employee {

    private int workHours;

    public SeniorDeveloper() {
    }

    public SeniorDeveloper(Double salary, Bonus bonus, int workHours) {
        super(salary, bonus);
        this.workHours = workHours;
    }

    public int getWorkHours() {
        return workHours;
    }

    public void setWorkHours(int workHours) {
        this.workHours = workHours;
    }
}
