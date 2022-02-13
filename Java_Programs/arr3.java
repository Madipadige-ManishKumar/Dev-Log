class arr3
{
	public static void main(String s[])
	{
		int arr[][]=new int  [3][];
		arr[0]=new int [5];
		for(int i=0;i<arr.length;i++)
		{
			for(int j=0;j<arr[i].length;j++)
			{
				System.out.println(arr[i][j]);
			}
		}
	}
}