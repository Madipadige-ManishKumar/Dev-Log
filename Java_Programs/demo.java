import java.sql.*;

class JavaJdbcEx1
{
    public static void main(String[] args) {
        try {
            String url = "jdbc:mysql://localhost/db1";
            String UserName = "root";
            String Password = "cme123";
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection(url,UserName,Password);
            Statement st = connection.createStatement();
            st.executeUpdate("CREATE TABLE T2 (ID INT PRIMARY KEY ,NAME VARCHAR(30))");
            st.executeUpdate("INSERT INTO T2 VALUES(1,'Manish')");
            st.executeUpdate("INSERT INTO T2 VALUES(2,'Kumar')");
            st.executeUpdate("INSERT INTO T2 VALUES(3,'Anil')");
            ResultSet resultSet = st.executeQuery("SELECT *FROM T2");
            while(resultSet.next())
            {
                System.out.println(resultSet.getInt(1)+" "+resultSet.getString(2));
            }
            st.executeUpdate("DROP TABLE T2");
        }
        catch (Exception e)
        {
        }
    }
}