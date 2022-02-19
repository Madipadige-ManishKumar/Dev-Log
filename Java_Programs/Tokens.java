import java.util.*;
public class Tokens
{
	public static void main(String args[])
	{
		int i=1;
		String s ="THIS IS CSE CLASS";
		String D="THIS,IS,CSE,CLASS";
		StringTokenizer st =new StringTokenizer(s," ",true);
		StringTokenizer dt =new StringTokenizer(D,",",true);
		System.out.println("STRING 1");
		while(st.hasMoreTokens())
		{
			System.out.println("TOKEN"+i+"= "+st.nextToken());
			i++;
		}
		i=1;
		System.out.println("STRING 2");
		while(dt.hasMoreTokens())
		{
			System.out.println("TOKEN"+i+"= "+dt.nextToken());
			i++;
		}
	}
}