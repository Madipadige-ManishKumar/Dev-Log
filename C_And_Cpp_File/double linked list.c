#include<stdio.h>
#include<stdlib.h>
struct node
{
	int x;
	struct node *p;
	struct node *q;
}*l[1],*t,*k;
struct node *s=NULL;
int main()
{
	int i,c,j,u;
   //clrscr();
   i=0;
   do
   {
      printf("\n1-inse\n2-dele\n3-displ\n4-exit\n" );
       scanf("%d",&c);
      switch(c)
     { 
   	     case 1:
   	     	l[i]=(struct node*)malloc(sizeof(struct node));
   	     	printf("\nENTER A VALUE \n");
   	     	scanf("%d",&l[i]->x);
   		   if(i==0)
   		  {
   			t=s=l[0];
   			l[0]->p=NULL;
		  }
		  if(i>=1)
		  {
		  	l[i-1]->q=l[i];
		  	l[i]->p=l[i-1];
		  }
		  l[i]->q=NULL;
		  i++;
		  break ;
		  case 2:
		  	j=--i;
		  	l[j-1]->q=NULL;
		  	l[j]->p=NULL;
		  	break;
		case 3:
			k=l[i-1];
		   while(k!=NULL)	
		   {
		   	printf("->%d",k->x);
		   	k=k->p;
		   }
		   break;
       } 
    }while(c!=4);
	return 0;
}
