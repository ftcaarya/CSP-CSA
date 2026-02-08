package FunPrograms.AdventOfCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class DayTwo {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter IDS to be checked");
        String ids = input.nextLine();

        String[] idArray = ids.split(",");

        ArrayList<String> idArrayList = new ArrayList<>(Arrays.asList(idArray));

        long total = 0;

        for (String idRanges : idArrayList) {
            String[] rangeParts = idRanges.split("-");
            long start = Long.parseLong(rangeParts[0]);
            long end = Long.parseLong(rangeParts[1]);

            for (long i = start; i <= end; i++) {
                String current = Long.toString(i);
                int len = current.length();

                if (len % 2 == 0) {
                    int half = len / 2;
                    String first = current.substring(0, half);
                    String second = current.substring(half);
                    if (first.equals(second)) total += i;
                }
            }
        }

        System.out.println("Total: " + total);
        input.close();
    }


}
