//linked list
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int j=0;
int i=0;
int k;
void  insert();
void delet();
void dis( );
struct node
{
	int x;
	struct node *a;
}*l[1],*t,*t1;
struct node *s=NULL;
void main()
{
	int m,n,c;
	do
	{
		printf("\n1-insert\n2-dele\n3-display\n4-exit\n5-search");
		scanf("%d",&c);
		switch(c)
		{
			case 1:
			insert();
			break;
			case 2:
			delet();
			break;
			case 3:
			dis();
			break;
			
		}

	
	}while(c!=4);
	   
}
void insert()
{

	l[i]=(struct node*)malloc(sizeof(struct node));
			printf("ENTER A VALUE \n");
			scanf("%d",&l[i]->x);
			if(i==0)
			{
				l[i]->a=NULL;	
			}
			if(i>=1)
			{
				l[i-1]->a=l[i];
			}
			l[i]->a=NULL;
			i++;
		
}
 void  delet()
{
	i--;
    l[--i]->a=NULL;
    
     
}
void dis()
{
	
	t=l[j];
	printf("START");
	while(t!=NULL)
	{
	    printf("->%d",t->x);
		t=t->a;	
	}	
}


