import java.io.*;
public class JavaExam
{
	public static void main(String []args) throws Exception
	{
		RandomAccessFile o = new RandomAccessFile("C:\\javapro\\FinalVariable.java","r");
		int n;
		char c;
		while(true)
		{
			n=o.read();
			if(n==-1)
			break;
			System.out.print((char)n);
		}
	}
}