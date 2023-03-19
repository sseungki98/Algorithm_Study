import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BJ_5545 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int list=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        int dow_price=Integer.parseInt(st.nextToken());
        int topping_price=Integer.parseInt(st.nextToken());
        int dow_cal=Integer.parseInt(br.readLine());
        int sum_cal=dow_cal;
        int price=dow_price;
        Integer topping[]=new Integer[list];
        for(int i=0;i<list;i++){
            topping[i]=Integer.parseInt(br.readLine());
        }
        Arrays.sort(topping, Comparator.reverseOrder());
        for(int i=0;i<list;i++){
            if((sum_cal/price)<=(sum_cal+topping[i])/(price+topping_price)) {
                sum_cal = sum_cal + topping[i];
                price = price + topping_price;
            }
        }
        System.out.println((Integer)(sum_cal/price));

    }
}
