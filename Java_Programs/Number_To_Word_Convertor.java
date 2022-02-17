import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

class Number_To_Word_Convertor
{
    public static void main(String[] args) {
        String s,st;
        String d="0abcdefghijklmnopqrstuvwxyz";
        String input;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter The String");
        s=sc.nextLine();
        st=s.toLowerCase();
        System.out.println("Enter The value ");
        input=sc.nextLine();
        StringTokenizer str = new StringTokenizer(st," ",true);
        StringTokenizer str1 = new StringTokenizer(s," ",true);
        ArrayList<String>o  = new ArrayList<String>();
        ArrayList<String>o1  = new ArrayList<String>();
        while(str.hasMoreTokens()){
            String w= str.nextToken();
            if(w.equals(" ") ){}
                else
                o.add(w);
            }
        while(str1.hasMoreTokens()){
            String w= str1.nextToken();
            if(w.equals(" ") ){}
            else
                o1.add(w);
        }
        int f=0,i,j;
        String s2="";
            String s1;
            while(f<o.size())
            {
                s2="";
                s1=String.valueOf(o.get(f));
                for(i=0;i<s1.length();i++) {
                    for (j = 0; j < d.length(); j++) {
                        if (d.charAt(j) == s1.charAt(i)) {
                            s2 += String.valueOf(j);
                            break;
                        }
                    }
                }
                if(s2.equals(input)){
                    System.out.println(o1.get(f));
                    System.exit(1);}
                f++;
            }
        System.out.println("Not Found");
    }
}
