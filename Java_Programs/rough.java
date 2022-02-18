import java.util.Calendar;

// Get current time

public class rough
{
public static void main(String []args)
{
Calendar calendar = Calendar.getInstance();
int hour = calendar.get(Calendar.HOUR_OF_DAY); // 24 hour format
int minute = calendar.get(Calendar.MINUTE);
int second = calendar.get(Calendar.SECOND);
System.out.println("Hours:"+hour+"Minutes"+minute+"seconds"+second);
if (19 == hour)
System.out.println("Hello");
}

}