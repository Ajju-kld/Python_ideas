import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Scanner;

/**
 * Filedemo
 */
public class Filedemo {
public static void main(String[] args) {
try {
    
    FileInputStream s =new FileInputStream("hello.c");
    FileOutputStream d=new FileOutputStream("make.c");
  byte [] b=s.readAllBytes();
 String f="hello this is fake";
 
 for(int i = 0; i < b.length; i++) {
    System.out.println(b[i]);
 }
   d.write(b);
  
   d.close();
   s.close();
   } catch (Exception e) {
    //TODO: handle exception
}
}
    
}