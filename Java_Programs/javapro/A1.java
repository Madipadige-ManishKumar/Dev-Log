package samepackage;
public class A1
{
	public int a=10;
	int b=20;	
	protected int c=30;
	private int d=40;
	public void display()
	{

		System.out.println("In same package in same class a:"+a);
		System.out.println("In same package in same class b:"+b);
		System.out.println("In same package in same class c:"+c);
		System.out.println("In same package in same class d:"+d);	
	}
	public static void main(String []s )	
	{
		A1 obj = new A1();
		obj.display();
		System.out.println("THIS PROGRAM IS EXECUTED BY 21001-CS-076");
}}