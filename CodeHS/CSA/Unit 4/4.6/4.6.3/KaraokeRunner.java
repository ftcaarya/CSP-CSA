import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class KaraokeRunner
{
   public static void main(String[] args) throws IOException
   {
        // Create a File object (must match EXACTLY)
        File songFile = new File("As It Was.txt");

        // Create a Scanner object
        Scanner input = new Scanner(songFile);

        // Print each line of the song
        while (input.hasNextLine())
        {
            System.out.println(input.nextLine());
        }

        // Close the Scanner
        input.close();
   }
}