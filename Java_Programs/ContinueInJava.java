class ContinueInJava
{
	public static void main(String s[])
	{
	out:for(int j=1;j<=100;j++)
		{
			
			for(int i=2;i<=j-1;i++)
			{
				if(j%i==0)
				continue out;
			}
			System.out.println(j);
		}
		System.out.println("ARE THE PRIME NUMBERS ");
	}
}