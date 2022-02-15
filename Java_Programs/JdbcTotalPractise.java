import java.sql.*;
import java.util.*;
public class JdbcTotalPractise
{	
	public static void main(String []args)
	{
		try{
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1", "root", "cme123");
		Statement st = con.createStatement();
		Scanner sc=  new Scanner(System.in);	
		ResultSet rs;
		String name,pass,sql;
		System.out.println("Enter Name and passwors");
		name =sc.nextLine();
		pass=sc.nextLine();
	
			sql="select * from tab1 where uname='"+name+"'and pword='"+pass+"'";
			System.out.println(sql);
			rs=st.executeQuery(sql);
			
			if(rs.next())
			{
			int n;
			String s,s1;
			n=rs.getInt("AGE");
			s=rs.getString("QUA");
			s1=rs.getString("CUR");
			System.out.println("Your Age Is " + n+"   Your Qulification Is    "+s+"   Your Currently as "+s1);	
			}
}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
}