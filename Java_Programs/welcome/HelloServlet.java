import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
public class HelloServlet  extends HttpServlet
{
	public void service(ServletRequest req,ServletResponse res) throws ServletException,IOException 
	{
		res.setContentType("text/html");
		PrintWriter out = res.getWriter();		
		out.println("Welcome to Madipadige Tejaswi");
		out.println("And Madipadige Manish Kumar");
	}
}