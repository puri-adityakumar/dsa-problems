package gfg.solutions;

import java.util.Arrays;
import gfg.interfaces.Solution;
import java.util.Scanner;

public class PushZeroAtEnd implements Solution {
    @Override
    public void execute(Scanner scanner) {
        // Test array
        int[] arr = { 0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9 };

        System.out.println("Original array: " + Arrays.toString(arr));
        pushZerosToEnd(arr);
        System.out.println("Array after moving zeros: " + Arrays.toString(arr));
    }

    @Override
    public String getProblemName() {
        return "Move all zeros to end of array";
    }

    public void pushZerosToEnd(int[] arr) {
        int count = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                int temp = arr[i];
                arr[i] = arr[count];
                arr[count] = temp;
                count++;
            }
        }
    }
}