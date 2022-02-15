import java.util.*;
interface c
{
	public void set();
public	void mod();
}
interface b extends c
{
	void div();	
	void mul();
}
interface a extends b
{
	void add();
	void sub();
}
class A implements a
{
	int a1,b1;

	public void set()
	{
		Scanner sc =new Scanner(System.in);
		a1=sc.nextInt();
		b1= sc.nextInt();
	}
public 	void add()
	{
		System.out.println("ADDITION="+(a1+b1));
	}
	public void sub ()
	{
		System.out.println("Subtraction="+(a1-b1));
	}
	public void mul ()
	{
		System.out.println("Multiplication="+(a1*b1));
	}	
	public void div ()
	{
		System.out.println("Division="+(a1/b1));
	}
	public void mod ()
	{
		System.out.println("Modulo division="+(a1%b1));
	}
}
class In1
{
	public static void main(String s[])
	{
		A  o = new A();
		o.set();
	}
}