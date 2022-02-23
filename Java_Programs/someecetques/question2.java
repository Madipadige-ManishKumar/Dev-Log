import java.util.*;
class question2
{
    public static void main (String[] args) 
    {
        int arr1[] = {1, 2, 3};
        int arr2[] = {1, 2, 3};
	System.out.println("arr1==arr2");
	if (arr1==arr2)  // not same 
            System.out.println("Same");
        else
            System.out.println("Not same");
	System.out.println("arr1.equals(arr2)");
        if (arr1.equals(arr2))
            System.out.println("Same");
        else
            System.out.println("Not same");
	System.out.println("Array.equals(arr1,arr2)");
	if (Arrays.equals(arr1,arr2))
            System.out.println("Same");
        else
            System.out.println("Not same");
    }
}