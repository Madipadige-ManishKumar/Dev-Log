/*This is code is written by Manish  Kumar */
// header section 
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stdlib.h>
using namespace std;
void print(int a);  // function declaration 
void format_specifer()
{
	int a=7;
	printf("%d\a",a);  // audible bell 
	printf("%d\n",a); // next line 
	printf("%d\b",a); // back space 
	printf("%d\r",a); // carriage return 
	// \0 is null charcter which will 
	printf("%d\\",a); // black slah
	printf("%d\f",a); // form feed
	printf("%d'\ ",a); //  single quote 
	printf("%d\v",a); // vertical tab 
	printf("%d'\a'",a); // doublr quote 
	printf("%d\?",a); // question mark
}


/*
Theory{
// storgae class
	Storage location,default value ,life time  according to stroage class 
			storage class 		 storage location 	 default value 		life time 
			auto 					RAM					garbage value 	with in that block 
			extrem					RAM 					0			whole program	
			static 					RAM						0			Within that block
			register 			register 				garbage value	within that block 

//format specifer with it's data type 

	formatspecifer 		data_type
	%d					int
	%f					float
	%lf					longfloat
	%c					char
	%s					string
	%h					short
	%i					decimal,hexadecimal,octal
	%o					octal integer 
	%u					unsigned int 
	%x					hexadecimal 					

// Some Important points of arithemtic operation 
	5.0/2 is not valid 
	in modulud operator  if numarator contains negative sign then the answer will be negative 
// conditional statement 
	 simple  if 
	 if else 
	 else if ladder 
	 switch statment 
// iterative  statement 
	while   // entery control loop 
	dowhile  // exit control loop 
	for // entry control  loop 
// jump statment 
	goto 
	
	
	 
	 
}
*/


void Dynamic_Memory_Allocation(){
	int *ptr;
	// malloc
	ptr=(int*) malloc(3*sizeof(int));  // malloc 
	int i;
	for(i=0;i<3;i++)
	ptr[i]=i;
	ptr=(int*)realloc(ptr,3*sizeof(int));   // realloc
	free(ptr);  // free
	ptr=(int*)calloc(4,sizeof(int)); //calloc 
	free(ptr);  // free      
}

struct My_structure
{
	int a;
	float b;
};
void data_type_use()
{
	int a=23487;  // size 4 bytes in modern computer 
	short s=123;
	float f=3.14f;
	double d=3.1412332;
	char c='m';
	signed int i=-123;
//	unsigned int ui=-123;// this is  invalid
	unsigned int ui=123;
	cout<<a<<s<<f<<d<<c<<i<<ui;
	cout<<endl;
	
	
}
struct operator_C
{
	int a=10,b=20;
	void Arithmetic_operator()
	{
		cout<<a+b;
		cout<<a-b;
		cout<<a*b;
		cout<<a/b;
		cout<<a%b;
	}
	void  relational_operator()
	{
		// relation operator is used to compare two quantities   it is used to condition if the condition is true give 1=True else  0=false 
		cout<<(20>1)<<endl;  
		cout<<(20<30)<<endl;
		cout<<(20>=10)<<endl;
		cout<<(20<=10)<<endl;
		cout<<(20==10)<<endl;
		cout<<(~(20))<<endl;
		cout<<(20>~1)<<endl;
		cout<<(20<~30)<<endl;
	}
	void logical_operator()
	{
		//it is used to compare two relational operator   if  the give condition is true then it will give 1 else 0 
		cout<<(1&&0)<<endl;  // logical and  it will be true only if all condition are true 
		cout<<(1||0)<<endl; //logical or  it will  be true only if one condition is true 
		cout<< "The Logical Not Operator is "<<(!0)<<endl;
	}
	void  assignment_operator()
	{
		int f=0;
		f+=1;
		f-=1;
		f/=1;
		f*=1;
		f%=1;
		// != not equalto operator 
	}
	void inc_or_dec()
	{
		cout<<a++<<endl; //postincrement 
		cout<<++a<<endl; //preincrement 
		cout<<--a<<endl; //predecrement 
		cout<<a--<<endl; //postdecrement  
	}
	void conditional_operator()
	{
		cout<<(1>9?1:0);
		cout<<(1<9?1:0);
	}
	void bitwise_operator()
	{
		int a=10,b=5;
		cout<<(a&b);
		cout<<(a|b);
		//  bitwise !
	}
};



