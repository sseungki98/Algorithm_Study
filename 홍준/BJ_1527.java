import java.io.*;
        import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ_1527 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int a=Integer.parseInt(st.nextToken());
        int b=Integer.parseInt(st.nextToken());
        int cnt=0;
        String[] plus = { "4", "7" };
        cnt=bfs(plus,a,b);
        System.out.println(cnt);

    }
    public static int bfs(String[] plus,int A,int B) {
        int ans=0;
        Queue<String> q = new LinkedList<>();
        q.add("");

        while (!q.isEmpty()) {
            String s = q.poll();

            for (int i = 0; i < 2; i++) {
                String next = s + plus[i]; // 문자열 이어붙히기

                // 문자열의 크기가 더 작은 경우, 이어붙힌 문자열을 queue에 다시 삽입
                if (Long.parseLong(next) < A)
                    q.add(next);
                    // 문자열의 크기가 더 큰 경우, 무시
                else if (Long.parseLong(next) > B)
                    continue;
                    // 문자열의 크기가 A와 B의 사이에 있는 경우, count 증가 후, queue에 삽입
                else {
                    ans++;
                    q.add(next);
                }
            }
        }
        return ans;
    }

    }
