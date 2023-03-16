import java.io.*;
import java.util.StringTokenizer;
import static java.lang.Math.*;

public class BJ_1002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int JO[];
        int BAEK[];
        int RYU[];
        int test=Integer.parseInt(br.readLine());
        for(int i=0;i<test;i++){
            JO=new int[2];
            BAEK=new int[2];
            RYU=new int[2];
            st=new StringTokenizer(br.readLine());
            JO[0]=Integer.parseInt(st.nextToken());
            JO[1]=Integer.parseInt(st.nextToken());
            RYU[0]=Integer.parseInt(st.nextToken());
            BAEK[0]=Integer.parseInt(st.nextToken());
            BAEK[1]=Integer.parseInt(st.nextToken());
            RYU[1]=Integer.parseInt(st.nextToken());
            System.out.println(scan(JO,BAEK,RYU));
        }

    }

    public static int scan(int[] JO,int[] BAEK,int[] RYU){
        double distance=sqrt(pow((JO[0]-BAEK[0]),2)+pow((JO[1]-BAEK[1]),2));
        int answer=0;
        if(distance==0&&RYU[0]==RYU[1]){
            answer=-1;
        }
        else if(distance<RYU[0]+RYU[1]&&distance>abs(RYU[0]-RYU[1])){
            answer=2;
        }
        else if(distance==(RYU[0]+RYU[1]) || distance==abs(RYU[0]-RYU[1])){
            answer=1;
        }
        else if(distance>RYU[0]+RYU[1]||distance<abs(RYU[0]-RYU[1])) {
            answer=0;
        }
        return answer;
    }
}
