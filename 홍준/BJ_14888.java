import java.io.*;
import java.util.StringTokenizer;

public class BJ_14888 {
    static int max=Integer.MIN_VALUE;
    static int min=Integer.MAX_VALUE;
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int number[]=new int[n];
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++)
            number[i]=Integer.parseInt(st.nextToken());
        int operator[]=new int[4];
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<4;i++){
            operator[i]=Integer.parseInt(st.nextToken());
        }
        for(int i=0;i<4;i++){
            if(operator[i]!=0) {
                operator[i]-=1;
                calculate(number, operator, n, i, 0, number[0]);
                operator[i]+=1;
            }
        }
        System.out.println(max);
        System.out.println(min);

    }
    public static void calculate(int number[], int operator[], int n, int a, int current, int sum){
        switch (a){
            case 0:
                sum=sum+number[current+1];
                current+=1;
                break;
            case 1:
                sum=sum-number[current+1];
                current+=1;
                break;
            case 2:
                sum=sum*number[current+1];
                current+=1;
                break;
            case 3:
                sum=sum/number[current+1];
                current+=1;
                break;
        }
        
        if(current==n-1){
            max=Math.max(max,sum);
            min=Math.min(min,sum);
        }
        else {
            for (int i = 0; i < 4; i++) {
                if (operator[i] != 0) {
                    operator[i] -= 1;
                    calculate(number, operator, n, i, current, sum);
                    operator[i] += 1;
                }
            }
        }

    }
}
