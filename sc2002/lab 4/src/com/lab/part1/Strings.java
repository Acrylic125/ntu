package com.lab.part1;

import java.util.Scanner;
public class Strings
{
// --------------------------------------------
// Reads in an array of integers, sorts them,
// then prints them in sorted order.
// --------------------------------------------
    public static void main (String[] args)
    {
        String[] intList;
        int size;
        Scanner scan = new Scanner(System.in);
        System.out.print ("\nHow many strings do you want to sort? ");
        size = scan.nextInt();
        intList = new String[size];
        System.out.println ("\nEnter the numbers...");
        for (int i = 0; i < size; i++)
            intList[i] = scan.next();
        Sorting.insertionSort(intList);
        // Sorting.selectionSort(intList);
        System.out.println ("\nYour numbers in sorted order...");
        for (int i = 0; i < size; i++)
            System.out.print(intList[i] + " ");
        System.out.println ();
    }
}
