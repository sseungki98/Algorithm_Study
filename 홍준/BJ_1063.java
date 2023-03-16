import java.io.*;
import java.util.StringTokenizer;

public class BJ_1063 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int phon[][]=new int[2][2];
        String line[]=new String[2];
        for(int i=0;i<2;i++) {
            line[i] = st.nextToken();
            phon[i][0]=(int)line[i].charAt(0)-'A'+1;
            phon[i][1]=(int)line[i].charAt(1)-'0';
        }
        String move;
        int n=Integer.parseInt(st.nextToken());
        for(int i=0;i<n;i++){
            move=br.readLine();
            switch(move){
                case "R":
                    if(phon[0][0]<8)
                        phon[0][0]++;
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][0]<8)
                            phon[1][0]++;
                        else
                            phon[0][0]--;
                    }
                    break;
                case "L":
                    if(1<phon[0][0])
                        phon[0][0]--;
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(1<phon[1][0])
                            phon[1][0]--;
                        else
                            phon[0][0]++;
                    }
                    break;
                case "B":
                    if(1<phon[0][1])
                        phon[0][1]--;
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(1<phon[1][1])
                            phon[1][1]--;
                        else
                            phon[0][1]++;
                    }
                    break;
                case "T":
                    if(phon[0][1]<8)
                        phon[0][1]++;
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][1]<8)
                            phon[1][1]++;
                        else
                            phon[0][1]--;
                    }
                    break;
                case "RT":
                    if(phon[0][1]<8&&phon[0][0]<8) {
                        phon[0][1]++;
                        phon[0][0]++;
                    }
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][1]<8&&phon[1][0]<8) {
                            phon[1][1]++;
                            phon[1][0]++;
                        }
                        else {
                            phon[0][1]--;
                            phon[0][0]--;
                        }
                    }
                    break;
                case "LT":
                    if(phon[0][1]<8&&phon[0][0]>1) {
                        phon[0][1]++;
                        phon[0][0]--;
                    }
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][1]<8&&phon[1][0]>1) {
                            phon[1][1]++;
                            phon[1][0]--;
                        }
                        else {
                            phon[0][1]--;
                            phon[0][0]++;
                        }
                    }
                    break;
                case "RB":
                    if(phon[0][1]>1&&phon[0][0]<8) {
                        phon[0][1]--;
                        phon[0][0]++;
                    }
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][1]>1&&phon[1][0]<8) {
                            phon[1][1]--;
                            phon[1][0]++;
                        }
                        else {
                            phon[0][1]++;
                            phon[0][0]--;
                        }
                    }
                    break;
                case "LB":
                    if(phon[0][1]>1&&phon[0][0]>1) {
                        phon[0][1]--;
                        phon[0][0]--;
                    }
                    if(phon[0][1]==phon[1][1]&&phon[0][0]==phon[1][0]) {
                        if(phon[1][1]>1&&phon[1][0]>1) {
                            phon[1][1]--;
                            phon[1][0]--;
                        }
                        else {
                            phon[0][1]++;
                            phon[0][0]++;
                        }
                    }
                    break;
            }
        }
        for(int i=0;i<2;i++){
            char tmp;
            phon[i][0]+=64;
            tmp=(char)phon[i][0];
            line[i]=Character.toString(tmp)+String.valueOf(phon[i][1]);
            System.out.println(line[i]);
        }
    }
}
