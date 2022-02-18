import java.util.*;
public class pro
{  static int[] reverse(int a[], int n)
	{
		int[] b = new int[n];
	
		int j = n;
		for (int i = 0; i < n; i++) {
			b[j - 1] = a[i];
			j = j - 1;
		}

		// printing the reversed array
		return b;
		
	}
    public static void main(String args[]){
int t=0;
        int []a =new int [100];
        int []er =new int [100];
        int []ex =new int [100];
        int index[]=new int [10];
        int index1[]=new int [10];
        int []c =new int [100];
        int []d =new int [100];
        int []b=new int [100];
        int []e=new int [100];
        	String ch="abcdefghijklmnopqrstuvwxyz";
		String s;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER THE STRING ");
		s=sc.nextLine();
		int num,k,y=0,j,i,x=0;
		System.out.println("ENTER THE NUMBER ");
		num=sc.nextInt();
		for (i=0;i<s.length();i++)
		{	y=0;k=1;
			for(j=0;j<ch.length();j++)
			{
				if(s.charAt(i)==ch.charAt(j))
				{
					y=1;
					break;
				}
				k++;
			}
			if(y==1)
			{
				a[x]=k;
					x++;}
			else{
				a[x]=30;
				x++;}
		}
		int f=x;
		 i=0;
		 x=0;
		 int u,v;
		    for(i=0;i<f;i++)
		    {
		            if(a[i]==30){
		                b[x]=a[i];
		                x++;
		            }
				else{
		             u=a[i]%10;
		             v=a[i]/10;
		            b[x]=u;
		            c[x]=v;
		            x++;}
		      
		    		}
		    f=x;
		    x=0;
		    for(i=0;i<f;i++)
		    {
		        if(c[i]==0)
		        {
				er[x]=b[i];
		            x++;
		        }
		        else if(b[i]==30)
		        {
		              er[x]=c[i];
		            x++;
		        }
		        else
		        {
 						er[x]=c[i];
		            x++;
		            er[x]=b[i];
		            x++;
		        }
		    }
			index[0]=0;
			int q=1;
			for(i=0;i<x;i++)
			{
				if(er[i]==30)
				{index1[q]=i+1;q++;}
			}
				
int si=x;
		  index[0]=0;
		  f=0;
		  for(i=0;i<x;i++)
		  {
		      if(a[i]==30)
		      {
		           f++;
		          index[f]=(i+1);
		         
		      }
		  }
int h=f;
        u=0;
        while(num>0)
        {
            v=num%10;
            d[u]=v;
            num=num/10;;
            u++;
        }
		f=0;
		int w=0;
		int i1=0;
	e=reverse(d,u);
		for(i=0;i<u;i++)
		ex[i]=e[i];
		out:while(true)
		{	w=0;
			for(i=0;i<c.length;i++)
			c[i]=0;
			for(i=index1[f];i<si;i++)
			{
				c[w]=er[i];
		  		if(er[i+1]==30)
				break;
				if(c[w]!=0)
				w++;
			}
			if(Arrays.equals(c,ex))
			{
				for(i=index[f];i<x;i++)
				{
					if(a[i]==30)
						break out;
					t=a[i];
					System.out.print(ch.charAt(t-1)+" ");
				}
			}
			if(f>q)
			{
				System.out.println("NOT FOUND");
				break out;
			}
			
			f++;	

		}
    }
}