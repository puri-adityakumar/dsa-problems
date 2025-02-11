package gfg;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import gfg.interfaces.Solution;
import gfg.solutions.*;

public class Main {
    private static List<Solution> solutions = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        initializeSolutions();

        while (true) {
            displayMenu();
            int choice = getChoice();

            if (choice == 0) {
                System.out.println("Exiting program...");
                break;
            }

            if (choice > 0 && choice <= solutions.size()) {
                solutions.get(choice - 1).execute(scanner); // Pass scanner to execute
            } else {
                System.out.println("Invalid choice! Please try again.");
            }
        }
        scanner.close();
    }

    private static void initializeSolutions() {
        solutions.add(new SecondLargest());
        solutions.add(new PushZeroAtEnd());
    }

    private static void displayMenu() {
        System.out.println("\n=== DSA Problems Menu ===");
        for (int i = 0; i < solutions.size(); i++) {
            System.out.printf("%d. %s%n", i + 1, solutions.get(i).getProblemName());
        }
        System.out.println("0. Exit");
        System.out.print("Enter your choice: ");
    }

    private static int getChoice() {
        try {
            return Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            return -1;
        }
    }
}