import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.Scanner;

class rough extends Frame implements ActionListener {
    GridBagLayout g;
    GridBagConstraints gb;

    Button b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, bc, ba, bs, bm, bd, be;

    String str = "";


    TextField t1;

        rough() {
            g = new GridBagLayout();
            gb = new GridBagConstraints();
            setLayout(g);
            setSize(500, 500);
            setVisible(true);
            t1 = new TextField(10);
            gb.gridx = 0;
            gb.gridy = 0;
            gb.gridwidth = 4;
            gb.fill = GridBagConstraints.HORIZONTAL;
            add(t1, gb);
            b1 = new Button("1");
            gb.gridx = 0;
            gb.gridy = 1;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b1.addActionListener( this);
            add(b1, gb);
            b2 = new Button("2");
            gb.gridx = 1;
            gb.gridy = 1;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b2.addActionListener( this);
            add(b2, gb);
            b3 = new Button("3");
            gb.gridx = 2;
            gb.gridy = 1;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b3.addActionListener((ActionListener) this);
            add(b3, gb);
            ba = new Button("+");
            gb.gridx = 3;
            gb.gridy = 1;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            ba.addActionListener( this);
            add(ba, gb);

            b4 = new Button("4");
            gb.gridx = 0;
            gb.gridy = 2;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b4.addActionListener(this);
            add(b4, gb);
            b5 = new Button("5");
            gb.gridx = 1;
            gb.gridy = 2;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b5.addActionListener( this);
            add(b5, gb);
            b6 = new Button("6");
            gb.gridx = 2;
            gb.gridy = 2;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b6.addActionListener(this);
            add(b6, gb);
            bs = new Button("-");
            gb.gridx = 3;
            gb.gridy = 2;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            bs.addActionListener( this);
            add(bs, gb);

            b7 = new Button("7");
            gb.gridx = 0;
            gb.gridy = 3;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b7.addActionListener( this);
            add(b7, gb);
            b8 = new Button("8");
            gb.gridx = 1;
            gb.gridy = 3;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b8.addActionListener( this);
            add(b8, gb);
            b9 = new Button("9");
            gb.gridx = 2;
            gb.gridy = 3;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b9.addActionListener( this);
            add(b9, gb);
            bm = new Button("*");
            gb.gridx = 3;
            gb.gridy = 3;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            bm.addActionListener(this);
            add(bm, gb);
            b0 = new Button("0");
            gb.gridx = 0;
            gb.gridy = 4;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            b0.addActionListener(this);
            add(b0, gb);
            bc = new Button("c");
            gb.gridx = 1;
            gb.gridy = 4;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            bc.addActionListener(this);
            add(bc, gb);
            be = new Button("=");
            gb.gridx = 2;
            gb.gridy = 4;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            be.addActionListener(this);
            add(be, gb);
            bd = new Button("/");
            gb.gridx = 3;
            gb.gridy = 4;
            gb.gridwidth = 1;
            gb.fill = GridBagConstraints.HORIZONTAL;
            bd.addActionListener(this);
            add(bd, gb);
        }


        public static void main (String[] args){
            rough o = new rough();
        }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == b1) {
            str += "1";
            t1.setText(str);
        }

        if (e.getSource() == b2) {
            str += "2";
            t1.setText(str);
        }

        if (e.getSource() == b3) {
            str += "3";
            t1.setText(str);
        }

        if (e.getSource() == b4) {
            str += "4";
            t1.setText(str);
        }

        if (e.getSource() == b5) {
            str += "5";
            t1.setText(str);
        }

        if (e.getSource() == b6) {
            str += "6";
            t1.setText(str);
        }

        if (e.getSource() == b7) {
            str += "7";
            t1.setText(str);
        }

        if (e.getSource() == b8) {
            str += "8";
            t1.setText(str);
        }

        if (e.getSource() == b9) {
            str += "9";
            t1.setText(str);
        }

        if (e.getSource() == b0) {
            str += "0";
            t1.setText(str);
        }

        if (e.getSource() == ba) {
            str += "+";
            t1.setText(str);
        }

        if (e.getSource() == bs) {
            str += "-";
            t1.setText(str);
        }

        if (e.getSource() == bm) {
            str += "*";
            t1.setText(str);
        }

        if (e.getSource() == bd) {
            str += "/";
            t1.setText(str);
        }

        if (e.getSource() == bc) {
            str = "  ";
            t1.setText(str);
        }
        if (e.getSource() == be) {
            String s;
            Scanner sc = new Scanner(System.in);
            s=sc.nextLine();
            ArrayList o = new ArrayList();
            ArrayList o1 = new ArrayList<Character>();
            ArrayList <Integer>o2 = new ArrayList<Integer>();
            String d="+-*/";
            String s1="";
            int i,j,f=0,n=0,m=0;
            for(i=0;i<s.length();i++)
            {f=0;
                for(j=0;j<d.length();j++)
                {
                    if(s.charAt(i)==d.charAt(j))
                    {
                        if(j<=1){
                            o.add(1);
                            o1.add(s.charAt(i));
                            f=1;
                        }
                        else {
                            o.add(2);
                            o1.add(s.charAt(i));
                            f=1;
                        }

                    }

                }
                if(f!=1) {
                    s1+=s.charAt(i);
                    n=Integer.parseInt(s1);
                    if(i==s.length()-1)
                        o2.add(n);
                }

                else
                {

                    o2.add(n);
                    s1="";
                }


            }
            char c;

            f=0;
            while(o.size()!=0)
            {
                if(o.contains(2))
                {
                    n=o.indexOf(2);
                    c=(char)o1.get(n);
                }
                else
                {
                    n=o.indexOf(1);
                    c=(char)o1.get(n);
                }

                switch(c)
                {
                    case '+':
                        i=o2.get(n);
                        j=o2.get(n+1);
                        f=i+j;
                        o2.set(n,f);
                        o2.remove(n+1);
                        break;
                    case '-':
                        i=o2.get(n);
                        j=o2.get(n+1);
                        f=i-j;
                        o2.set(n,f);
                        o2.remove(n+1);
                        break;
                    case '*':
                        i=o2.get(n);
                        j=o2.get(n+1);
                        f=i*j;
                        o2.set(n,f);
                        o2.remove(n+1);
                        break;
                    case '/':
                        i=o2.get(n);
                        j=o2.get(n+1);
                        f=i/j;
                        o2.set(n,f);
                        o2.remove(n+1);
                        break;


                }
                System.out.println("HI");
                o.remove(n);
            }
            System.out.println(f);
            str=" "+f;

            t1.setText(str);

        }
    }
}
