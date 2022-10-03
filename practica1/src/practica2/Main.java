package practica2;

import practica2.Model.JuniorDeveloper;
import practica2.Model.MaxBonus;
import practica2.Model.MinBonus;
import practica2.Model.SeniorDeveloper;

public class Main {
    public static void main(String[] args) {

        JuniorDeveloper juniorDeveloper = new JuniorDeveloper(2500000.0, new MinBonus(), "Cra 27");

        SeniorDeveloper seniorDeveloper = new SeniorDeveloper(4000000.0, new MaxBonus(), 30);

        System.out.println("Bonus for junior: "+juniorDeveloper.getBonus());

        System.out.println("Bonus for senior: "+seniorDeveloper.getBonus());

    }
}
