import java.util.Scanner;

public class IceCreamShop
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        double scoopPrice = 2.50;

        System.out.println("What flavor ice cream would you like?");
        String flavor = scanner.nextLine();

        System.out.println("How many scoops would you like?");
        int scoops = scanner.nextInt();

        double total = scoopPrice * scoops;

        System.out.println("Order Summary:");
        System.out.println("Flavor: " + flavor);
        System.out.println("Number of Scoops: " + scoops);
        System.out.println("Total: " + total);

        scanner.close();
    }
}