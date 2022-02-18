import java.util.*;
public class RandomEx
{
	public static void main(String s[])
	{
		//Random r =new Random();
//		System.out.println(r.nextInt());
		Random random = new Random();
		int [] a = random.ints(5,1,100).toArray();
		for(int i:a)
		System.out.println(i);
	}
}