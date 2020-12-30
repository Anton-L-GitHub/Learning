package com.company;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float monthlyRate = scanner.nextFloat() / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period (Years): ");
        int months = scanner.nextInt() * 12;

        double mortgage = principal * ( (monthlyRate * (Math.pow(1 + monthlyRate, months) / (Math.pow(1 + monthlyRate, months) - 1) ) ) );

        String sum = NumberFormat.getCurrencyInstance().format(mortgage);

        System.out.println(sum);
    }
}