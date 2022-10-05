#include<iostream>
using namespace std ;
class abc 
{
//	int x;
	public :
	int x;
	void set()
	{
		cout<<"ENTER A VALUE ";
		cin>>x;
	}
	
};
class xyz :public abc
{
	public:
	void dis()
	{
		cout<<"THE ENTERED VALUE IS ="<<x;
	}
}o;
int  main()
{
	o.set();
	o.dis();
	return 0;
}
