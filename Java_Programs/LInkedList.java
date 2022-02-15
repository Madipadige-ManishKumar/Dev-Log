import java.util.*;
public class  LInkedList
{
	public static void main(String s[])
	{
		LinkedList <Integer> st = new LinkedList<Integer>();
	while(true){
		System.out.println("ENTER 1 TO ADD  VALUE AT FIRST");
		System.out.println("ENTER 2 TO ADD  VALUE AT LAST");
		System.out.println("ENTER 3 TO REMOVE   VALUE AT FIRST");
		System.out.println("ENTER 4 TO REMOVE  VALUE AT LAST");
		System.out.println("ENTER 5 TO SEE  VALUE AT FIRST");
		System.out.println("ENTER 6 TO ADD  VALUE AT LAST");
		System.out.println("ENTER 7 TO EXIT");
		int choice;
		Scanner sc= new Scanner(System.in);
		System.out.println("ENTER YOUR CHOICE");
		choice =sc.nextInt();	
//		sc.nextLine(); used for string 
		int value;
		switch(choice)
		{
			case 1:
				System.out.println("YOU HAVE SELECTED TO ADD VALUE AT  FIRST");
				value=sc.nextInt();
				st.addFirst(value);
				break;
			case 2:
				System.out.println("YOU HAVE SELECTED TO ADD VALUE AT  LAST");
				value=sc.nextInt();
				st.addLast(value);
				break;
			case 3:
				System.out.println("YOU HAVE SELECTED TO REMOVE VALUE AT  FIRST");
				System.out.println("REMOVED VALUE IS "+st.removeFirst());
				break;
			case 4:
				System.out.println("YOU HAVE SELECTED TO REMOVE VALUE AT  LAST");
				System.out.println("REMOVED VALUE IS "+st.removeLast());
				break;
			case 5:
				System.out.println("YOU HAVE SELECTED TO SEE VALUE AT  FIRST");
				System.out.println(" VALUE IS "+st.peekFirst());
				break;
			case 6:
				System.out.println("YOU HAVE SELECTED TO SEE VALUE AT  LAST");
				System.out.println(" VALUE IS "+st.peekLast());
				break;
			case 7:
				System.exit(1);
				break;		
			default:
				System.out.println("INVALID \n TRY AGAIN");

		}
	}
	}
}