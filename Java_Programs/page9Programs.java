import java.util.*;
class  ChainConstructor
{
	int l,b,h;
	public ChainConstructor()
	{
		System.out.println(" IN DEFAULT CONSTRICTOR ");
		System.out.println(" l= "+l);
		System.out.println(" b= "+b);
		System.out.println(" h= "+h);
	}
	public ChainConstructor(int i)
	{this();
		l=b=h=i;
		System.out.println(" IN ONE PARAMETER ");
		System.out.println(" l= "+l);
		System.out.println(" b= "+b);
		System.out.println(" h= "+h);
	}
	public ChainConstructor(int i,int j,int k)
	{	this(i);
		l=i;b=j;h=k;
		System.out.println("IN THREE PARAMETER ");
		System.out.println(" l= "+l);
		System.out.println(" b= "+b);
		System.out.println(" h= "+h);
	}
	public static void main(String s[])
	{
		int i,j,k;
		Scanner sc =new	Scanner(System.in);
		System.out.println("ENTER THREE VALUES");
		i=sc.nextInt();
		j=sc.nextInt();
		k=sc.nextInt();
		ChainConstructor  o= new ChainConstructor(i,j,k);
		System.out.println("THIS PROGRAM IS EXECUTED BY 21001-CS-007");
	}
}
/*class Super
{
	Super()
	{
		System.out.println("PARAENT CLASS");
	}
}
class Sub extends Super 
{
	Sub()
	{
		super();
		System.out.println("CHILD CLASS");
	}
	public static void main(String s[])
	{
		Sub o=new Sub();
		System.out.println("THIS PROGRAM IS EXECUTED BY 21001-CS-007");
	}
}
class Uncover
{
	int s;
	void set(int s)
	{
		this.s=s;
	}
	void dis()
	{
		System.out.println("THE AREA OF SQUARE IS "+(s*s));
		System.out.println("THE PERIMETER OF SQUARE IS "+(4*s));
	}
	public static void main(String s[])
	{
		Uncover o =new Uncover ();
		int i;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER A VALUE ");
		i=sc.nextInt();
		o.set(4);
		o.dis();
		System.out.println("THIS PROGRAM IS EXECUTED BY 21001-CS-007");
	}
}
class Super
{
	int s;
	void dis()
	{
		System.out.println("THE AREA OF SQUARE IS "+(s*s));
		System.out.println("THE PERIMETER OF SQUARE IS "+(4*s));
	}

}
class Sub extends Super 
{
	void set (int s )
	{
		super.s=s;	
	}
	public static void main(String er[])
	{
		int i;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER A VALUE ");
		i=sc.nextInt();
		Sub o = new Sub();
		o.set(i);
		o.dis();
		System.out.println("THIS PROGRAM IS EXECUTED BY 21001-CS-007");
	}
}*/