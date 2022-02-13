import java.util.*;  
class arr   
{  
public static void main(String[] args)  
{  
Scanner sc= new Scanner(System.in);    //System.in is a standard input stream  
//System.out.print("Enter first number- ");  
int []a=new int [5];
int i;
for(i=0;i<5;i++)
a[i]= sc.nextInt();  
for(i=0;i<5;i++)
System.out.print(a[i]+ "  ");
System.out.println("THE SIZE OF ARRAY "+a.length);
}  
} 