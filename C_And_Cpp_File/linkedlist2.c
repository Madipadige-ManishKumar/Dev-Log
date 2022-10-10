#include<stdio.h>
#include<stdlib.h>
struct node 
{
	int x,no;
	struct node *n;
};
struct node *t=NULL;
struct node *s=NULL;
int nm;
void main()
{
	void ins();
	void del();
	void dis();
	void search();
	void sort();
	void reverse();
	void exit();
	void swap();
	int n;
	while(1)
	{
		printf("\n1-INSERT\n2-DELETE\n3-DISPLAY\n4-SEARCH\n5-SORT\n6-REVERSE\n7-SWAP\n8-EXIT\n");
		scanf("%d",&n);
		switch(n)
		{
			case 1:ins();break;
			case 2:del();break;
			case 3:dis();break;
			case 4:search();break;
			case 5:sort();break;
			case 6:reverse();break;
			case 7:swap();break;
			default:printf("ENTEE THE RIGHT CHIOCE \n");break;
		}
	}
}
void ins()
{
	int n;
	struct node *ptr=(struct node*)malloc(sizeof(struct node));
	if(!ptr)
	{
		
	printf("\nMEMORY IS ALLOCATED\n");
	exit();
	}
	printf("ENTER THE VALUE \n");
	scanf("%d",&n);
	nm++;
	ptr->d=n;
	ptr->no=nm;
	ptr->n=NULL;
	if(s==null)
	{
		s=ptr;
	}
	else
	{
		t=s;
		while(t->n!=NULL)
		t=t->n;
		t->n=ptr;
	}
	printf("\nCOMPLETED\n");
}
void del()
{
	struct node *v;
	if(t!=NULL)
	{
		nm--;
		t=s;
		while(t->n!=NULL)
		{
			v=t;
			t=t->n;
		}
		free(t);
		v->n=NULL;
		printf("COMPLELTED DEL\n");
		else
		printf("THE LIST IS EMPTY");
	}
}
void dis()
{
	t=s;
	if(t!=NULL)
	{
		while(t!=NULL)
		{
			printf("->%sd",t->x);
			t=t->n;
		}
	}
	else
	printf("\nCOMPELETED\n");
}
void search()
{
	int k,f=0;
	t=s;
	if(t!=NULL)
	{
		printf("ENTER THE KEY\n");
		scanf("%d",&k);
	}
	while(t!=NULL)
	{
		if(t->d==k)
		{
			printf("%d data is fund at %d",k,t->no);
			f=1;
			break;
		}
		t=t->n;
	}
}
void sort()
{
	
}
