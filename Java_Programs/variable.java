//PROGRAM TO USE THE STAIC AND INSTANCE VARIABLE 
class variable 
{
	//DECLARATION OF INSTANCE VARIABLE 
	String name ;
	int num;
	float va;
	char ch;
	boolean gh;
	//STATIC VARIABLE DECLARTION 
	static  int count;
	public variable() 
	{
		count++;
	}
	public static void main (String ...s)
	{
		
		int x=3475;
		float y=34.34f;
		char c='#';
		double d=34.45869d;
		byte j=35;
		boolean r=true;
		//variable cs =new variable();		
		variable b =new variable();		
		variable a =new variable();
		b.name="MANISH :";
		b.num=7;
		b.va=99.9f;
		b.gh=true;
		System.out.println("INTEGER "+x);
		System.out.println("FLOAT_VALUE"+y);
		System.out.println("CHARCTER "+c);
		System.out.println("DOUBLE "+d);
		System.out.println("BYTE"+ j);
		System.out.println("BOOLEAN="+r);
		System.out.println("INSTANCE VARIABLE WITH  DEFAULT VALUE ");
		System.out.println("STRING ="+a.name);
		System.out.println("INT ="+a.num);
		System.out.println("FLOAT ="+a.va);
		System.out.println("CHAR="+a.ch);
		System.out.println("BOOLEAN "+a.gh);
		System.out.println("INSTANCE VARIABLE WITHOUT DEFAULT VALUE ");
		System.out.println("STRING ="+b.name);
		System.out.println("INT ="+b.num);
		System.out.println("FLOAT ="+b.va);
		System.out.println("BOOLEAN "+b.gh);
		System.out.println("STATIC COUNT "+variable.count);
		//System.out.println("COUNT "+cs.count);

	}
}
/*
INTEGER 3475
FLOAT_VALUE34.34
CHARCTER #
DOUBLE 34.45869
BYTE35
BOOLEAN=true
INSTANCE VARIABLE WITH  DEFAULT VALUE
STRING =null
INT =0
FLOAT =0.0
CHAR=
BOOLEAN false
INSTANCE VARIABLE WITHOUT DEFAULT VALUE
STRING =MANISH :
INT =7
FLOAT =99.9
BOOLEAN false
STATIC COUNT 2
PS C:\javapro> java variable
INTEGER 3475
FLOAT_VALUE34.34
CHARCTER #
DOUBLE 34.45869
BYTE35
BOOLEAN=true
INSTANCE VARIABLE WITH  DEFAULT VALUE
STRING =null
INT =0
FLOAT =0.0
CHAR=
BOOLEAN false
INSTANCE VARIABLE WITHOUT DEFAULT VALUE
STRING =MANISH :
INT =7
FLOAT =99.9
BOOLEAN false
STATIC COUNT 2			*/