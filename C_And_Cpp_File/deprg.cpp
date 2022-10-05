#include<iostream>
using namespace std;

class atomsphere
{
	public:
	
	virtual void set()=0;	
	
	atomsphere()
	{
		cout<<"I am The Construtor Of atomsphere "<<endl;
	}
	~atomsphere()
	{
		cout<<"I am The Destructor Of atomsphere"<<endl;
	}
	virtual void dis()
	{
		cout<<"This is  The atomsphere"<<endl;
	}
	
};
class air
{
	
	public:
	int a;
	air()
	{
		cout<<"I am The Construtor Of Air "<<endl;
	}
	~air()
	{
		cout<<"I am The Destructor Of Air"<<endl;
	}
	
};
class N2:public air  			// Single inheritance 
{
	public:
	N2()
	{
		cout<<"I am The Consturtor of N2"<<endl;
	}
	~N2()
	{
		cout<<"I am The destructor of N2"<<endl;
	}
};
class oxygen: protected N2  // multi level inheritence
{
	public:
	oxygen()
	{
		cout<<"I am The Construtor Of oxygen "<<endl;
	}
	~oxygen()
	{
		cout<<"I am The Destructor Of oxygen"<<endl;
	}
	
};
class smoke:/*private*/ public air,public atomsphere  // multiple inheritance , Hichercal or tree inheritance  
// because the  N2 and air are inheritaned so it is tree inheritance 
{
	public:
	void set()
	{
		cout<<"In The Smoke Class The Values Are Set"<<endl;
	}
	smoke()
	{
		a=7;
		cout<<"I am The Construtor Of smoke "<<endl;
	}
	~smoke()
	{
		cout<<"I am The Destructor Of smoke"<<endl;
	}
	
	
	void dis()
	{
		cout<<"This is smoke class "<<endl;
	}

	
};

/*  Complete is known as the hybrid inhertance */
int main()
{
	air o;
	N2 o1;
	oxygen o2;	
	smoke s1;
	atomsphere *at1;
	at1=&s1;
	at1->dis();
	at1->set();	
	return 0;
}
