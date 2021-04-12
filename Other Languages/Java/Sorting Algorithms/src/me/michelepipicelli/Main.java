package me.michelepipicelli;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Integer[] unsortedArray = {9, 6, 1, 3, 5, 7, 10, 8, 2, 4, 1, 9};
        boolean sorted = false;
        int i = 0;

        // System.out.println(Arrays.toString(bubbleSort(unsortedArray)));

        while (!sorted) {

            if (checkSorted(unsortedArray)) {
                System.out.println("Sorted in " + i + " attempts\nSorted: " + Arrays.toString(unsortedArray));
                sorted = true;
                break;
            }
            i++;
            unsortedArray = shuffle(unsortedArray);
            System.out.println("Unsorted: " + Arrays.toString(unsortedArray) + "\nAttempt: " + i);
        }
    }

    public static Integer[] bubbleSort(Integer[] array) {
        while (true) {
            if (checkSorted(array)) {
                return array;
            } else {
                for (int i = 0; i < array.length - 1; i++) {
                    int first = array[i];
                    int second = array[i + 1];
                    if (array[i] > array[i + 1]) {
                        array[i + 1] = first;
                        array[i] = second;
                    }
                }
                if (checkSorted(array))
                    return array;
            }
        }
    }

    public static boolean checkSorted(Integer[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public static Integer[] shuffle(Integer[] intArray) {

        List<Integer> intList = Arrays.asList(intArray);

        Collections.shuffle(intList);

        intList.toArray(intArray);

        return intArray;
    }
}
