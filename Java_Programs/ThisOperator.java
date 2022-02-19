class ThisOperator 
{
	int l,b,h;
		
	public ThisOperator()
	{
	System.out.println("DEFAULT CONSTRUCTUR");
	}
public	ThisOperator(int l)
	{this();
	System.out.println("1 PARAMETER");
	}
	public ThisOperator(int l, int b,int h)
	{
		this(l);
	System.out.println("3 PARAMETER ");
	}
	public int  sum(int a,int b)
	{
		int add=a+b;
	System.out.println(add);
        return add;
	}
	public void sum(int a,int b,int c)
	{
	int r=this.sum(a,b);
	System.out.println(r+c);
	}
	public static void main(String s[])
	{
		ThisOperator o= new ThisOperator(12,3,4);
		ThisOperator o1=new ThisOperator(34);
		sum(1,2);
		sum(1,2,3);
	}
}
		