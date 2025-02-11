package gfg.solutions;

import java.util.Scanner;
import gfg.interfaces.Solution;

public class SecondLargest implements Solution {
    @Override
    public void execute(Scanner scanner) {
        try {
            System.out.print("Enter array elements (space-separated): ");
            String[] input = scanner.nextLine().split(" ");

            if (input.length == 0) {
                System.out.println("Error: Empty input");
                return;
            }

            int[] arr = new int[input.length];
            for (int i = 0; i < input.length; i++) {
                arr[i] = Integer.parseInt(input[i]);
            }

            int result = getSecondLargest(arr);
            System.out.println("Second largest element: " + result);
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format");
        }
    }

    @Override
    public String getProblemName() {
        return "Second Largest Element";
    }

    public int getSecondLargest(int[] arr) {
        int alpha = -1;
        int beta = -1;

        for (int i = 0; i < arr.length; i++) {
            int current = arr[i];

            if (current > alpha) {
                beta = alpha;
                alpha = current;
            } else if (current > beta && current != alpha) {
                beta = current;
            }
        }
        return beta;
    }
}