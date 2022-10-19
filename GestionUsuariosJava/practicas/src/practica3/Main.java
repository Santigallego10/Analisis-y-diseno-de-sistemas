package practica3;

import practica3.controllers.UserController;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {

        UserController userController = new UserController();

        boolean flag = true;

        while(flag){
            switch (showMainMenu()){
                case 0:
                    flag = false;
                    break;
                case 1:
                    showUsersManagementMenu(userController);
                    default:
                    break;
            }
        }

    }

    private static void showUsersManagementMenu(UserController userController) {
        String[] options = new String[] {"Exit", "Delete User", "Update User", "Create User"};
        int response = JOptionPane.showOptionDialog(null, "Please select an option", "Te Lo Consigo Store",
                JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE,
                null, options, options[0]);
        switch (response){
            case 0:
                break;
            case 1:
                userController.deleteUser();
                break;
            case 2:
                userController.updateUser();
                break;
            case 3:
                userController.addUser();
                break;
            default:
                break;
        }
    }

    private static int showMainMenu() {
        String[] options = new String[] {"Exit", "Manage Users"};
        int response = JOptionPane.showOptionDialog(null, "Welcome to 'Te lo consigo'\nPlease select an option", "Te Lo Consigo Store",
                JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE,
                null, options, options[0]);
        return response;

    }
}
