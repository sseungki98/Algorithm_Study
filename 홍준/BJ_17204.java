import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BJ_17204 {
    public static void main(String[] args)throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        ArrayList<Integer> game=new ArrayList<Integer>();
        int n=Integer.parseInt(st.nextToken());
        int bo=Integer.parseInt(st.nextToken());
        int point[]=new int[n];
        for(int i=0;i<n;i++)
            point[i]=Integer.parseInt(br.readLine());

        play(0,point,game);
        if(game.contains(bo))
            System.out.print(game.indexOf(bo)+1);
        else
            System.out.print(-1);

    }

    public static void play(int n,int[] point,ArrayList<Integer> game){
        if(!game.contains(point[n])) {
            game.add(point[n]);
            play(point[n], point, game);
        }
    }
}
