#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
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
int  main()
{
    int c;
    do
    {
       printf("\n1-insert\n2-delete\n3-display\n4-sort\n5-search\n6-swap\n7-exit\n");
       scanf("%d",&c);
       switch(c)
       {
	  case 1:ins();break;
	  case 2:del();break;
	  case 3:dis();break;
	  case 4:sort2();break;
	  case 5:search();break;
	  case 6:swap();break;
       }
    }while(c!=7);
    return 0;
}
void ins()
{
    l[i]=(struct node*)malloc(sizeof(struct node));
    printf("ENTER A VALUE \n");
    scanf("%d",&l[i]->x);
    t=l[0];
    l[i-1]->n=l[i];
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


