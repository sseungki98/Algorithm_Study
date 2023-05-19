
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_21610 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int order=Integer.parseInt(st.nextToken());
        int map[][]=new int[n+1][n+1];
        ArrayList<int[]> cloud=new ArrayList<>();
        int tmp[]=new int[]{n,1};
        cloud.add(tmp);
        tmp=new int[]{n,2};
        cloud.add(tmp);
        tmp=new int[]{n-1,1};
        cloud.add(tmp);
        tmp=new int[]{n-1,2};
        cloud.add(tmp);
        for(int i=1;i<=n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=1;j<=n;j++){
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        for(int i=0;i<order;i++){
            st=new StringTokenizer(br.readLine());
            move(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),map,cloud,n);
            rain(map,cloud,n);
            makecloud(map,cloud,n);
        }
        int sum=0;
        for(int i=1;i<=n;i++)
            sum+=Arrays.stream(map[i]).sum();

        System.out.println(sum);

    }
    public static void move(int order,int distance,int[][] map,ArrayList<int[]> cloud,int n){
        int tmp;
        int tmp2;
        switch (order){
            case 1 :
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]-(distance%n);
                    if(tmp<1)
                        tmp+=n;
                    cloud.get(i)[1]=tmp;
                }
                break;
            case 2:
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]-(distance%n);
                    tmp2=cloud.get(i)[0]-(distance%n);
                    if(tmp<1)
                        tmp+=n;
                    if(tmp2<1)
                        tmp2+=n;
                    cloud.get(i)[1]=tmp;
                    cloud.get(i)[0]=tmp2;
                }
                break;
            case 3:
                for(int i=0;i<cloud.size();i++){
                    tmp2=cloud.get(i)[0]-(distance%n);
                    if(tmp2<1)
                        tmp2+=n;
                    cloud.get(i)[0]=tmp2;
                }
                break;
            case 4:
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]+(distance%n);
                    tmp2=cloud.get(i)[0]-(distance%n);
                    if(tmp>n)
                        tmp-=n;
                    if(tmp2<1)
                        tmp2+=n;
                    cloud.get(i)[1]=tmp;
                    cloud.get(i)[0]=tmp2;

                }
                break;
            case 5:
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]+(distance%n);
                    if(tmp>n)
                        tmp-=n;
                    cloud.get(i)[1]=tmp;
                }
                break;
            case 6:
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]+(distance%n);
                    tmp2=cloud.get(i)[0]+(distance%n);
                    if(tmp>n)
                        tmp-=n;
                    if(tmp2>n)
                        tmp2-=n;
                    cloud.get(i)[1]=tmp;
                    cloud.get(i)[0]=tmp2;
                }
                break;
            case 7:
                for(int i=0;i<cloud.size();i++){
                    tmp2=cloud.get(i)[0]+(distance%n);

                    if(tmp2>n)
                        tmp2-=n;

                    cloud.get(i)[0]=tmp2;
                }
                break;
            case 8:
                for(int i=0;i<cloud.size();i++){
                    tmp=cloud.get(i)[1]-(distance%n);
                    tmp2=cloud.get(i)[0]+(distance%n);

                    if(tmp<1)
                        tmp+=n;
                    if(tmp2>n)
                        tmp2-=n;

                    cloud.get(i)[0]=tmp2;
                    cloud.get(i)[1]=tmp;
                }
                break;
        }
    }
    public static void rain(int[][] map,ArrayList<int[]>cloud,int n){
        int a;
        int b;
        for(int i=0;i<cloud.size();i++){
            a=cloud.get(i)[0];
            b=cloud.get(i)[1];
            map[a][b]+=1;
        }
        for(int i=0;i<cloud.size();i++){
            a=cloud.get(i)[0];
            b=cloud.get(i)[1];
            if(a-1>0&&b-1>0){
                if(map[a-1][b-1]>0)
                    map[a][b]+=1;
            }
            if(a+1<=n&&b-1>0){
                if(map[a+1][b-1]>0)
                    map[a][b]+=1;
            }
            if(a-1>0&&b+1<=n){
                if(map[a-1][b+1]>0)
                    map[a][b]+=1;
            }
            if(a+1<=n&&b+1<=n){
                if(map[a+1][b+1]>0)
                    map[a][b]+=1;
            }

        }
    }
    public static void makecloud(int[][] map,ArrayList<int[]>cloud,int n){
        int size=cloud.size();
        int tmp2[];
        int map2[][]=new int[n+1][n+1];
        int a;
        int b;
        for(int i=0;i<size;i++) {
            a=cloud.get(0)[0];
            b=cloud.get(0)[1];
            map2[a][b]=1;
            cloud.remove(0);
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(map[i][j]>=2&&map2[i][j]!=1){
                    tmp2=new int[]{i,j};
                    cloud.add(tmp2);
                    map[i][j]-=2;
                }
            }
        }

    }
}
