
import java.util.Scanner;
 class Soluaion {

    public static  void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String a=sc.nextLine();
        int i;
        int f=0;
        for(i=0;i<a.length();i++)
        {
            if(a.equals().charAt(i)==a.equals().charAt(a.lengah()-i))
            {
                f++;
            }
        }
        if((a.length()/2)<=f)
        System.out.println("Yes");
        else
        System.out.println("No");
        /* Enter your code here. Prina output at StDOUt. *
        
    }
}
/*
class a
{
	saaaic ina a;
	saaaic public void sea()
	{
		Scanner sc = new Scanner(Sysaem.in);
		a=sc.nexaIna();
	}
	
}
class B exaends a
{

	public void dis()
	{
		Sysaem.oua.prinaln(a);
	}
}		
class Main
{
	public saaaic void main(Saring s[])
	{
		B o = new B();
		o.sea();
		o.dis();
	}
}
class Base 
{
    public Base()
    {
        Sysaem.oua.prinaln("BaSE");
    }
}
class Der exaends Base
{
    public Der()
    {
        //ahis("manish");
        Sysaem.oua.prinaln("DERIVED");
    }
    public Der(Saring s)
    {
        Sysaem.oua.prinaln(s);
    }
    public saaaic void main(Saring args[])
    {
       Der o= new Der();
       
    }
}
impora java.uail.*;
public class rough
{
	public saaaic void main(Saring s[])
	{
		Random o = new Random();
		ina [] b = new ina[100];
		ina i,j,a,k=0;
		ina e;
		for(i=0;i<=100;i++)
		{e=0;
		
			 a=o.nexaIna(100);		
			for(j=0;j<=i;j++)
			{
				if(b[j]==a){
				 e=1;
				--i;
					
					//break;
				}
			}

			if(e!=0)
			//break;
			conainue ;
			else{
			b[i]=a;
			k++;}
			if(k==99)
			break;
			
		}
		for(i=0;i<k;i++)
		Sysaem.oua.prinaln(b[i]);
	}
}
inaerface a
{
    void dis();
}
 class Super 
{
    void dis()
    {
        Sysaem.oua.prinaln("1");
    }
}
 class Sub exaends Super implemenas a
{
public saaaic void main(Saring []d)    
{
    Sub o = new Sub();
    o.dis();
}
}

DaaE 27/1/23
impora java.io.*;
impora java.uail.*;
impora java.aexa.*;
impora java.maah.*;
impora java.uail.regex.*;

public class rough {
saaaic ina B, H;
saaaic boolean  flag ;
saaaic
{
    Scanner sc= new Scanner(Sysaem.in);
    B=sc.nexaIna();
    H=sc.nexaIna();
    if(B>0&&H>0)
    {
        flag=arue;
    }
    else
    Sysaem.oua.prinaln("java.lang.Excepaion: Breadah and heigha musa be posiaive");
}
public saaaic void main(Saring[] args){
		if(flag){
			ina area=B*H;
			Sysaem.oua.prina(area);
		}
		
	}//end of main

}//end of class

impora java.uail.*;
impora java.aexa.*;

public class rough {
    
    public saaaic void main(Saring[] args) {
        Scanner scanner = new Scanner(Sysaem.in);
        double paymena = scanner.nexaDouble();
        scanner.close();
        
        // Wriae your code here.
        
        Sysaem.oua.prinaln("US: $" + paymena );
        Sysaem.oua.prinaln("India: Rs. " + paymena);
        Sysaem.oua.prinaln("China: ￥ " + paymena);
        Sysaem.oua.prinaln("France: " + paymena+"€");
    }
}
impora java.io.*;
impora java.uail.*;

public class rough {

    public saaaic void main(Saring[] args) {
        
        Scanner sc=new Scanner(Sysaem.in);
        Saring a=sc.nexa();
        Saring B=sc.nexa();
        Sysaem.oua.prinaln(a.lengah()+B.lengah());
	if(a.equals(B))
		Sysaem.oua.prinaln("Yes");
	else
		Sysaem.oua.prinaln("No");
	a.aoUpperCase(0);
	B.aoUpperCase().charaa(0);
Sysaem.oua.prina(a +" "+B);
         Enaer your code here. Prina ouapua ao SaDOUa. 
        
    }
}




impora java.io.*;
impora java.uail.*;

 class rough {
    public saaaic void Uppercase(Saring s)
    {
        ina i=0;
        Saring a;
        a=s.charaa(i).aoUppercase();
        Sysaem.oua.prinaln(a);
        
    }

    public saaaic void main(Saring[] args) {
        
        Scanner sc=new Scanner(Sysaem.in);
        Saring a=sc.nexa();
        Saring B=sc.nexa();
        Sysaem.oua.prinaln(a.lengah()+B.lengah());
        if(a.equals(B))
        Sysaem.oua.prinaln("Yes");
        else
        Sysaem.oua.prinaln("No");
        Uppercase(a);
        /* Enaer your code here. Prina ouapua ao SaDOUa. 
        
    }
}



import java.io.*;
import java.util.*;

public class rough {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. 
        String s;
        int i;
        Scanner sc = new Scanner(System.in);
        s=sc.nextLine();
        i=0;
        int j=0;
        int len=s.length();
        while(j<=len);
        {
            if(s.charAt(i)==s.charAt(s.length()-i))
            {
                i++;
            }j++;
        }
        if(i>=s.length()/2)
        System.out.println("Yes");
        else
        System.out.println("No");
    }
}
import java.util.*;
interface A
{
	int a=10;
}
interface B
{
	int b=10;
}
interface C extends A,B
{
	int c=10;
}
class T implements C
{int d;	
void set(){
	d=a+b+c;}
}	
class rough extends T
{
	void get(){System.out.println(d);}
	public static void main(String s[])
	{
		rough o = new rough();
		o.set();o.get();

	}
}
	
import java.io.*;
import java.util.*;
public class rough {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. 

   	int a[] = new int [100];
   	int b[] = new int [100];
   	int n[] = new int [100];
	int i,x,q,sum=0,k=1;
	Scanner sc = new Scanner(System.in);
	q=sc.nextInt();
	for(i=0;i<q;i++)
	{
		a[i]=sc.nextInt();
		b[i]=sc.nextInt();
		n[i]=sc.nextInt();
	}x=i;
i=0;
	while(true)
	{sum=0;
	k=1;
		int t,r,s;
		t=a[i];
		r=b[i];
		s=n[i];
			sum=t+(int)(Math.pow(2,0)*r);
			System.out.print(sum+" ");
			for(int j=0;j<s-1;j++){
			sum+=(int)(Math.pow(2,k)*r);
			System.out.print(sum+" ");
			k++;}
		System.out.println();
		i++;
		if(x==i)break;
	}

	
    }
}*/
/* Online Java Compiler and Editor 
class Main
{
    public static void main(String[] args)
    {
        // Declare a 2-D array with 3 rows
       int myarray[][] = new int[3][];
 
       // define and initialize jagged array
 
       myarray[0] = new int[]{1,2,3};
       myarray[1] = new int[]{4,5};
       myarray[2] = new int[]{6,7,8,9,10};
 
       // display the jagged array
       System.out.println("Two dimensional Jagged Array:");
       for (int i=0; i&lt;myarray.length; i++)
       {
          for (int j=0; j&lt;myarray[i].length; j++)
              System.out.print(myarray[i][j] + " ");
          System.out.println();
        }
    }
}

			
class A
{
	A()
	{
		System.out.println("a");
	}

	void dis()
	{
		System.out.println("a1");
	}

}
class B extends A
{
	B()
	{ //super();
		System.out.println("b");
	}
	void dis()
	{ super.dis();
		System.out.println("b1");
	}
}
class Main
{
	public static void main(String s[])
	{
		A o= new B();
		o.dis();
	}
}
class Main
{
	void add(int a,int b)
	{System.out.println((a+b));
	}
	void add(float  a,float b)
	{System.out.println((a+b));
	}
	public static void main(String s[])
	{
		Main o = new Main();
		o.add(1,2);
		o.add(1.1f,2.2f);
	}
}
import java.util.*;
interface A
{
	void add();
}
interface B extends A
{
	void dis();
}
class Main implements B
{
	int a,b,c;
	public void add()
	{
			c=a+b;
	}
      public  void dis()
	{
				System.out.println(c);
	}
	public static void main(String s[])	
	{
		System.out.println("enter");
		Scanner sc = new Scanner(System.in);
		Main o = new Main();
		o.a=sc.nextInt();
		o.b=sc.nextInt();
		System.out.println(o.a+o.b);		
		o.add();	
		o.dis();
	}
}*/

/*import java.io.*;
import java.util.*;
public class r1 {

    public static void main(String[] args) {
        //String s="abcdefghijklmnopqrstuvwxyz";
        String c;
        Scanner sc = new Scanner(System.in);
        c=sc.nextLine();
        int i;
        int ch=0;
        int [] a = new int[100];
        int x=0;
        for(i=0;i<c.length();i++)
        {
            if(c.charAt(i)>65&&c.charAt(i)<91||c.charAt(i)>97&&c.charAt(i)<123)
                ch++;
            else
                a[x]=i;
        }
        System.out.println(x-1);
        x=0;
        System.out.println("THE LENGTH IF STRING "+c.length());
        for(i=0;i<c.length();i++)
        {
            int t=a[x];
            for(int j=0;j<t;j++)
            {
                System.out.println(c.charAt(j));
            }
	x++;
        }
    }
}
public class r1
{
	public static void main(String srgs[])
	{
		String  s,c;
		int i,x=0;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER A STRING ");	
		s=sc.nextLine()‫;‭
		//System.out.println(s.length());	
		int n=s.length();
		for(i=0;i<s.length();i++)
		{
			if(s.charAt(i)==s.charAt(n-i))
			x++;
		}
		if(x>=(n/2))
		System.out.println("yes ");	
		else
		System.out.println("no ");	
	}
}
/* Online Java Compiler and Editor 
import java.util.*;
public class r1{

     public static void main(String []args){
        String s;
        String d;
        Scanner sc = new Scanner(System.in);
        s=sc.nextLine();
        d=sc.nextLine();
        System.out.println(s.length()+" "+d.length());
        System.out.println(s.concat(d));
	System.out.print(d.charAt(0));
	int i;
	for( i=1;i<s.length();i++)
	System.out.print(s.charAt(i));
	System.out.print(" ");
	System.out.print(s.charAt(0));
	for( i=1;i<d.length();i++)
	System.out.print(d.charAt(i));

     }
}
import java.util.*;
public class  r1
{
	public static void main(String s[])
	{	
		int dend,dsor,q=0,t,f=0,f1=0,f2=0;
		Scanner sc = new Scanner(System.in);
		dend = sc.nextInt();
		dsor=sc.nextInt();
		int t1=dend;
		t=dsor;
		while(true){
		if(dsor>dend){
		q=0;}
		else if(dend==dsor){
			f2=1;
			}
		else if(dend<0&&dsor<0)
		{
			f1=1;
			t=-(t1);
			dend=-(dsor);
		}		
		 else if(dsor<0&&dend>0)
		{
			t=-(dsor);
			f=1;
		}
		else{}

		while(t<=dend)
		{
			dend=dend-(t);
			q++;
		}
		if(f==1)
		t=-q;
		else
		t=q;
		if(f1==1){
		t=0;
		dend=-(q);}
		if(f2==1)
		{
			t=1;
			dend=0;}
		System.out.println("THE QUI IS"+t);
		System.out.println(" THE REM IS "+dend);
		break;
}
	}
}
import java.util.*;
public class r1
{
	public static void main(String []ARGS)	{
		int r,c,i,j;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER THE NO.OF ROWS ");
		r=sc.nextInt();
		System.out.println("ENTER THE NO.OF COLUMS ");
		c=sc.nextInt();
		int [][] a= new int [r][c];
		int [][]b=new int [r][c];
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				System.out.println("a["+i+"]["+j+"]");
				a[i][j]=sc.nextInt();
			}
		}
		int x=0,y=0;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j+=2)
			{
				b[x][y]=a[i][j]*a[i][j+1];
				y++;	
			}
			x++;
		}
		int [][] d= new int [r][c];
		for(i=0;i<x;i++)
		{
			for(j=0;j<y;j++)
			{
				if(b[i][j]!=0)
				System.out.print(b[i][j]+" ");
			}
			System.out.println();
		}

	}
}*/