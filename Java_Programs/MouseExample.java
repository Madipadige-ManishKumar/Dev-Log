import java.awt.*;
import java.awt.event.*;

public class MouseExample extends Frame implements MouseListener
{
    Label lb;
    public MouseExample()
    {
        setSize(500,500);
        setVisible(true);
        lb = new Label("Label");
        add(lb,BorderLayout.EAST);
        addMouseListener(this);
    }
    public void mouseClicked(MouseEvent e)
    {
        System.out.println(e.getX()+" "+e.getY());
        lb.setText(e.getX()+" "+e.getY());

    }
    public void mouseExited(MouseEvent e)
    {
        System.out.println("exited");
    }
    public void mouseReleased(MouseEvent e)
    {
        System.out.println("release");

    }

    @Override
    public void mouseEntered(MouseEvent e) {
        System.out.println("mouseEntered");
    }

    public void mousePressed(MouseEvent e)
    {

    }
 public void mouseDragged(MouseEvent e)
    {
        System.out.println("Mouse Dragged ");
    }
    public void mouseMoved(MouseEvent e)
    {
        System.out.println("mouse moved");
    }
    public static void main(String[] args) {
        MouseExample o  = new MouseExample();
    }


}

