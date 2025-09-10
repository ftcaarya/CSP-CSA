import java.util.Scanner;

public class Banking101
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        double interestRate = 0.03;

        System.out.print("Please enter an initial balance: ");
        double balance = scanner.nextDouble();
        System.out.println("Initial balance: $" + balance);

        balance *= (1 + interestRate);
        System.out.println("Balance after interest: $" + balance);

        System.out.print("Please enter a deposit amount: ");
        double deposit = scanner.nextDouble();

        balance += deposit;

        balance *= (1 + interestRate);

        System.out.println("Final balance after interest: $" + balance);

        scanner.close();

    }
}