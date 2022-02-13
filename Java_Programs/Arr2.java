import java.util.*;
class Arr2
{
	public static void main(String s[])
	{
		int a[][]= new int[3][3];
		Scanner sc=new Scanner(System.in);
		int i,j;
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				a[i][j]=sc.nextInt();
			}
		}
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				System.out.print(a[i][j]);
			}
			System.out.println();
		}
	}
}