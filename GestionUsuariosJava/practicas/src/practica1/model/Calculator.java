package practica1.model;

public class Calculator {

    private String nombre;

    private String operador2;

    private String operador3;


    public String sayHi() throws Exception {
        validateName();
        return "Hi everyone";
    }


    //The method is private because we won't use it outside this class
    private void validateName() throws Exception {
        if(nombre.equals("Pedro")){
            throw new Exception("I hate pedro");
        }
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getOperador2() {
        return operador2;
    }

    public void setOperador2(String operador2) {
        this.operador2 = operador2;
    }

    public String getOperador3() {
        return operador3;
    }

    public void setOperador3(String operador3) {
        this.operador3 = operador3;
    }
}
