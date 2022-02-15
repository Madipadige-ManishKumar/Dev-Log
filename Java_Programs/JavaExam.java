import java.sql.*;
public class JavaExam
{
	public static void main(String []args)
	{
		try{
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
		System.out.println(con);	
		CallableStatement  ps = con.prepareCall("call p4(?,?)");
		ps.setInt(1,5);
		ps.setInt(2,19);
		ps.execute();
		
		}
		catch(Exception e){
			System.out.println(e.getMessage());
		}
	}
}