/*// by manish kumar m
//package statement default it is lang
//import 
public class workshop2
{
	
	public static void main(String s[])
	{


		out:for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(j==1)
				continue out;
				if(j==2)
				break out;
			}
		}
				
	}
}// by manish kumar m
//package statement default it is lang
//import 
public class workshop2
{
	static int a,b,c;
	workshop2(int a,int b,int c)
	{
		this.a=a;
		this .b=b;
		this.c=c;
	}
	public static void main(String s[])
	{
		//int [][]a;
		workshop2 o= new workshop2(12,3,4);
		//System.out.println(o.c);
		int [] a=new int[5];
		//System.out.println(a[6]);
				
	}
}// by manish kumar m
//package statement default it is lang
//import 
public class workshop2
{
	int d;//instance variable
	static int a,b,c;//class variable
	workshop2()
	{
		System.out.println("!");
	}
	workshop2(int a,int b,int c)
	{this();
		System.out.println("#");
	}
	public static void main(String s[])
	{
		//int [][]a;
		workshop2 o= new workshop2(12,3,4);
		//System.out.println(o.c);
		int [] a=new int[5];
		//System.out.println(a[6]);
				
	}
}workshop2(int a,int b,int c)
	{
		System.out.println("#");
	}default constructor 
/*program to print this pattern
123456789
1234  6789
123    789
12      89
1        9

class pattern1
{
	public static void main(String s[])
	{
		int c=0,m1,m2,n=9;
		int [] a=new int[50];
		int i;
		for(i=0;i<=8;i++)//for
		a[i]=i+1;
             int y=n-2;
		do//do while
		{
			m1=(4)+c;
			m2=(4)-c;
			if(c==0)//if 
			{
				for(i=0;i<n;i++)
				System.out.print(a[i]);
			}
			else
			{
				for(i=0;i<=m2;i++)
				System.out.print(a[i]);
				for(i=m2;i<m1;i++)
				System.out.print(" ");
				for(i=m1;i<n;i++)
				System.out.print(a[i]);
			}
			c++;
			System.out.println();
		}while(m1!=9);
	}
}
  
class workshop2
{
		final static int d;
		public static void main(String s[])
		{
		d=45;
		final int a;
		a=13;
		System.out.println(a);
		System.out.println(d);
		}
}
class workshop2
{

		public static void main(String s[])
		{
			int n1=Integer.parseInt(s[0]);
			int n2=Integer.parseInt(s[1]);
			System.out.println(n2+n1);
		}
}*/