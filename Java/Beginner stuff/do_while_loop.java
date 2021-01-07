import java.util.Scanner;

public class do_while_loop {
    Scanner scan = new Scanner(System.in);
    String playAgain = "";

    do
    {
        int theNumber = (int) (Math.random() * 10 + 1);
        int numberOfTries = 0;
        int guess = 0;

        while (guess != theNumber) {
            numberOfTries++;
            System.out.print("\nGuess a number between 1-10: ");
            guess = scan.nextInt();

            if (guess == theNumber) {
                System.out.println(theNumber + " is correct! You win");
                System.out.println("It took you " + numberOfTries + " tries to win!");
            } else if (guess > theNumber) {
                System.out.println(guess + " is too high, try again.");
            } else {
                System.out.println(guess + " is too low, try again.");
            }
        }

        System.out.println("\nWould you like to play again? (y/n): ");
        playAgain = scan.next();
    }while(playAgain.equalsIgnoreCase("y"));
    {
        System.out.println("Thank you for playing, good bye! ");
    }
}}
