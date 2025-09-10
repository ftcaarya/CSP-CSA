public class TipCalculator
{
    public static void main(String[] args)
    {
        double meal = 25.99;
        double appetizer = 6.50;
        double drink = 3.99;

        // Create variables to store the different tip options
        double total = meal + appetizer + drink;
        double tip15 = total * .15;
        double tip20 = total * .2;
        double tip25 = total * .25;

        // Print out the total and different amounts for each tip option
        System.out.println("Total cost of the mean: " + total);
        System.out.println("15% tip amount: " + tip15);
        System.out.println("20% tip amount: " + tip20);
        System.out.println("25% tip amount: " + tip25);
    }
}