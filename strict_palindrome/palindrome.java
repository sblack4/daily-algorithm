package strict_palindrome;

import java.io.Console;

public class palindrome {
    public static void main(String[] args){ 
        System.out.println("hello world, let's test a palindrome: \n ");
        String input = System.console().readLine();

        boolean is_palindrome = isPalindrome(input);

        System.out.println(input + " is a palindrome: " + is_palindrome);
    }

    public static boolean isPalindrome(String input) {
        int half_input_length = Math.round(input.length() / 2);
        String[] input_array = input.split("");

        for(int i=0; i<half_input_length; i++) {
            int char_to_compare = input.length() - i - 1;

            // System.out.println(input_array[i] + " " + input_array[char_to_compare]);
            if (!input_array[i].equals(input_array[char_to_compare])) {
                return false;
            }
        }
        return true;
    }
}