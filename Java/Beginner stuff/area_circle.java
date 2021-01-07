package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter the radius: ");

        double pi = Math.PI;
        double radius = scan.nextDouble();
        double area = Math.pow(radius, 2) * pi;
        double perimeter = radius * 2 * pi;

        System.out.println("Perimeter = " + perimeter);
        System.out.println("Area = " + area);

    }
}
