class Par
{
	String name;
	int r;
	String g;
	public Par(String n,int r,String h)
	{this(r);
		name=n;
		this.r=r;
		g=h;
	}
	public Par(int r)
	{ this();
	System.out.println("One Parameter Constructor ");
	}
	public Par()
	{
				System.out.println("defalut constructor ");
	}
	void dis()
	{
		System.out.println(name+"  "+r+ "  "+g+" ");
	}
}
class b extends Par
{
	String c;
	b(String n, int r, String g,String s)
	{
		super(n,r,g);
		c=s;
	}
	void dis()
	{
		super.dis();
		System.out.println(c);
	}
	public static void main(String sda[])
	{
		b o= new b("Manish",7,"Male","cse");
		o.dis();
	}
}
		