struct Array_and_String
{
	void Array()
	{
		
		// Array is a collection of homogenois data type   in this the elements are accessed by index , it will store the contiously 
		// The index of arrayu start with 0 and ends with n-1 where n = length of array or size of array 
		int a[5];
		cout<<endl<<"The Arrays"<<endl;
		cout<<"Inserting The Values into array";
		int i;
		for(i=0;i<5;i++){
		a[i]=1;
		cout<<a[i]<<"  ";
		}
		cout<<endl;
	
		
	}
	void String()
	{
		// string is nothing but array of charcter 
		// The Declaration below  will end with the terminator  
		char c[]="Manish";
		char d[]="Kumar";
		cout<<sizeof(c)<<endl;
		puts(c);
		
		// methods of String
		cout<<"-----------------------------Methods of String-----------------------------"<<endl;
		cout<<strlen(c)<<endl;
		cout<<sizeof(c)<<endl;
		cout<<strcmp(c,d)<<endl;
		cout<<strcat(c,d)<<endl;
		
		
	}
};


void math_Header_Functions()
{
	int x=90;
	int y=3.1;
	cout<<endl<<"------------------------------------Math_Header_Function ------------------------------------"<<endl;
	cout<<sqrt(x)<<endl;
	cout<<cbrt(x)<<endl;
	cout<<floor(y)<<endl;
	cout<<ceil(y)<<endl;
	cout<<pow(y,x)<<endl;
	cout<<sin(x)<<endl;
	cout<<cos(x)<<endl;
	cout<<tan(x)<<endl;
	
	
	
	
}

int main()  //  main section 
{
	/*     multiple line  comment
		It Will tell concept of C which we have read in 3rd sem.I apologize  if any  concept 
		if i miss .In this i have  used some cpp statments for my convenice .please don't mind 
	
	*/
	//use of data types 
	data_type_use();
	//format specifier use 
	format_specifer();
	// operator  in C
	operator_C op;
	op.Arithmetic_operator();
	op.assignment_operator();
	op.bitwise_operator();
	op.conditional_operator();
	op.inc_or_dec();
	op.logical_operator();
	op.relational_operator();
	// Array and string in C 
	Array_and_String as;
	as.Array();
	as.String();
	
	
	
	
	// Math_Header_Functions
	math_Header_Functions();
	// Structure section   the size of struct = sum of data member's size in struct 
	My_structure obj;
	obj.a=7;
	obj.b=143;
	
	//Dynamic Memory Allocation 
	Dynamic_Memory_Allocation();
	
	
	
	cout<<"The Value of a of obj is ";print(obj.a);
	cout<<"The Value of b of obj is ";print(obj.b);
	float a;
	a=2.0/2.0;
	printf("%f\n",a);
	a=4%-2;
	printf("%d",a);
	cout<<"This is In Cpp"<<a<<endl;
	printf("This is complement of relation operator\n");
	a=((20)>~(30)); // ~ function shortcut -((n)+1)
	cout<<a<<endl;
	char c[100];
	char s[100];
	char c1[100];
	print(10);   // function call 
	cout<<"Enter a First_Name"<<endl;
	gets(c);
	cout<<"Enter The Last Name"<<endl;
	scanf("%[*\n]s",c1);
	cout<<c<<endl;
	cout<<strlen(c)<<endl;
	cout<<strcpy(s,c)<<endl;
	cout<<"String Has Been Copied Sucussfully"<<endl;
	cout<<s<<endl;
	cout<<strcmp(s,c)<<endl;
	cout<<strcat(s,c)<<endl;
	//creating pointer for Struct 
	My_structure *ptr;
	ptr->a=10;
	cout<<(ptr->a)<<endl;
	return 0;
}
void print(int a)  // function defination 
{
	cout<<a<<endl;
}
