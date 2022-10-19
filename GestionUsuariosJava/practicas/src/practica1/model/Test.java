package practica1.model;

public class Test {

    private int operator;

    private int operator2;

    public int doOperations(String operation){
        if(operation.equals("suma"))
            return operator+operator2;
        if (operation.equals("resta"))
            return operator-operator2;
        if(operation.equals("division"))
            return operator/operator2;
        return 0;
    }
}
