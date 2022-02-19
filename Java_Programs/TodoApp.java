import java.util.ArrayList;
import java.util.Scanner;

public class TodoApp {
    private ArrayList<String> todos;

    public TodoApp() {
        todos = new ArrayList<String>();
    }

    public void addTodo() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your todo: ");
        String todo = scanner.nextLine();
        todos.add(todo);
        System.out.println(todo + " added to the list.");
    }

    public void viewTodos() {
        System.out.println("Todos:");
        for (int i = 0; i < todos.size(); i++) {
            System.out.println((i + 1) + ". " + todos.get(i));
        }
    }

    public void removeTodo() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of the todo you want to remove: ");
        int index = scanner.nextInt();
        String todo = todos.get(index - 1);
        todos.remove(index - 1);
        System.out.println(todo + " removed from the list.");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TodoApp todoApp = new TodoApp();
        while (true) {
            System.out.println("Enter 1 to add todo, 2 to view todos, 3 to remove todo, or 4 to exit.");
            int choice = scanner.nextInt();
            if (choice == 1) {
                todoApp.addTodo();
            } else if (choice == 2) {
                todoApp.viewTodos();
            } else if (choice == 3) {
                todoApp.removeTodo();
            } else if (choice == 4) {
                System.out.println("Exiting...");
                break;
            } else {
                System.out.println("Invalid choice.");
            }
        }
    }
}