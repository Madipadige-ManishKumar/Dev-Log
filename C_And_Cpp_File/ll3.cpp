//linked list
#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
void print(struct node *p);

struct node
{
   int x;
   struct node *n;
}*s[1];
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
} */
int  main()
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

      s[i]=(struct node*)malloc(sizeof(s));
      printf("enter a value \n");
      scanf("%d",&s[i]->x);

	if(i==0)
	s[i]->n=NULL;
      if(i>=1)
      s[i-1]->n=s[i];
  //   if(s[i+1]->x==NULL)
      s[i]->n=NULL;
      i++;
      break;

     case 2:
     j=--i;
     if(j==0)
	s[0]=0;


     s[j-1]->n=NULL;
     break;

      case 3:
   //  print(s[0]);
   printf("start");
   u=0;
   while(s[u]!=NULL)
   {
      printf("->%d",s[u]->x);
      s[u]=s[u]->n;
   //   u++;
   }
      break;

   }
   }while(c!=4);
   printf("\npress any key to exit\n");
   //getch();
   return 0;
}
