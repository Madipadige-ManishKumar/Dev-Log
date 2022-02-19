class ThreadOne extends Thread
{
    public void  run()
	{
		System.out.println("This Is The First Thread  ");
	}
}


class ThreadTwo extends Thread
{
    public void  run()
	{
		System.out.println("This Is The Second Thread  ");
	}
}

class ThreadThree extends Thread
{
    public void  run()
	{
		System.out.println("This Is The Thrid Thread  ");
	}
}
public class  Thread_NameAndPriority{
	public static void main(String []args)
	{
		ThreadOne t1 = new ThreadOne();
		ThreadTwo t2 = new ThreadTwo();
		ThreadThree t3 = new ThreadThree();
		t1.setPriority(Thread.MAX_PRIORITY);
		t2.setPriority(Thread.MIN_PRIORITY);
		t3.setPriority(Thread.NORM_PRIORITY);
		System.out.println("This Is The First Thread  With The Priority   =  " + t1.getPriority());
		System.out.println("This Is The First Thread  With The Priority   =  " + t2.getPriority());
		System.out.println("This Is The First Thread  With The Priority   =  " + t3.getPriority());
		t1.start();
		t2.start();
		t3.start();
	}
}