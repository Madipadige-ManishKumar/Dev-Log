import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

class TodoApp extends Frame implements ActionListener
{
    Button b1,b2,b3,b5,b4,b6,b7;
    GridBagConstraints gb;

    ArrayList<Button> bu = new ArrayList<Button>();
    ArrayList<Label> la = new ArrayList<Label>();
    GridBagLayout g;
    Label l1;
    TextField t1,t2,t3,t4,t5,t6;
    public void Start()
    {

        removeAll();
        g=new GridBagLayout();
        gb= new GridBagConstraints();
        setLayout(g);
        setSize(500,500);
        setVisible(true);
        t1 = new TextField(20);
        gb.gridx=0;
        gb.gridy=0;
        add(t1,gb);

        t2 = new TextField(20);
        gb.gridx=0;
        gb.gridy=1;
        add(t2,gb);



        b1 = new Button("Login in");
        gb.gridx=0;
        gb.gridy=2;
        gb.gridwidth=1;
        gb.fill= GridBagConstraints.HORIZONTAL;
        add(b1,gb);


        b2 = new Button("Register ");
        gb.gridx=0;
        gb.gridy=3;
        gb.gridwidth=1;
        gb.fill= GridBagConstraints.HORIZONTAL;
        add(b2,gb);

        b1.addActionListener(this);
        b2.addActionListener(this);


    }

    public static void main(String[] args) {
        TodoApp o = new TodoApp();
        o.Start();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==b4)
        {
                String s,s1 = null,s2=null;
                s=t6.getText();
                try
                {
                    for(int i2 = 0;i2<la.size();i2++)
                    {
                        remove(la.get(i2));
                        remove(bu.get(i2));
                    }
                    bu.removeAll(bu);
                    la.removeAll(la);
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1", "root", "cme123");
                    Statement st = con.createStatement();
                    ResultSet rs = st.executeQuery("select * from  Apptable  where  username ='"+t1.getText()+"'and password ='"+t2.getText()+"'");
                    if(rs.next()) {
                        System.out.println("entered");
                        s1 = rs.getString("task");
                    }
                    System.out.println("Exited");
                    s1=s1+","+s;
                    s1="update Apptable set task ='"+s1+"'where username ='"+t1.getText()+"'and password ='"+t2.getText()+"'";
                    System.out.println(s1);
                    st.executeUpdate(s1);

                    StringTokenizer str = new StringTokenizer(s1,",",true);
                    ArrayList <String> st1 = new ArrayList<String>();
                    while(str.hasMoreTokens())
                    {
                        s2=str.nextToken();
                        if(s2.equals(",")){}
                        else {
                            st1.add(s2);
                        }
                    }
                    int i=2,x=0;
                    for(i=2;i<(st1.size()+2);i++,x++)
                    {
                        gb.gridy=i;
                        gb.gridx=0;
                        s1=st1.get(x);
                        System.out.println(s1);
                        Label l2 = new Label(s2);
                        System.out.println(l2);
                        la.add(l2);
                        add(la.get(x),gb);
                        Button bt = new Button("done");
                        bu.add(bt);
                        gb.gridy=i;
                        gb.gridx=1;
                        add(bu.get(x),gb);
                    }
                    for(i=0;i<bu.size();i++)
                    {
                        bu.get(i).addActionListener(this);
                    }
                    con.close();
                    st.close();
                }
                catch (Exception e1)
                {
                    System.out.println(e1.getMessage());
                }

        }
        if(e.getSource()==b2)
        {
            removeAll();
            t3 = new TextField(20);
            gb.gridx=0;
            gb.gridy=0;
            add(t3,gb);

            t4 = new TextField(20);
            gb.gridx=0;
            gb.gridy=1;
            add(t4,gb);

            t4.setEchoChar('*');

            b3 = new Button("Register");
            gb.gridx=0;
            gb.gridy=3;
            gb.gridwidth=1;
            gb.fill= GridBagConstraints.HORIZONTAL;
            add(b3,gb);
            if(t3.getText().equals(t4.getText()))
                b3.addActionListener(this);
            else
            {
                l1 = new Label("Password Not Matched");
                gb.gridx=0;
                gb.gridy=6;
                add(l1,gb);
            }

        }
        if(e.getSource()==b3)
        {
            try {

                Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1", "root", "cme123");
                PreparedStatement ps = con.prepareStatement("insert into Apptable value(?,?,?,?,?)");
                String s1,s;
                s= t3.getText();
                s1=t4.getText();
                ps.setString(1,s);
                ps.setString(2,s1);
                ps.setString(3,null);
                ps.setString(4,null);
                ps.setInt(5,5);
                System.out.println(ps);
                ps.executeUpdate();
                ps.close();
                con.close();
                Start();
            }
            catch (Exception e1)
            {
                System.out.println(e1.getMessage());
            }
        }
        if(e.getSource()==b1)
        {
            removeAll();
            try {
                String s, s1, s2;
                s = t1.getText();
                s1 = t2.getText();
                s2="select * from AppTable where username= '"+s+"' and password ='"+s1 +"'";
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1", "root", "cme123");
                PreparedStatement ps = con.prepareStatement(s2);
                System.out.println(s2);
                ResultSet rs = ps.executeQuery();
                b5 = new Button("Home");
                gb.gridx=2;
                gb.gridy=0;
                add(b5,gb);
                if(rs.next()) {
                    String g;
                    g=rs.getString("task");
                    StringTokenizer str = new StringTokenizer(g,",",true);
                    ArrayList <String> st = new ArrayList<String>();
                    while(str.hasMoreTokens())
                    {
                        g=str.nextToken();
                        if(g.equals("")||g.equals(",")){}
                        else {
                            st.add(g);
                        }
                    }
                    System.out.println(st);
                    t6 = new TextField(20);
                    gb.gridx = 0;
                    gb.gridy = 0;
                    add(t6, gb);
                    b4= new Button("Add Task");
                    gb.gridx=1;
                    gb.gridy=0;
                    add(b4,gb);
                    b4.addActionListener(this);
                    int i=2,x=0;
                    for(i=2;i<(st.size()+2);i++,x++)
                    {
                        gb.gridy=i;
                        gb.gridx=0;
                        g=st.get(x);
                        System.out.println(g);
                        Label l2 = new Label(g);
                        System.out.println(l2);
                        la.add(l2);
                        add(la.get(x),gb);
                        Button bt = new Button("done");
                        bu.add(bt);
                        gb.gridy=i;
                        gb.gridx=1;
                        add(bu.get(x),gb);

                    }
                    for(i=0;i<bu.size();i++)
                    {
                        bu.get(i).addActionListener(this);
                    }
                    con.close();
                    ps.close();
                }

                }
            catch (Exception e1)
            {
                System.out.println(e1.getMessage());
            }

        }
        int i1=0;
        for( i1=0;i1<bu.size();i1++)
        {
            if(e.getSource()==bu.get(i1))
            {
                System.out.println(e.getSource());
                try {
                    remove(la.get(i1));
                    remove(bu.get(i1));
                    la.remove(i1);
                    bu.remove(i1);
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost/db1", "root", "cme123");
                    Statement st = con.createStatement();
                    String s="",s1;
                    for(int j=0;j<la.size();j++)
                    {
                        s1=la.get(j).getText();
                        s=s+s1+",";
                        System.out.println(s);
                    }
                    s1="Update  apptable  set task='"+s+"' where username='"+t1.getText()+"' and password ='"+t2.getText()+"'";
                    st.executeUpdate(s1);
                }
                catch (Exception e1)
                {
                    System.out.println(e1.getMessage());
                }

            }
        }

    }
}
