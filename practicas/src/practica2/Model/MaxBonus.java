package practica2.Model;

import practica2.Model.Interfaces.Bonus;

public class MaxBonus implements Bonus {

    public Double getBonus(Double salary) {
        return salary*0.20;
    }
}
