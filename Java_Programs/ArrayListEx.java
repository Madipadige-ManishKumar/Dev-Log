import java.util.*;
class ArrayListEx
{
	public static void main(String s[])
	{
		ArrayList<Integer> a = new ArrayList<Integer>();
		ArrayList<Integer> b = new ArrayList<Integer>(5);
		ArrayList<Integer> c = new ArrayList<Integer>(b);
		System.out.println("THE SIZE OF ARRAY IS "+b.size());
		System.out.println("B"+b);
		b.add(1);// add method
		b.add(2);
		b.add(3);
		b.add(4);
		b.add(5);
		b.add(7);
		b.add(2,6);// add method 2
		System.out.println("B"+b);
		System.out.println("THE SIZE OF ARRAY IS "+b.size());
		System.out.println(b.remove(0));//remove method
		System.out.println("THE SIZE OF ARRAY IS "+b.size());// size method
		System.out.println("B"+b);
		System.out.println("C"+c);
		ArrayList<Integer> d = new ArrayList<Integer>(b);
		System.out.println("D"+d);
		System.out.println(c.addAll(d));//addAll method
		System.out.println("C"+c);
		System.out.println("B"+b);
		System.out.println(" TO CHECK WHETHER THE C ARRAY IS EMPTY OR NOT"+c.isEmpty());// isEmpty // method
		System.out.println("THE ELEMENT IN INDEX 0 IS "+b.get(0));// get method 
		System.out.println("TO CHECK WHAT IS THERE IS  A PARTICULAR INDEX ");
		System.out.println(b.indexOf(2));//indexOf method
//		b.clear();
//		System.out.println("B"+b);
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER A VALUE TO CHECK IN B ARRAY ");
		n=sc.nextInt();
		System.out.println(b.contains(n));// contains method 
//		Collection.sort(b);
		Collections.sort(b);// sort method 
	//	trimTosize();
	//	ensureCapacity();
	}
}