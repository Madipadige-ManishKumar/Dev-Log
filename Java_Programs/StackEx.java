import java.util.*;
public class StackEx
{
	public static void main(String args[])
	{
		Stack<String> st = new Stack<String>();
		while(true)
		{
			System.out.println("ENTER 1 TO PUSH");
			System.out.println("ENTER 2 TO POP");
			System.out.println("ENTER 3 TO SEE ELEMENT");
			System.out.println("ENTER 4 TO SEARCH");
			System.out.println("ENTER 5 TO EXIT");
			int choice;
			Scanner sc =new Scanner(System.in);
			System.out.println("ENTER YOUR CHOICE");
			choice=sc.nextInt();
			String  s;
			sc.nextLine();
			switch(choice)
			{
				case 1:
					System.out.println("YOU SELECTED TO PUSH");
					System.out.println("ENTER--");
					s=sc.nextLine();
					st.push(s);
					break;
				case 2:
					System.out.println("YOU SELECTED TO POP ");
					System.out.println("POPPED IS "+st.pop());
					break;
				case 3:
					System.out.println("SELECTED TO PEEK");
					System.out.println(" ELEMENT AT TOP "+st.peek());
					break;
				case 4:
					System.out.println("SEARCHING IS SELECTED ");
					System.out.println("ENTER THE VALUE TO SEARCH");
					String d=sc.nextLine();
					System.out.println("INEDX ="+st.search(d));
					break;
				case 5:
					System.exit(1);break;
				default: System.out.println("INVAILD TRY AGAIN");
			}
		}
	}
}