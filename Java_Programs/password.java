import java.util.*;
class password
{
	public static void main(String wer[])
	{	
		String s;
		String d;
		String g=" @#$&*";
		int c=0,k=0;
		System.out.println("ENTER  A PASSWORD ");
		Scanner sc= new Scanner(System.in);
		Scanner sc1= new Scanner(System.in);
		s=sc.nextLine();
		while(true)
		{
			int ch;
			c=k=0;
			System.out.println("1-InsertAgain 2-Exit");
			ch=sc.nextInt();	
			if(ch==1){
			System.out.println("ENTER  A PASSWORD ");
			d=sc1.nextLine();
			if(d.equals(s))
			System.out.println("ALREADY EXITS ENTER AGAIN ");
			if(d.length()<8)
			System.out.println("PASSWORD SHOULD BE MINIMUM 8 CHARCTERS");
			int i;
			for(i=0;i<d.length();i++)
			{
				if(d.charAt(i)>65&&d.charAt(i)<91)
				c++;
			}
			if(c==0)
			System.out.println("THE PASSWORD SHOULD CONTAIN UPPER CASELETTER ENTER AGAIN ");
		int j;
		for(j=0;i<d.length();j++)
			{
				if(d.charAt(j)>97&&d.charAt(j)<123)
				k++;
			}
			if(k==0)
			System.out.println("THE PASSWORD SHOULD CONTAIN LOWERCASE LETTER ENTER AGAIN ");
			k=0;
			for(i=0;i<d.length();i++)
			{
				for(j=0;j<d.length();j++)
				{
					if(d.charAt(i)==g.charAt(j))
					k++;
				}
			}
			if(k==0)
			System.out.println("THE PASSWORD SHOULD CONTAIN SPECIAL SYMBOL ");
				
		}
		else
		break;
		}
	}
}