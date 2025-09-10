import java.util.Scanner;

public class PhotoWallPlanner
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int wallHeight = 8 * 12;

        System.out.println("What is the height of each picture?");
        int pictureHeight = scanner.nextInt();

        double totalRows = (double) wallHeight / pictureHeight;

        int completeRows = wallHeight / pictureHeight;

        int leftover = wallHeight % pictureHeight;

        System.out.println("Total rows (including partial rows): " + totalRows);
        System.out.println("Complete rows: " + completeRows);
        System.out.println("Inches leftover: " + leftover);

        scanner.close();
    }
}