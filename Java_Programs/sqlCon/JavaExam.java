import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
import java.sql.*;
public class JavaExam extends HttpServlet
{
	public void doPost(HttpServletRequest req ,HttpServletResponse res) throws ServletException,IOException
	{
		res.setContentType("text/html");
		PrintWriter out = res.getWriter();
		try{
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection com =DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
		out.println("Connected ..."+com);
		Statement st = com.createStatement();
		String uname =req.getParameter("name");
		String pword = req.getParameter("password");
		ResultSet rs = st.executeQuery("select *from tab1 where uname= '"+uname+"' and pword= '"+pword+"'");	
		rs.last();
		if(rs.getRow()!=0)
		out.println("You Are an Authenticated User");
		else
		out.println("Data Not Found Please See Your Username and Password ");
		com.close();	
		}
		catch(Exception e){}
		
	}
}
	