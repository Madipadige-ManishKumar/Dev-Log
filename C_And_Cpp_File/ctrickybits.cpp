#include<stdio.h>
int main(){
	
//int a = 5, b = 3, c = 7;
//printf("%d\n", a & b | c);



//int a = 5, b = 3, c = 7;
//printf("%d\n", a * b + c / 2);

//int a = 5, b = 3;
//a = a + b * 2;
//b = b + a / 2;
//printf("%d %d\n", a, b);


//float x = 0.1;
//if (x == 0.1)
//    printf("Equal\n");
//else
//    printf("Not Equal\n");


//int a = 1, b = 2;
//printf("%d\n", a << b);


//int a = 5, b = 3, c = 7;
//printf("%d\n", (a++) * (b--) / (c++)); 


//int a = 7, b = 3;
//printf("%d\n", a & ~b);


//********
//int x = 5;
//x = x++;
//printf("%d\n", x);


//int a = 5, b = 7;
//a = a++ + ++b;
//printf("%d %d\n", a, b);


//int a = 5, b = 3;
//printf("%d\n", a > 3 && a < b);


//int x = 5, y = 10;
//int z = x > 7 ? x : y > 7 ? y : x + y;
//printf("%d\n", z);
	
	
//int a = 5, b = 3;
//printf("%d\n", (a | b) & ~(a & b)); 


//int a = 5, b = 3;
//int *ptr1 = &a, *ptr2 = &b;
//printf("%d\n", *ptr1 + *ptr2);


//int a = 5, b = 3, c = 7;
//int x = (a > b) ? (a > c) ? a : c : (b > c) ? b : c;
//printf("%d\n", x);



//int a = 5, b = 3;
//int result = a && b++;
//printf("%d %d\n", result, b);


//int a = 5;
//int b = a + a++;
//printf("%d\n", b);



//int a = 5, b = 5;
//printf("%d %d\n", a--, --b);


//****
//int x = 5;
//printf("%d %d %d\n", x++, x++, x++);





//int a = 5;
//int b = a++ + a++ + a++;
//printf("%d\n", b);




//int a = 5, b = 3;
//int result = a || b++;
//printf("%d %d\n", result, b);


//int x = 5;
//printf("%d\n", sizeof(x++));


int a = 5, b = 3;
int result = a && b-- || a++ || b++;
printf("%d %d\n", result, b);


	return 0;
	
}
