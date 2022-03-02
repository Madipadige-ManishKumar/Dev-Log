import java.util.Scanner;

public class hello
{
    public static void main(String[] args) throws Exception
    {
        System.out.println("Enter a Value");
        Scanner sc  = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        System.out.println(n);
    }
}