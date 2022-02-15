import java.sql.*;
public  class jdbcEx
{
    public static void main(String[] args)  
	{
        String url="jdbc:mysql//localhost:3306/jdbcdemo";
        String username ="root";
        String password="cme";
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");


            Connection connection= DriverManager.getConnection(url,username,password);


            Statement statement =connection.createStatement();


            ResultSet resultSet = statement.executeQuery("select * from t1");

            while(resultSet.next())
            {
                System.out.println(resultSet.getInt(1)+ " "+ resultSet.getInt(2));
            }

            connection.close();



        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
