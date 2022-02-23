import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
public class JavaExam extends HttpServlet
{	
	public void srvice(ServletRequest req,ServletResponse res)	throws ServletException,IOException
	{		
		PrintWriter  out =res.getWriter();
		String name =req.getParameter("name");
		out.println("Your Name Is "+name);
	}
}