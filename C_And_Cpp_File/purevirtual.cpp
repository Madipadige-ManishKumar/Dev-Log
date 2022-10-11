#include<iostream>
using namespace std;
class a
{
	public :
	virtual dis();
};
class b:public a
{
	public:
	    void dis()
		{
			cout<<"I AM IN D1";
		}
}o;
class c:public b
{
	public:
		void dis()
		{
			cout<<"I AM IN D2";
		}
}o1;
int main()
{
	o.dis();
	o1.dis();
	return 0;
}
