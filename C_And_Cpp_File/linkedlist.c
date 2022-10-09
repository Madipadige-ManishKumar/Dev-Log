//linked list
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int j=0;
int i=0;
void  insert();
void delet();
void dis( );
void search();
void reverse();
void swap();
void sort2();
struct node
{
	int x;
	struct node *a;
}*l[1],*t;
struct node *s=NULL;
void main()
{
	int m,n,c;
	do
	{
		printf("\n1-insert\n2-dele\n3-display\n4-exit\n5-search\n6-sort\n7-swap\n8-reverse\n");
		scanf("%d",&c);
		switch(c)
		{
			case 1:
			insert();
			break;
			case 2:
				//j=0;
			delet();
			break;
			case 3:
			dis();
			break;
			case 5:
			search();
			break;
			case 6:
			sort2();
			break;
			case 7:
			swap();
			break;
		/*	case 8:
			reverse();
			break;*/
		
		
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
				t=s=l[j];
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

	t=l[j];
	t=t->a;
	j++;

     
}
void dis()
{
	
	t=l[j];
	printf("START");
	while(t!=NULL)
	{
	    printf("->%d",t->x);
		t=t->a;	
			  //u++;
	}	
}
void search()
{
	int k;
	printf("ENTER THE KEY ELEMENT \n");
	scanf("%d",&k);
		t=l[j];
	while(t!=NULL)
	{
	    if(k==t->x)
	    {
	    	 printf("\n%d IS FOUND AT %d",k,i);
	    	 break;
		}
	   
		t=t->a;	  
	}	
	if(t==NULL)
	printf("\nELEMENT NOT FOUND \n");
}
void sort2()
{
	int g;
	int y;
	int d;
	int *a;
	a=(int*)malloc(i*sizeof(int));
	t=l[j];
	for(y=0;y<i;y++)
	{
		a[y]=t->x;
		t=t->a;
	}
	for(y=0;y<i;y++)
	{
		for(d=y+1;d<i;d++)
		{
			if(a[y]>a[d])
			{
				g=a[y];
				a[y]=a[d];
				a[d]=g;
			}
		}
	}
	t=l[j];
	for(y=0;y<i;y++)
	{
		t->x=a[y];
		t=t->a;
	}
	
}
void swap()
{
	int g,d;
	int x,y;
	int e,r;
	int s=--i;
	printf("ENTER THE NODE NUMBERs \n");
	scanf("%d %d",&g,&d);
    int z;
    g=g-1;
    d=d-1;
    x=l[g]->x;
    y=l[d]->x;
	z=x;
	x=y;
	y=z;
	l[g]->x=x;
	l[d]->x=y;
	
	
}
/*void reverse()
{
	int *a;
	int y=0;
	a=(int *)malloc(i*sizeof(int));
	t=l[j];
	while(t!=NULL)
	{
		a[y]=t->a;
		t=t->a;
	}
	printf("%d",a[0]);
}*/
