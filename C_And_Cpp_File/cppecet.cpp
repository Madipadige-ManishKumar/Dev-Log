/* Created by M Manish Kumar   */
#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
template<class T1,class T2>


class Template_use
{
	public:
		void dis(T1 e,T2 f)
		{
			cout<<"The Addition Of The Both is "<<e+f<<endl;
		}
};
template <class T1>
void print(T1 s)
{
	cout<<s<<endl;
}
class My_class
{
	// default private 
	
	int a;
	public:
		void set(int a)
		{
			this->a=a;
		}
		void get()
		{
			print(a);
		}
		My_class() // default construtor
		{
			print("This is Constructor");
		}
		My_class(int a)	// parameterized construtor 
		{
			print("This is parameterized construtor ");
			this->a=a;
		}
		My_class(My_class &onj)	// copy construtor   & should be passed 
		{
			print("This is copy construtor ");
			this->a=onj.a;
		}
		~My_class()
		{
			print("This is destructor");
		}
		void  operator-()
		{
			print("This is Unary  Operator Overloading With Member Function");
		}
		void operator+(My_class obj)
		{
			print("This is Binary Operator Overloading With Member Function ");
		}
		
		
		void _function(int a);
		friend void display(My_class obj);   // friend 
		friend void operator*(My_class obj);
};
class A
{
	public:
	virtual getdata()
	{
		print("This is GetData Function Of Class A ");
	}
};
class B:public A
{
	public:
	getdata()
	{
		print("This is GetData Function Of Class B ");
	}
};


void operator*(My_class obj)
{
	print("This is a Unary Operator With Friend Function ");
}

/* 
Theroy{
    Inline Function 
    	This function consist of simple functions . This should not consist of looping statments,recusive function and e.t.c
    	The Function in a class are always inline .And The Function which you declare  inside and define outside is called outline funtion 
    	
    Class That do not contain data member and member function are called empty class or stub class 
    	
    Acess specifier in c++
    	Public,Private,Protected
	Friend function 
		Friend Function are The Function which are not a member function but they access  the private data member   of class 
		.This Friend Function can't be called with the object instead we can pass object to it 
		
	- In Cpp The non static function can't access static member 
	-In Cpp The constructor overloading is posiible but not for the destrutor 
	- destrutor can be virtual 
	-Constructor can't be virtual 
    		
    This Pointer 
    	This pointer is used when a variable name of data member of class and passed argument are same then we use this operator 
	Operator Overloading 
		An Unary Operator overloading function needs no argument and  friend function need 1 argument 
		An Binary Oerator overloading fucntion needs 1 argument and friend function need 2 argument     	
}
*/
void My_class::_function(int a)
{
	print(a);
}
void display(My_class obj)
{	print("This is a   friend function");
	print(obj.a);
}

int a=0;  //global variable

// user defined manipulator 
ostream unit(ostream &output)
{
	output<<"inch"<<endl;
}

class atomsphere
{
	public:
	
	
	virtual void set()=0;	  // pure virtual function 
	
	atomsphere()
	{
		cout<<"I am The Construtor Of atomsphere "<<endl;
	}
	~atomsphere()
	{
		cout<<"I am The Destructor Of atomsphere"<<endl;
	}
	virtual void dis()     // virtual function 
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
	friend void fri();
};
void fri()
{
	cout<<"This is Friend Function of air"<<endl;
}
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
class smoke:public air,public atomsphere  // multiple inheritance , Hichercal or tree inheritance  
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
class demo
{
	public:
	int a;
	int id;
	string name;
	demo()
	{
		cout<<"The Object Is created "<<endl<<"If a Class Defines a constructor Then The Default constructor is disabled"<<endl;
	}
	demo(int id,string name){
		this->id=id;
		this->name=name;
	}
	// member function of a class 
	void  display_function(){
		
		cout<<endl<<"--------------------------------\n"<< "This a Member fucntion section \n";
		cout<<"Student details\n";
		cout<<"Id:"<<this->id<<endl;
		cout<<"Name:"<<this->name<<endl;
	}
	
	friend void display_of_a();  // friend function 
};

class manipulator
{
	public:
		void ios_manipulator()
		{
		cout<<"-----------------------------------------"<<endl;
		cout.width(5);
		cout<<"->IOS Manipulator"<<endl;
		cout.width(10);
		cout<<"->This Is Width  function";
		cout.width(10);
		cout<<3<<endl;
		cout<<"This is Presicion function"<<endl;
		cout<<"-> Without presicion"<<endl;
		cout<<3.1401278365125;
		cout.precision(2);
		cout<<endl;
		cout<<"-> Witho presicion"<<endl;
		cout<<3.1401278365125<<endl;
		cout.width(10);		
		cout.fill('$');
		cout<<"Manish"<<endl;
		cout<<endl<<"Flags"<<endl;
		cout.setf(ios::oct,ios::basefield);
		cout<<endl<<"the Octal value of "<<10<<endl;
		}
		void standardmanipulator()
		{
			/* We use standard manipulator to overcome the problem in iosmanipulator 
			  i.e. when you use the ios manipulator then 
			  we can't connect any other thing that's why we use the standard manipulator 
			
			*/
			cout<<"---------------------------------------------------------------"<<endl;
			cout<<"Standard Manipulator in Cpp"<<endl;
			cout<<"This Is setw function "<<setw(10)<<"Manish"<<endl;
			cout<<"This Is Set precision function "<<setprecision(2)<<3.14456789<<endl;
			cout<<"This Is setfill function"<<setw(10)<<setfill('#')<<"Manish"<<endl;
			cout<<"This is setbase Fucntion"<<"The Hexadecimal Value of 10"<<setbase(16)<<10<<endl;
			cout<<"This   setiosflagsfunction"<< setiosflags(ios::showbase)<<setiosflags(ios::hex)<<"The Hexadecimal value of the 10 is"<<10<<endl;
//			cout<<"This Is Whitespace function"<<ws<<"						Manish"<<endl;
			
		}
		
