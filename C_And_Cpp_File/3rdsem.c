#include<stdio.h>
#include<stdlib.h>
struct n 
{
	int x;
	struct n *y;
	struct n *f;
	int *u;
}o,*v,o1;
int i=0;
int j=0;
struct node
{
   int x;
   struct node *n;
}*l[1],*t;
struct node *s=NULL;
void ins();
void del();
void dis();
void sort2();
void search();
void swap();
int main()
{
	int k;
	int fg,ty;
	int  q[10],f1,r1;
	int x=43859,*p,**p2;//pointer decalation 
	o.x=10;
	int top=-1;
	int c1;
	o.y=NULL;
	o1.x=2397;
	o.y=&o1;
	o1.f=&o;
	int *b[5];
	int a[5]={1,2,3,4,5},*p1;
	printf("\nPOINTERS\n");
	p=&x;
	printf("%d\n",*p);
	printf("\nARRAY OF POINTER\n");
	int i=0;
	p=a;
    for(i=0;i<5;i++)
    b[i]=&a[i];
	for(i=0;i<5;i++)
	{
		printf("%d\t",*b[i]);
	}
	printf("\nPOINTER INILIZED BY ARRAY \n");
	for(i=0;i<5;i++)
	{
		printf("%d\t",*p);
		p++;
	}
	printf("\nPOINTER ASSIGNED BY STRUCT AS STRUCT VARIABLE  \n");
	v=&o;
	printf("%d",*v);
	printf("\nPOINTER  ASSIGNED AS STRUCT MEMBER \n");
	o.u=&o.x;
	printf("%d",*(o.u));
	printf("\nSELF REFERENTIAL STRUCTURE \n");
	printf("%d",o.y->x);
	printf("\n SELF REFERENTIAL STRUCTTURE \n");
	printf("%d",o1.f->x);
	//CH 2 USING MALLOC CALLOC REALLOC 
	printf("\nCH 2 USING MALLOC,CALLOC AND REALLOC,FREE\n");
	int *g1,*h1;
	printf("\nUSING MALLOC \n");
	g1=(int *)malloc(sizeof(int));
	g1[0]=123;
	printf("%d",g1[0]);
	printf("\nUSING CALLOC \n");
	h1=(int*)calloc(1,sizeof(int));
	h1[0]=43;
	printf("%d",h1[0]);
	printf("\nUSING REALLOC\n");
	h1=(int *)realloc(h1,2*sizeof(int));
	h1[0]=234;
	h1[1]=345;
	printf("%d %d",h1[0],h1[1]);
	free(g1);
	free(h1);
	printf("\n USED FREE\n");
	printf("\nCH 3-SORTING \n");
	int t;
	int arr[100],j;
	int c;
	int n;
	printf("ENTER THE SIZE\n");
	scanf("%d",&n);
	printf("ENTER %d VALUES ",n);
	for(j=0;j<n;j++)
	scanf("%d",&arr[j]);
	do
	{
	
	printf("\n1-BUBBLE SORT\n2-SELECTION SORT\n3-INSERTION SORT \n4-LINEAR SEARCH \n5-LINKED LIST\n6-EXIT\n7- STACK \n8-queue\n");
	scanf("%d",&c);
	switch(c)
	{
		case 1:
			printf("\nBUBBLE SORT\n");
	      //  int n=10;
	 		for(i=0;i<n-1;i++)
			{
				for(j=0;j<n-i-1;j++)
				{
					if(arr[j]>arr[j+1])
					{	
						t=arr[j];
						arr[j]=arr[j+1];
						arr[j+1]=t;
					}
				}
			}
	for(i=0;i<n;i++)
	printf("%d\t",arr[i]);
	break;
	case 2:
		printf("\nSELETION SORT\n");
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{		
				if(arr[i]>arr[j])
				{
					t=arr[i];
					arr[i]=arr[j];
					arr[j]=t;
				}
			}
		printf("%d\t",arr[i]);
		}
		break;
	case  3:
		printf("\nINSERTION SORT \n");
		for(i=1;i<n;i++)
		{
			t=arr[i];
			j=i-1;
			while(t<arr[j]&&j>=0)
			{
				arr[j+1]=arr[j];
				j=j-1;
			}
			arr[j+1]=t;
		}
		for(i=0;i<n;i++)
		printf("%d\t",arr[i]);
		break;
	case 4:             
	//int k;
		printf("ENTER THE KEY \n");
		scanf("%d",&k);
		i=0;
		while(i<10)
		{
			if(k==arr[i])
			{
				printf("\nELEMENT IS FOUNDED \n");
				break;
			}
		   i++;
		}
		if(i==10)
		printf("ELEMENGT NOT FOUNND\n");
		break;
	case 5:
		 do
    	{
    	
       	printf("\n1-insert\n2-delete\n3-display\n4-sort\n5-search\n6-swap\n7-exit\n");
       	scanf("%d",&c1);
       	switch(c1)
       	{
	  	case 1:ins();break;
	  	case 2:del();break;
	  	case 3:dis();break;
	  	case 4:sort2();break;
	  	case 5:search();break;
	  	case 6:swap();break;
       	}
    	}while(c1!=7);
    	break;
	case 7:
		top=-1;
		int s7[10],ele;
		do
		{
			printf("\n1-INSERT\n2-DELETE \n3-display \n4-EXIT\n");
			scanf("%d",&c1);
			switch(c1)
			{
				case 1:
					if(top==9)
					printf("OVERFLOW\n");
					else
					{
						top++;
						printf("ENTER THE VALUE ");
						scanf("%d",&s7[top]);
					}
				break;
				case 2:
					if(top==-1)
					printf("UNDER FLOW \n");
					else 
					{
						top--;
					}
				break;
				case 3:
					for( fg=top;fg>=0;fg--)
					printf("%d\n",s7[fg]);
					break;
			}
		}while(c1!=4);
	break;
		case 8:
			f1=r1=-1;
		do
		{
		
			printf("\n1-INSERT\n2-DELETE \n3-display \n4-EXIT\n");
			scanf("%d",&c1);
			switch(c1)
			{
				case 1:
					if(r1==9)
					printf("OVERFLOW");
					else
					{
						r1++;
						printf("ENTER A VALUE \n");
						scanf("%d",&q[r1]);
					}
					if(f1==-1)
					f1++;
				break;
				case 2:
					f1++;
				break;
				case 3:
					for( ty=f1;f1<=r1;f1++)
					printf("%d\t",q[f1]);
				break;
			}
	    }while(c1!=4);
	}
	//	printf("\nREFER QUICK SORT,MERGE SORT,BINARY SEARCH \n");
}while(c!=6);
	return 0;
}
void ins()
{
   		l[i]=(struct node*)malloc(sizeof(struct node));
		    printf("ENTER A VALUE \n");
			scanf("%d",&l[i]->x);
			if(i==0)
			{
				t=s=l[i];
				l[i]->n=NULL;	
			}
			if(i>=1)
			{
				l[i-1]->n=l[i];
			}
			l[i]->n=NULL;
			i++;
}
void del()
{
   t=l[j];
   j++;
}
void dis()
{
   t=l[j];
   while(t!=NULL)
   {
      printf("->%d",t->x);
      t=t->n;
   }
}
void sort2()
{
  // int h=j;
   int y,z;
   int u=i-1;
   int g;
   int *a;
   t=l[j];
  // int *a;
   a=(int*)malloc(u*sizeof(int));
   for(y=0;y<i;y++)
   {
      a[y]=t->x;
      t=t->n;
   }
   for(y=0;y<i;y++)
   printf("%d",a[y]);
   for(y=0;y<i;y++)
   {
      for(z=y+1;z<i;z++)
      {
	 if(a[y]>a[z])
	 {
	    g=a[y];
	    a[y]=a[z];
	    a[z]=g;
	 }
      }
   }

   for(y=0;y<i;y++)
   printf("%d",a[y]);

   t=l[j];
   for(y=0;y<i;y++)
   {
      t->x=a[y];
      t=t->n;
   }
}
void search()
{
    int k,h=1;
    t=l[j];
   // int h=1;
  //  int k;
    printf("ENTER THE kEY \n");
    scanf("%d",&k);
    while(t!=NULL)
    {
	if(k==t->x)
	{
	   printf("%d IS FOUND IN %d\n",k,h);
	   break;
	}
	t=t->n;
	h++;
    }
    if(t==NULL)
    printf("ELEMENT IS NOT FOUNDED\n");
}
void swap()
{

   int n1,n2;
   struct node *v;
   int e,r;
   int w;
   printf("ENTER THE NODE NUMBER ");
   scanf("%d%d",&n1,&n2);
   n1--;
   n2--;
   v->x=l[n1]->x;
  l[n1]->x=l[n2]->x;
  l[n2]->x=v->x;

}
