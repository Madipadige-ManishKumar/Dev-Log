class constructor
{
	int len;
	int bre;
	int hei;//instance variable
	constructor ()
	{
		len=bre=hei=0;
	}
	constructor(int l,int b,int h)
	{

		len=l;
		bre=b;
		hei=h;
	}
	 constructor(int i)//i is local  variable 
	{
		len=bre=hei=i;
	}
	constructor( constructor q)
	{
		len=q.len;
		bre=q.bre;
		hei=q.hei;
 	}
	void set()
	{
		hei=len=bre=0;
	}
	void vol()
	{
		System.out.println("VOLUME = "+(hei*bre*hei));
	}
	public  static void main (String s[])
	{
		constructor o1=new constructor(12,3,4);
		constructor o2=new constructor(3);//initialiation of an object 
		constructor o3 =new constructor(o2);
		constructor o4= new constructor();
		o1.vol();
		o2.vol();
		o3.vol();
	}
}
class a
{
	boolean  x;
	void dis()
	{
	System.out.println(x);
	}
	public static void main(String s[]){
	a o4 = new a();
	o4.dis();
	
}
}