import java.sql.*;
 class JavaJdbcEx
{
    public static void main(String[] args) {
        try{
        String url="jdbc:mysql://localhost/db1";
        String username ="root";
        String password="cme123";


            Connection connection= DriverManager.getConnection(url,username,password);
		System.out.println("The Connection Is Established");
		
            Statement statement =connection.createStatement();
		ResultSet rs =statement.executeQuery("select *from t1");
		while(rs.next())
		System.out.println(rs.getInt(1)+ " "+rs.getInt(2));
            connection.close();



        }
        catch(Exception e)
        {
//		System.out.println("Hi");
//            System.out.println(e);
        }
    }
}
