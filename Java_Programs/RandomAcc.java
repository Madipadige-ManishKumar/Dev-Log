import java.io.*;
class RanAc
{
	public static void main(String s[]) throws Exception
	{
		
        RandomAccessFile fr = new RandomAccessFile("C:\\javapro\\id.txt","r");
	int i;
              int []a = new int [100];
              int []f = new int [100];
	for(i=0;i<100;i++)
	{
		a[i]=0;
		f[i]=0;
	}
              int c=1,x=0,y=0;
              fr.seek(0);
              while(true)
              {
                      int   ch=fr.read();
		char ch1 =(char) ch;
		System.out.print(ch1);
                  if(ch==-1)
                      break;
	else if(ch1=='\n')
	c++;
                  else  if (ch1== '{') {
                          a[x] = c;
                          x++;
                      }
		
                      
                      else if (ch1== '}') {
                          f[y] = c;
                          y++;
                      }
                  else {}
              }

	y--;
/*	for(i=0;i<x;i++)
	{
		System.out.println("THE OPENING BRACKET IS "+a[i]);
		System.out.println("THE CLOSING BRACKET IS "+f[y]);
		y--;
		if(y<0)
		break;
	}	*/
System.out.println("A CLASS");
for(i=0;i<x;i++)
System.out.print(a[i]+" ");
System.out.println(" B CLASS");
for(i=0;i<x;i++)
System.out.print(f[i]+" ");

}}