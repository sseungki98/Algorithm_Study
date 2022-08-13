import java.io.*;
import java.util.*;

public class BJ_2877 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
        n=n+1;
        StringBuilder sb = new StringBuilder();
        int num = 0;
        while(n!=0){
            num = n%2;
            sb.append(num);
            n = n/2;
        }
        StringBuilder result = new StringBuilder();
        for(int i=sb.toString().length()-2;i>=0;i--){
            if(sb.charAt(i) == '0') result.append(4);
            else result.append(7);
        }
        System.out.println(result.toString());
	}
}
