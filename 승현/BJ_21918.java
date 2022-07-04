import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_21918 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] bulb = new int[N+1]; // 0-> out, i-> in
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            bulb[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());
            int third = Integer.parseInt(st.nextToken());
            if (command == 1) {
                bulb[second] = third;
            } else if (command == 2) {
                for (int j = second; j <= third; j++) {
                    if (bulb[j] == 1) {
                        bulb[j] = 0;
                    } else if(bulb[j] == 0){
                        bulb[j] = 1;
                    }
                }
            } else if (command == 3) {
                for (int j = second; j <= third; j++) {
                    bulb[j] = 0;
                }
            } else if (command == 4) {
                for (int j = second; j <= third; j++) {
                    bulb[j] = 1;
                }
            }
        }
        for (int i = 1; i < N+1; i++) {
            System.out.print(bulb[i]+" ");
        }
    }
}
