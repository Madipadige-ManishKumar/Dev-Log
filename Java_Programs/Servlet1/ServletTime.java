import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
public class ServletTime extends HttpServlet
{
	public void doGet(HttpServletRequest req ,HttpServletResponse res)throws ServletException,IOException
	{
		res.setContentType("text/html");
		PrintWriter out = res.getWriter();
		String name =req.getParameter("username");
		String pass = req.getParameter("password");
		out.println("Welcome To "+name+"To Our WebPage ");
		out.println("Thankyou for visting ");
	}
}