package BackJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_2579 {
    public static int dynamic(int[] dp, int[] stairs, int N) {
        for (int i = 4; i < N+1; i++) {
            dp[i] = Math.max(dp[i-2]+stairs[i],dp[i-3]+stairs[i]+stairs[i-1]);
        }
        return dp[N];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] stairs = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }
        if (N == 1) {
            System.out.println(stairs[1]);
            return;
        } else if (N == 2) {
            System.out.println(stairs[1]+stairs[2]);
            return;
        } else if (N == 3) {
            if (stairs[1] + stairs[3] > stairs[2] + stairs[3]) {
                System.out.println(stairs[1] + stairs[3]);
                return;
            } else {
                System.out.println(stairs[2] + stairs[3]);
                return;
            }
        }
        int[] dp = new int[N+1];
        dp[1] = stairs[1];
        dp[2] = stairs[1] + stairs[2];
        if (stairs[1] + stairs[3] > stairs[2] + stairs[3]) {
            dp[3] = stairs[1] + stairs[3];
        } else {
            dp[3] = stairs[2] + stairs[3];
        }
        System.out.println(dynamic(dp,stairs,N));
    }
}
