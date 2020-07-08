import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = (n*b+99)/100 -a;
        if(c<0){
            c=0;
            
        }
        System.out.println(c);
        
    }
}