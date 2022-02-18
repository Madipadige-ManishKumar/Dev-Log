import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

 class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
       Scanner scanner = new Scanner(System.in);
        int lines = 1;

        while (scanner.hasNextLine()) {
            System.out.println(lines + " " + scanner.nextLine());
            lines++;
        }
        scanner.close();
    }
    
}
