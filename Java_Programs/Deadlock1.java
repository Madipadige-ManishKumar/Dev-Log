class ResourceOne
{
    public synchronized  void f1(ResourceTwo ref )
    {
        System.out.println("The ThreadOne Called  f1 ");
        try{
            Thread.sleep(1000);
        }
        catch (Exception e){}
        ref.f4();
    }
    public synchronized void f2()
    {
        System.out.println("F2 called ");
    }

}
class ResourceTwo
{
    public synchronized  void f3(ResourceOne ref)
    {
        System.out.println("The ThreadTwo Called  f3 ");
        try{
            Thread.sleep(1000);
        }
        catch (Exception e){}
        ref.f2();
    }
    public synchronized  void f4()
    {
        System.out.println("F4 called ");
    }
}


public class Deadlock1
{
    public static void main(String[] args) {
        ResourceOne ref = new ResourceOne();
        ResourceTwo t = new ResourceTwo();
        new Thread()
        {
            @Override
            public void run() {
                ref.f1(t);
            }
        }.start();
        new Thread()
        {
            @Override
            public void run() {
                t.f3(ref);
            }
        }.start();

    }
}
