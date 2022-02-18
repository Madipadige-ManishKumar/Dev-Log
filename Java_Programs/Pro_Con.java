class Pandc
{
	int i=0;	
	boolean flag =true;
		public synchronized void put() 
		{	
			if(flag ==true){
			System.out.println("Produce = "+(++i));	
			notify();
			flag =false;}
			else{
			try{wait();}catch(Exception e){}
			}
		}
		public synchronized void get() 
		{
			if(flag ==false){
			System.out.println("Consume = "+i);
			notify();
			flag =true;
			}
			else{
			try{wait();}catch(Exception e){}
			}
		}
}
class Producuer extends Thread
{
	Pandc o = new Pandc();
	Producuer (Pandc o1)
	{
		o = o1;
	}
	public void run()
	{
		while(true){
		o.put();
		try{Thread.sleep(1000);}
		catch(Exception e){}
		}
	}
}

class Consumer extends Thread
{
	Pandc o = new Pandc();
	Consumer(Pandc o1)
	{
		o = o1;
	}
    public void run()
	{
		while(true){
		o.get();
		try{Thread.sleep(1000);}
		catch(Exception e){}
		}
	}
}

class Pro_Con
{
	public static void main(String []args)
	{
		Pandc o = new Pandc();
		Producuer  p = new Producuer (o);
		Consumer c = new Consumer(o);
		p.start();
		c.start();
	}
}