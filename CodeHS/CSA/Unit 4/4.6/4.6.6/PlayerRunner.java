import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class PlayerRunner
{
    public static void main(String[] args)
    {
        // Create array to store players (top 30)
        String[] players = new String[30];
        int index = 0;

        // Read Players.txt using try-catch
        try
        {
            File file = new File("Players.txt");
            Scanner input = new Scanner(file);

            while (input.hasNextLine() && index < players.length)
            {
                players[index] = input.nextLine();
                index++;
            }

            input.close();
        }
        catch (IOException e)
        {
            System.out.println("File error: " + e.getMessage());
        }

        // Test the countryNumPlayers method
        countryNumPlayers(players, "Argentina");
        countryNumPlayers(players, "Brazil");
        countryNumPlayers(players, "Portugal");
    }
    
    // Prints players from a country and returns the count
    public static int countryNumPlayers(String[] arr, String country)
    {
        int count = 0;

        System.out.println("\nPlayers from " + country + ":");

        for (String player : arr)
        {
            if (player != null && player.contains(country))
            {
                System.out.println(player);
                count++;
            }
        }

        System.out.println("Total players from " + country + ": " + count);
        return count;
    }
}