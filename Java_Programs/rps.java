import java.util.*;
class rps
{
	public static void main(String s[])
	{
		int c=0;
		int m=0,n=0;
		int x,u,y;
		int e,r;
		e=r=0;
		x=u=y=0;
	String []rps={"r","p","s"};
		System.out.println("THERE ARE 5 ROUNDS");
            do
		{
		m=n=0;
		//System.out.println("THERE ARE 5 ROUNDS");
		String computermove =rps[new Random().nextInt(rps.length)];
		Scanner sc= new Scanner(System.in);
		System.out.println("ENTER YOUR CHOICE R,P,S");
		String playermove=sc.nextLine();
		if(playermove.equals("p")||playermove.equals("s")||playermove.equals("r")){
		System.out.println("computer move  "+computermove);
		System.out.println("PLAYERMOVE  "+playermove);
		if(computermove.equals("r")&&playermove.equals("p"))
		m=1;r++;
		if(computermove.equals("r")&&playermove.equals("s"))
		n=1;e++;
		if(computermove.equals("p")&&playermove.equals("r"))
		n=1;e++;
		if(computermove.equals("p")&&playermove.equals("s"))
		m=1;r++;
		if(computermove.equals("s")&&playermove.equals("p"))
		n=1;e++;
		if(computermove.equals("s")&&playermove.equals("r"))		
		m=1;r++;
		if(computermove.equals(playermove))
		 m=n=0;
}
else
{
		System.out.println("ENTER A VALID CHOICE");
		n=1;
}
		
		if(m==0&&n==0){
		System.out.println("tie");
		x++;}
		if(m==1){
		System.out.println("YOU WIN");
		u++;}
		if(n==1){
		System.out.println("YOU LOSE");
		y++;}
            c++;
		System.out.println("ROUND"+c+"COMPELETED");
		}while(c!=4);//while
		int h;
		h=x>u?x:u;
		int g;
		g=h>y?h:y;
		if(g==x||e==r)
		System.out.println("THE MATCH HASS BEEN TIE");
		if(g==u)
		System.out.println("YOU WON THE MATCH");
		if(g==y)
		System.out.println("YOU LOSE THE MATCH");
	}
}
	/*if(computermove ==p)
		m=1;
		if(computermove ==r)
		m=0;
		if(computermove ==s)
		m=2;
		if(playermove ==p)
		n=1;
		if(playermove ==r)
		n=0;
		if(playermove ==s)
		n=2;
		if(
*/