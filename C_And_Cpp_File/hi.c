#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
struct node
{
   int x;
   struct node *a;
}*l[1],*t,*u;
struct node  *s=NULL;

int main()
{
    int i=0,j,c;
  //  clrscr();
    do 
   {
   	    printf("\n1-inse\n2-dele\n3-displ\n4-exit\n" );
        scanf("%d",&c);
        switch (c)
      {
       case 1:  
       l[i]=(struct node*)malloc(sizeof(struct node ));
       printf("ENTER A VALUE \n");
       scanf("%d",&l[i]->x);
       if(i==0)
       {
	  s=l[i];
	  //t=s;
	  l[i]->a=NULL;
       }
       if(i>0)
       {
	  l[i-1]->a=l[i];
	   l[i]->a=NULL;

       }
     //  l[i]=NULL;
       i++;
       break;
      
	case 3:		    
	t=s;
    printf("start");
    printf("-> %d ",l[0]->x);
    while(t!='\0')
    {
       //	printf("start");
	printf("->%d",t->x);
	t=t->a;
	break;
    }
}

    }while(c!=4);                         
    //getch();
   // return 0;
}/*
//linked list
#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
//void print(struct node *p);

struct node
{
   int x;
   struct node *a;
}*l[1],*t;
struct node *s=NULL;
/*
void print(struct node *p)
{
   printf("start");
   i=0;
   while(p!=0)
   {
      printf("->%d",s[i]->x);
      p=p->n;
      i++;
   }
} 
int main()
{
   int i,c,j,u;
  // clrscr();
   i=0;
   do
   {
   printf("\n1-inse\n2-dele\n3-displ\n4-exit\n" );
   scanf("%d",&c);
   switch (c)
   {
      case 1:

     l[i]=(struct node*)malloc(sizeof(struct node ));
       printf("ENTER A VALUE \n");
       scanf("%d",&l[i]->x);
       if(i==0)
       {
	  s=l[i];
	  t=s;
	  l[i]->a=NULL;
       }
       if(i>0)
       {
	  l[i-1]->a=l[i];
	   l[i]->a=NULL;

       }
     //  l[i]=NULL;
       i++;
    
      break;

     case 2:
     j=--i;
     if(j==0)
	l[0]=0;


     l[j-1]->a=NULL;
     break;

      case 3:
      	printf("start");
   // printf("-> %d ",l[0]->x);
    while(t!='\0')
    {
       //	printf("start");
	printf("->%d",t->x);
	t=t->a;

    }     
  
      break;

   }
   }while(c!=4);
   printf("\npress any key to exit\n");
   //getch();
   return 0;
}*/
