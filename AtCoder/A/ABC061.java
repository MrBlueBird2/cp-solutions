import java.util.*;
public class Main {
    static void myMethod() {
        System.out.println("Hello World! ");
    }
  public static void main(String[] args) {
      /*String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      System.out.println("The Length Of The String Is " + txt.length());
      String txt2 = "Hello World";
      System.out.println(txt2.toUpperCase());
      System.out.println(txt2.toLowerCase());
      int a = 12;
      int b = 11;
      if(a == b){
          System.out.println(a+b);
      }else{
          System.out.println(a*b);
      }
      int x = 50;
      int y = 10;
      if(x > y){
          System.out.println("Hello World!");
      }
      int day = 3;
    switch (day) {
        case 1:
            System.out.println("Monday");
            break;
        case 2:
            System.out.println("Tuesday");
            break;
        case 3:
            System.out.println("Wednesday");
            break;
        case 4:
            System.out.println("Thursday");
            break;
        }
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
            if(i == 2){
                break;
            }
        }
        for(int i = 0; i<5; i++){
            System.out.println(i);
        }*/
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if(c >= a && c <= b) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}