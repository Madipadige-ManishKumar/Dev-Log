package p2;
import p1.A;
class B extends A
{
	public static void main(String []args)
	{
		System.out.println("THIS IS B AND IMPORT PACKAGE P1");
		A o = new A();
		o.Display();	
		o.Display1();

	}
}