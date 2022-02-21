import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

public class WalkingDoraemon extends JPanel {

    private final Image doraemon;
    private int x;

    public WalkingDoraemon() {
        ImageIcon icon = new ImageIcon("doraemon.png");
        doraemon = icon.getImage();
        x = 0;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(doraemon, x, 0, null);
    }

    public void startAnimation() {
        JFrame frame = new JFrame("Walking Doraemon");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setPreferredSize(new Dimension(800, 600));
        frame.setResizable(false);
        frame.pack();
        frame.setVisible(true);

        setPreferredSize(new Dimension(800, 600));

        Timer timer = new Timer(50, new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                x += 5;
                if (x > getWidth()) {
                    x = -doraemon.getWidth(null);
                }
                repaint();
            }
        });

        timer.start();
    }

    public static void main(String[] args) {
        WalkingDoraemon doraemon = new WalkingDoraemon();
        doraemon.startAnimation();
    }
}