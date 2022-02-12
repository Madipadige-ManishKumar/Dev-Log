class Exam1 extends Exception{
}
class Ecet extends Exam1{}

class Main
{
public static void  main(String []args)
{
try{
	throw new Ecet();
}
catch( Exam1 e)
{
System.out.println("Hello");
}
finally
{
System.out.println("Bye");
}
}
}
