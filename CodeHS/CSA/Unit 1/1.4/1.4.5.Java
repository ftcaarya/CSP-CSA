public class FallingBodies
{
    public static void main(String[] args)
    {
        final double g = 9.8;

        double t = 23.0;

        double h = 0.5 * g * t * t;

        double v = g * t;

        System.out.println("The height of the cliff is " + h + " m.");
        System.out.println("The final velocity of the ball is " + v + " m/s.");
    }
}
