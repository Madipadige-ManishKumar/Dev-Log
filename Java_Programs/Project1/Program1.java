import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
import java.sql.*;
public class Program1 extends HttpServlet
{
	public static  String s,s1,g;
	public void service(ServletRequest req,ServletResponse res) throws ServletException,IOException 
	{
		res.setContentType("text/html");
		PrintWriter out = res.getWriter();		
		s=req.getParameter("txt");
		s1=req.getParameter("txt1");
		Method1();
		out.println(g);
	}

	public void Method1(){
		try{
		String d2;
		Connection con =DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
//		d2="select *from tab1 where uname="+s+"pword="+s1+";";
		int a;
		String q,c,g;
		Statement st =con.createStatement();
		ResultSet rs = st.executeQuery("select *from tab1");
		while(rs.next())
		{
			a=rs.getInt("age");
			q=rs.getString("Qua");
			c=rs.getString("CUR");
			System.out.println(a+" "+q+" "+c);
			g="Your Age = "+a+ " Your Qualificatio Is = "+q+" The Currently You Are Doing "+c; 
		}
		}
		catch(Exception e)
		{}
	}
}