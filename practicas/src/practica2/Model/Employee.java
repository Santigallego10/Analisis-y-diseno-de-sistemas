package practica2.Model;

import practica2.Model.Interfaces.Bonus;

public class Employee{

    private Double salary;
    private Bonus bonus;

    public Employee() {
    }

    public Employee(Double salary, Bonus bonus) {
        this.salary = salary;
        this.bonus = bonus;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public double getBonus() {
        return bonus.getBonus(this.salary);
    }

    public void setBonus(Bonus bonus) {
        this.bonus = bonus;
    }
}
