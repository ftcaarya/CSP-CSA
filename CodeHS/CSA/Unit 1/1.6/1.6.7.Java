public class HomeworkTime
{
    public static void main(String[] args)
    {
        int hours = 2;
        int minutes = 30;
        int seconds = 45;

        // convert hours to seconds
        int totalSeconds = 0;
        totalSeconds += hours * 3600;  // 1 hour = 3600 seconds

        // convert minutes to seconds
        totalSeconds += minutes * 60;  // 1 minute = 60 seconds

        // add remaining seconds
        totalSeconds += seconds;

        // print result
        System.out.println("Total time spent on homework in seconds: " + totalSeconds);
    }
}
