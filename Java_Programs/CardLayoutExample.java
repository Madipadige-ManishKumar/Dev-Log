import java.awt.*;
import java.awt.event.*;
 class ClassPrograms extends Frame implements ActionListener {
    // Action Listener
//    Panel p1,p2;
//    TextField t1,t2;
//    Button b;
//    Label l ;
//    String summation;
//    public ClassPrograms() {
//        p1 = new Panel(new FlowLayout(FlowLayout.LEFT));
//        p2 = new Panel(new FlowLayout(FlowLayout.CENTER));
//        l = new
  actionPerformed(ActionEvent  e)
//        {
//            int n1 = Integer.parseInt(t1.getText());
//            int n2 = Integer.parseInt(t2.getText());
//            int s;
//            s = n1 + n2;
//            summation =" sum= "+s;
//            l.setText(summation);
//        }
//
//    public static void main(String[] args) {
//        ClassPrograms o = new ClassPrograms();
//    }
    // card Layout
    CardLayout c = new CardLayout();
    Button next, prev, first, last;
    Panel Parent;
    Panel c1, c2, c3, c4, c5;
    Label c1l1, c1l2, c2l1, c2l2, c3l1, c3l2, c4l1, c4l2, c5l1, c5l2;

    public ClassPrograms() {
        next = new Button("next");
        prev = new Button("Previous");
        first = new Button("First");
        last = new Button("Last");
        c1 = new Panel();
        c1l1 = new Label("White text");
        c1l2 = new Label("Black text");
        c1.setLayout(new FlowLayout());
        c1.add(c1l1);
        c1.add(c1l2);

        c2 = new Panel();
        c2l1 = new Label("White text");
        c2l2 = new Label("Black text");
        c2.setLayout(new FlowLayout());
        c2.add(c1l1);
        c2 = new Panel();
        c2.add(c1l2);
        c2l1 = new Label("Pink text");
        c2l2 = new Label("Orange text");
        c2.setLayout(new FlowLayout());
        c2.add(c2l1);
        c2.add(c2l2);

        c3= new Panel();
        c3l1=new Label("White text");
        c3l2=new Label("Black text");
        c3.setLayout(new FlowLayout());
        c3.add(c3l1);
        c3.add(c3l2);

        c4 = new Panel();
        c4l1=new Label("White text");
        c4l2=new Label("Black text");
        c4.setLayout(new FlowLayout());
        c4.add(c4l1);
        c4.add(c4l2);

        c5 = new Panel();
        c5l1=new Label("White text");
        c5l2=new Label("Black text");
        c5.setLayout(new FlowLayout());
        c5.add(c5l1);
        c5.add(c5l2);
        Parent = new Panel();
        c= new CardLayout();
        Parent .setLayout(c);
        Parent.add(c1,"First");
        Parent.add(c2,"Second");
        Parent.add(c3,"Thrid");
        Parent.add(c4,"Fourth");
        Parent.add(c5,"Fifth");
        setLayout(new FlowLayout());;
        add(next);
        add(prev);
        add(first);
        add(last);
        add(Parent);
        next.addActionListener(this);
        prev.addActionListener(this);
        first.addActionListener(this);
        last.addActionListener(this);
        setSize(500,500);
        setVisible(true);

    }
    @Override
    public void actionPerformed(ActionEvent e)
    {
        if(e.getActionCommand()=="first")
            c.first(Parent);
        else if (e.getActionCommand()=="last")
            c.last(Parent);
        else if (e.getActionCommand()=="next")
            c.next(Parent);
        else
            c.previous(Parent);
    }
    public static void main(String[] args) {

    }


}
