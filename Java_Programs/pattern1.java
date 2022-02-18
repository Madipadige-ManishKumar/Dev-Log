/*program to print this pattern
123456789
1234  6789
123    789
12      89
1        9
*/
class pattern1
{
	public static void main(String s[])
	{
		int c=0,m1,m2,n=9;
		int [] a=new int[50];
		int i;
		for(i=0;i<=8;i++)//for
		a[i]=i+1;
             int y=n-2;
		do//do while
		{
			m1=(4)+c;
			m2=(4)-c;
			if(c==0)//if 
			{
				for(i=0;i<n;i++)
				System.out.print(a[i]);
			}
			else
			{
				for(i=0;i<=m2;i++)
				System.out.print(a[i]);
				for(i=m2;i<m1;i++)
				System.out.print(" ");
				for(i=m1;i<n;i++)
				System.out.print(a[i]);
			}
			c++;
			System.out.println();
		}while(m1!=9);
	}
}
				