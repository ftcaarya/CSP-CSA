public class IntegerOverflow
{
    public static void main(String[] args)
    {
        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;

        System.out.println("Minimum int value: " + min);
        System.out.println("Maximum int value: " + max);

        System.out.println("Minimum value - 1: " + (min - 1));
        System.out.println("Maximum value + 1: " + (max + 1));
        System.out.println("Maximum value * 2: " + (max * 2));
        System.out.println("Minimum value / 2: " + (min / 2));
    }
}
