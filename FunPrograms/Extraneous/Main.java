package FunPrograms.Extraneous;

import java.util.Scanner;

public class Main {
    private static int binaryNum;
    private static Scanner input = new Scanner(System.in);


    public static void main(String[] args) throws Exception {

        String binaryInput = Integer.toString(askBinary());
        int decimalOutput;

        if (binaryInput.length() > 10) {
            decimalOutput = moreThanTenConv(binaryInput);
        } else {
            decimalOutput = lessThanTenConv(binaryInput);
        }

        System.out.println("The decimal equivalent is: " + decimalOutput);
    }

    public static int askBinary() {
        System.out.print("Enter a binary number: ");
        String input = Main.input.nextLine();
        checkBinary(input);
        binaryNum = Integer.parseInt(input);
        return binaryNum;
    }

    public static void checkBinary(String binaryNum) {
        binaryNum = askBinary() + "";
        for (int i = 0; i < binaryNum.length(); i++) {
            char digit = binaryNum.charAt(i);
            if (digit != '0' && digit != '1') {
                System.out.println("Invalid binary number. Please try again.");
                checkBinary(askBinary() + "");
            } else {
                break;
            }
        }
    }

    public static int moreThanTenConv(String binary) {
        int index = -1;
        int power = 0;
        int decimalNum = 0;
        while (binary.length() + index >= 0) {
            char digit = binary.charAt(binary.length() + index);
            if (digit == '1') {
                decimalNum += Math.pow(2, power);
            }
            power++;
            index--;
        }
        return decimalNum;
    }

    public static int lessThanTenConv(String binary) {
        int power = 0;
        int decimalNum = 0;
        for (int i = binary.length() - 1; i >= 0; i--) {
            char digit = binary.charAt(i);
            if (digit == '1') {
                decimalNum += Math.pow(2, power);
            }
            power++;
        }
        return decimalNum;
    }
}
