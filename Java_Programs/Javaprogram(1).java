import java.sql.*;
import java.util.*;
public class Javaprogram
{
    public static void main(String []args)
    {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1","root","cme123");
            CallableStatement ps=con.prepareCall("call p7(?,?)");
            Scanner sc = new Scanner(System.in);
            int n1;
            System.out.println("Enter Your Id TO Delete ");
            n1=sc.nextInt();
            ps.setInt(1,n1);
            ps.registerOutParameter(2, Types.INTEGER);
            ps.execute();
            int n =ps.getInt(2);
            System.out.println("The Age Is "+n);
            System.out.println("This Program Is Executed by 21001-CS-007");
            con.close();
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
		