		void File_Manipulation()
		{
			
			
			char name[30];
			int id,i;
			ofstream of;
			of.open("FileOperation_ByCpp.txt",ios::out);
			if(!of)
			{
				cerr<<"Error! Can't Open The File";
			}
			else
			{
				
			
			cout<<"This Is OutputStream Operation On a File"<<endl<<"________________________________________"<<endl;
			cout<<"Enter The Name"<<endl;
			cin>>name;
			cout<<"Enter The Id "<<endl;
			cin>>id;
		 	for(i=0;i<sizeof(name);i++)
		 	{
		 		
		 		// write operation 
		 		of.write((char*)&name[i],sizeof(name[i]));
		 	
			 }
			 id=48+id;
			 // put operation 
			 of.put((char)id);					// Put Operation 
			 
		}
		of.close();
		
		ifstream fin;
		fin.open("FileOperation_ByCpp.txt",ios::in);
		if(!fin)
		{
			cerr<<"file Not Found"<<endl;
		}
		else
		{
			while(fin)
			{
				char c[30];
				cout<<(char)fin.get();  // get function 
//				cin.getline(c,20);   get line function 
				for(i=0;i<sizeof(name);i++){
				
//				fin.read((char*),&name[i],sizeof(name[i]));
//				fin.read((char*),&name[i],sizeof(name[i]));  // read function
				cout<<name[i];
			}				
			}
		}
		}
};
void display_of_a(){
	cout<<a;
}


class con_and_des
{
	public:
	int id,phno;
	//default constructor
	con_and_des()
	{
		// Constructor Are Mainly  used for inilization 
		
		/*
		In The Inheritance The Constructor of a super or base is called first than the child or sub class 
		constructor can have parameter and it can be overloaded 
		*/
		
		cout<<"This Is The Defalut Constructor"<<endl;
	}
	
	//parameteried constructor 
	con_and_des(int id,int phno)
	{
		this->id=id;
		this->phno=phno;
		
		cout<<endl<<"This is parameteried construtor"<<endl;
	}
	
	// copy constructor 
	con_and_des(con_and_des *o)
	{
		id=o->id;
		phno=o->phno;
		cout<<endl<<"This is copy construtor"<<endl;
	}
	
	// destrutor 
	
	~con_and_des()
	{
		
		/*
		In case Of inhertance 
		In Case of destructor first the  sub class or child class obj are destroyed  then the super class  
		destrutor are not having any parameter it is only one for a class
		*/
		// destructor are used to remove or close all of the connection 
	}
};


int  add ()    // add function 1
{
	return (a);
}
// inline function
inline void Its_inline_function()
{
	// This Function should be  very small 
	// In This Inline function there should not be any kind of loop statment  or recurrssive fucntion 
}

// default arguments 

int  add (int a,int b=50,int c=90) // add function   This is function overloading 
{
	return (a+b+c);
}
int main ()
{
	
	// object creation section 
	demo m;
	
	demo  obj1=demo(1,"Manish");
	/*
	The Standard input libaries are 
	std output stream 
	std input stream 
	std endline stream 
	*/
	int n= add();
	cout<<"The Value of n"<<n<<endl;
	cout<<"The Value of A"<<a<< endl;
	
	// Reference variable 
	int  &ref=n;
	cout<<ref;
	ref++;
	cout<<"The Value of N"<<n<<endl;
	
	
	n=add(3);
	cout<<"Calling default function The result is "<<n<<endl;
	
	// dynamic intilization 
	/*
	The Dynamic inilization is done by using new and delete operator 
	syntax as example 
	int a = new int[size]
	*/
	int *ab = new int[5];
	cout<<endl<<"The size of  'a' Which is done by dynamically "<<sizeof(ab);
	
	delete(ab);
	
	int *abc= new int(5);
	cout<<endl<<sizeof(abc);
	
	
	cout<<endl<<"Friend Function";
	//calling of friend fucntion 
	m.a=10;
	display_of_a();
	obj1.display_function();
	
	cout<<endl<<"--------------------------------"<< endl<<"The Manipulator In cpp"<<endl;
	// Manipulators In cpp
	
		// ios manipulator
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////		
		/*
		
		This Is About Manipulator 
		
		
		*/
		
		// user defined manipulator 
	cout<<"This is User defined function"<<15<<unit;
	manipulator  ios1;
	
//	ios1.ios_manipulator();
	ios1.standardmanipulator();
	ios1.File_Manipulation();	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////		
/*


This is Constructor and destructor section
*/

cout<<endl;

con_and_des  o1= new con_and_des();
con_and_des  o2= new con_and_des(7,6302394743);
con_and_des  o3= new con_and_des(o2);

My_class obj21;
	air o10;
	N2 o11;
	oxygen o12;	
	smoke s1;
	atomsphere *at1;
	at1=&s1;
	at1->dis();
	at1->set();
	fri();
	Template_use<int,float>t1;
	t1.dis(3,3.4);
	
	obj21.set(10);
	obj21.get();
	My_class obj3;
	obj3._function(23);
	-obj3;
	obj21+obj3;
	*obj21;
	A a;
	B b;
	A *c;
	c=&a;
	c->getdata();
	c=&b;
	c->getdata();
	
}
