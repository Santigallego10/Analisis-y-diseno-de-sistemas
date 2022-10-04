package practica2.Model;

import practica2.Model.Interfaces.Bonus;

public class MinBonus implements Bonus {

    public Double getBonus(Double salary) {
        return salary*0.10;
    }
}
