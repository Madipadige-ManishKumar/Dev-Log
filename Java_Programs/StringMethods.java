class StringMethods 
{	
	public static void main(String s[])
	{
		String a="*";
		String  b="/";
		String d="manish kumar ";
		String c= a.concat(b);
		System.out.println(c);
		System.out.println(a);
		System.out.println(a.endsWith("h"));
		System.out.println(a.startsWith("h"));
		System.out.println(b.compareTo(a));
		System.out.println(d.indexOf("a"));
		System.out.println(d.indexOf("a",3));
//		System.out.println(a.EqualIgonre(b));
		System.out.println(d.isEmpty() );
//		System.out.println(d.lastindexOf("s"));
		System.out.println(d.replace ('a','s'));
		System.out.println(d.substring(2));
		System.out.println(d.substring(2,10));
		System.out.println(d.trim());
	}
}