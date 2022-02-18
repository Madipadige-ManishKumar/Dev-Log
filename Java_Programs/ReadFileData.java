import java.io.*;
public class ReadFileData {

          public static void main(String[] args) throws Exception
          {
              File f= new File("C:\\javapro\\rough.java");
              FileInputStream fis = new FileInputStream("C:\\javapro\\id.txt");
             // FileInputStream fis = new FileInputStream("C:\\javapro\\rough.java");
    //          System.out.println("THE FILE PATH IS "+f.getPath());
      //        System.out.println("THE FILE NAME IS "+f.getName());
		System.out.println((char)fis.read());
		System.out.println("THE AVALIABLE BYTES ARE "+fis.available());
		System.out.println((char)fis.read());
		System.out.println("THE AVALIABLE BYTES ARE "+fis.available());
		while(fis.available()!=0)	
		{
			System.out.print((char)fis.read());
		}

//              System.out.println(fis.getFD());// what is this
//              System.out.println(fis.readNBytes(100));
          /*    while(fis.available()>=0)
              {
                  System.out.println(fis.read());
              }*/


	
	}
}