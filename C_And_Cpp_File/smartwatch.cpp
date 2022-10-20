#include<iostream>
#include<ctime>
#include<stdlib.h>
using namespace std;
class watch 
{
	int s,d,di,ca,t,h,k;
	public:
	void get()
	{
		cout<<"ENTER NO.OF STEPS \n";
		cin>>s;
	}
	void dis()
	{
		cout<<"THE NO.OF STEPS \n"<<s;;
	}
	void distance()
	{
		d=s/1400;
		
		di=s%1400;
		cout<<"THE DISTANCE YOU TRAVELD IS "<<d<<"."<<di<<"km";
	}
	void calories()
	{
	

		   cout<<endl;
		   ca=(s*0.05);
		   cout<<"\nTHE CALORIES YOU BURNED ARE  "<<ca<<"kilo calories";
		
	}
	void time()
	{   k=s/1400; 
		t=k*12;
		cout<<"\nTHE TIME YOU WALKED "<<t<<"min";
	}
	void timer()
	{
		cout<<"\nENTER COUNDOWN TIME";
		cin>>h;
		h=h*60;
		cout<<"AFTER "<<h<<"secods"<<endl;
		while(h>=0)
		{
		   
		h--;
	//	cout<<h<<endl;	
		}
		cout<<"BUZZ";
	}
	
}o;
int main()
{
/*	o.get();
	o.distance();
	//cout<<endl;
	o.calories();
	o.time();
	o.timer();*/
	int sw,l=0,i=0;
	l=sw=0;
	o.get();
	 time_t tt;
	 struct tm *ti;
    
    // cout<<"current day ,date and time "<<asctime(ti);
				
	do//(sw==1&&sw==2)
	{
		cout<<"\n0-POWER ON \n1-SWIPE RIGHT \n2-SWIPE LEFT\n 3-POWER OFF\n  ";
		cin>>sw;
		if(sw==1)
		{
		   l++;	
		   if(l>4)
		   {
		   	l=0;
		   }
		}
		if(sw==2)
		{
			l--;
			if(l<0)
			{
				l=4;
			}
		}
		if(sw==3)
		exit(1);
		switch(l)
		{
			case 0:
				 time(&tt);
	             ti=localtime(&tt);
	             cout<<asctime(ti);
				//o.dis();
				break ;
			case 1:
				o.dis();
				break;
			case 2:
			    o.distance();
				break;
			case 3:
			    o.calories();
				break;
		
			case 4:
			    o.time();
				break ;
			deafult:
			//	cout<<"\nTHAT'S IT\n";
			   break;
		}
	}while(sw==1||sw==2||sw==0);
}
