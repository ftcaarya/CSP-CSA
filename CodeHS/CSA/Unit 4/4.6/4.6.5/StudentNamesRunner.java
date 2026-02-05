import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class StudentNamesRunner
{
    public static void main(String[] args)
    {
        String[] students = new String[50];
        
        try
        {
            File file = new File("StudentNames.txt");
            Scanner input = new Scanner(file);
            int index = 0;
            
            while (input.hasNext())
            {
                String name = input.nextLine();
                students[index] = name;
                index++;
            }
            input.close();
        }
        catch (IOException e)
        {
            System.out.println("File not found: " + e.getMessage());
        }
        
        mystery(students, "Maya");
        
        int result = firstNameLetter(students, "M");
System.out.println("Number of students whose first name starts with M: " + result);

    }
    
    public static void mystery(String[] arr, String name)
    {
        for (String item : arr)
        {
	        if (item != null && item.contains(name))
	        {
	            System.out.println(name);
	        }
        }
    }
    
    public static int firstNameLetter(String[] arr, String letter)
{
    int count = 0;

    for (String name : arr)
    {
        // Make sure the element is not null
        if (name != null)
        {
            // Get the first letter of the name
            String firstLetter = name.substring(0, 1);

            if (firstLetter.equalsIgnoreCase(letter))
            {
                count++;
            }
        }
    }

    return count;
}

}