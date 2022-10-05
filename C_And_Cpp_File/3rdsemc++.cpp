#include<iostream>
#include<iomanip>
using namespace std;
void add()
{
	cout<<"THE PROGRAM HAS STARTED \n";
}
void add(int i)									//function overloading 
{
	cout<<"\nYOU HAVE ENTERED "<<i<<"VALUES"<<endl;
}
void dis(int a ,int b=0)			//default constructor 
{
	cout<<"\nTHE TWO VALUES \n"<<a<<" "<<b;
}
class a
{
//	add();
	int x;
	public :
	void set()
	{
		cout<<"\n ENTER A VALUE \n";
		cin>>x;
	}
	a add(a o,a o1)
	{
		a o2;
		o2.x=o.x+o1.x;
		return o2;
	}
	void dis()
	{
		cout<<"THE ENTERED VALUE ="<<x<<endl;
	}
	friend void add10(a );
};
class b  //class for constructors 
{	
    int x;
    public:
    b()
    {
    	cout<<"\nHELLO WORLD \n";
	}
	b(int a)
	{
		x=a;
	}
	b(b &o)
	{
		x=o.x;
	}
	void dis()
	{
		cout<<endl<<"THE VALUE="<<x;
	}
	~b()
	{
		cout<<"\nTHE PRG ENDED \n";
	}
	void operator ++()
	{
		cout<<x;
	}
	b operator -(a o2)
	{
		b o3;
		o3=x-o2.x;
		return o3;
	}
	friend operator+(b &o1,b &o2);
	friend operator --(b &o1);
};
void operator +(b &o1, b &o2)
{ 
	cout<<o1.x+o2.x;
}
void operator --(b &o1)
{
	cout<<endl<<o1.x;
}
void add10(a o)
{
	cout<<endl<<"THE VALUE + 10="<<o.x+10;
}
int main()
{
	add();
	a o;//creation of objects 
	int *p;
	int g=1023;
	int &y=g;//reference variable 
	a o2;
	a o1[3];
	int i; 
	for(i=0;i<2;i++)
	o1[i].set();
	for(i=0;i<2;i++)
	o1[i].dis();
	o1[2]=o1[2].add(o1[0],o1[1]);
	o1[2].dis();
	dis(2,3);
	dis(2);
	p=new int;//dynamic allocation 
	*p=10;
	cout<<endl<<*p;
	cout<<endl<<y;
	delete []p;
	add(i);
	cout.width(10);// ios class manipulator 
	cout.fill('$');
	cout<<10;
	cout.precision(3);
	cout<<endl<<21.347687468;
	cout.setf(ios::basefield,ios::hex);
	cout<<endl<<10;
	cout<<setw(10)<<setfill('$')<<23<<endl;//standard manioulator 
	cout<<setbase(8)<<10;
	cout<<ends<<"manish ";
	b p1(34);
	b p2(42);
	b p3(p2);
	//p3=p2;
	p1.dis();
	p2.dis();
	p3.dis();
	return 0;
}
