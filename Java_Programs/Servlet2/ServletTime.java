import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.sql.*;
import java.io.*;
public class ServletTime extends HttpServlet
{
	public void doGet(HttpServletRequest req ,HttpServletResponse res)throws ServletException,IOException
	{
		PrintWriter out = res.getWriter();
		try{
		Connection con= DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
		res.setContentType("text/html");
		Statement st = con.createStatement();
		String name =req.getParameter("username");
		String pass = req.getParameter("password");
		String sql;
		sql="select * from tab1 where uname='"+name+"'and pword='"+pass+"'";
		ResultSet rs = st.executeQuery(sql);
		if(rs.next())
		{
			int n;
			String s,s1;
			n=rs.getInt("AGE");
			s=rs.getString("QUA");
			s1=rs.getString("CUR");
			out.println("Your Age Is " + n+"   Your Qulification Is "+s+"Your Currently as "+s1);
		}
		else
		out.println("You Are Not A Proper User");
		out.println("Thankyou for visting ");
		}	

		catch(Exception e){
			out.println(e.getMessage());
		}
	}
}