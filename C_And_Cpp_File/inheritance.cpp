#include<iostream>
using namespace std ;
class a
{
	public:
	int r;
	int s;
}o3;
class b:public a
{
	public :
	char c[30];
}o1;
class c:public b
{
	public:
	float m;
	void set()
	{
		cout<<"ENTER THE CLASS \n";
		cin>>o3.s;
		cout<<"ENTER THE NAME ";
		cin>>o1.c;
		cout<<"\nENTER THE ROLLNO ";
		cin>>o3.r;
		cout<<"\nENTER THE MARKS";
		cin>>m;
		
	}
}o;
class d:public c,public b
{
	public:
	void dis()
	{
		cout<<o1.c<<" "<<o3.r<<" "<<o.m<<"  ";
	    cout<<o3.s;	
	}
}o2;
int  main()
{
	o.set();
	o2.dis();
	return 0;
}
