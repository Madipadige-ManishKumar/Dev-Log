import java.time.LocalDate;
import java.util.Calendar;
import java.util.Scanner;
 class A {
    public static void main(String[] args)  {
            int day,year,d,i,m=0,y,x=0,re=0;
            String [] week ={"sun","mon","tue","wed","thru","fri","sat"};
            Scanner sc = new Scanner(System.in);
            System.out.println("ENTER BIRTH DATE ,MONTH_NUMBER,YEAR   DD  MM  YYYY");
            day=sc.nextInt();
            m = sc.nextInt();
            year = sc.nextInt();
        LocalDate o =LocalDate.of(year,m,day);
        LocalDate o2 =LocalDate.of(2024,2,29);
        LocalDate o1 =  LocalDate.now();
        d=o.getDayOfYear()-o1.getDayOfYear();
        x= (o.isLeapYear()) ? 366 :365;
        re=o1.isBefore(o) ? d : x+d;
        if(o.isLeapYear())
        {if(o.getDayOfYear()==60)
                re=365*4;}
        System.out.println("ARE THE DAYS  =  "+re);
        int h= re%7;

        h= d>=0 ? h+2 :h+1;
        System.out.println("THE DAY_OF_WEEK    =   "+week[h]);
    }
}