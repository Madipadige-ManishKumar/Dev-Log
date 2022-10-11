#include<stdio.h>
int main()
{
	int q[5],f,r;
	int e,c,i=-1;
	f=r=-1;
	do
	{
		printf("\n1-INSERT\n2-DELETE\n3-DISPLAY \n4-EXIT\n");
		scanf("%d",&c);
		switch(c)
		{
			case 1:
				if(r==4)
				printf("OVERFLOW\n");
				else
				{
					printf("ENTER A VALUE \n");
					scanf("%d",&e);
					r++;
					q[r]=e;
				}
				if(f==-1)
				f++;
				break;
				case 2:
					if(f==-1)
					printf("UNDERFLOW \n");
					else
					{
						e=q[f];
						f++;
						if(f>r)
						{
							e=q[f];
						    f=-1;
						}
					}
					break;
				case 3:
					if(f==-1)
					printf("UNDERFLOW\n");
					else 
					{
						for(i=f;i<=r;i++)
						{
							printf("%d  ",q[i]);
					    }
					    if(i>r)
					    {
					    //	printf("%d ",);
					    	i=-1;
						}
				
					}
					break;
		}
	}while(c!=4);
	return 0;
}
