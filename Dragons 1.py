import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int s = sc.nextInt();
        int n = sc.nextInt();
        int c =0 ;
        for(int i=1;i<=n;i++){
            int d = sc.nextInt();
            int b = sc.nextInt();
            if(s>d){
                s=s+b;
                c++;
            }
            else{
                c=0;
                break;
            }
        }
        if(c==n)
            System.out.println("YES");
        else
             System.out.println("NO");
    }
}