import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
public class ProgramFile extends HttpServlet
{

	public void doGet(HttpServletRequest req ,HttpServletResponse res) throws ServletException,IOException
	{
		String s;
		s=req.getParameter("name");
		PrintWriter out= res.getWriter();	
		s="Welcome "+s+"To The Website ";
		out.println("<h1>" +s+"</h1>");
	}
}
		