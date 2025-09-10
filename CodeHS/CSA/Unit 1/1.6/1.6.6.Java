public class PlayerHealthTracker
{
    public static void main(String[] args)
    {
        int playerHealth = 100;

        // Eats hearty hazelnuts - gains 20 health
        playerHealth += 20;
        System.out.println("Health after eating hearty hazelnuts: " + playerHealth);

        // Runs into fire - loses 15 health
        playerHealth -= 15;
        System.out.println("Health after getting burned by the fire: " + playerHealth);

        // Finds healing ointment - gains 10 health
        playerHealth += 10;
        System.out.println("Health after finding healing ointment: " + playerHealth);

        // Runs into pokey stick - loses half of health
        playerHealth /= 2;
        System.out.println("Health after getting poked by a stick: " + playerHealth);

        // Finds super power potion - triples health
        playerHealth *= 3;
        System.out.println("Health after taking super power potion: " + playerHealth);
    }
}
