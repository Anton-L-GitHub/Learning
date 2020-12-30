import java.util.Scanner;


public class if_statements {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter degrees: ");
        int degrees = input.nextInt();

        if (degrees > 30)
            System.out.println("It's a hot day, remember to drink water!");
        else if(degrees >= 20)
            System.out.println("It's a nice day today");
        else
            System.out.println("It's cold today");
    }
}
