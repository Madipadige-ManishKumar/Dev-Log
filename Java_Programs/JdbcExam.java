import java.util.Scanner;
import java.sql.*;
public class JdbcExam
{

	public static void main(String []args)
	{		
		try{
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
		CallableStatement cs = con.prepareCall("CALL P2(?,?)");
		CS.
		con.close();
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
}
