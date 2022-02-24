import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
public class JavaServletEx extends HttpServlet
{
		public void  service(ServletRequest req,ServletResponse res) throws ServletException,IOException
		{
			PrintWriter out= res.getWriter();
			out.println("<h1> Welcome Manish</h1>");		
		}
}