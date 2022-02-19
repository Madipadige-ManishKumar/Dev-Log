class SleepEx extends Thread{
    public void run()
    {
        try {

            int i;
            for (i = 0; i < 10; i++){
            sleep(5000);
                System.out.println("The Current Thread Is " + Thread.currentThread().getName()+" "+ " i= "+i);}

        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
          SleepEx o = new SleepEx();
          o.setName("A");
          o.start();
        try {
            int i;
            for (i = 0; i < 10; i++){
            sleep(5000);
                System.out.println("The Current Thread Is " + Thread.currentThread().getName()+" "+ " i= "+i);}
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

}