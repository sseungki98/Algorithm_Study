import java.util.*;

public class PG_distance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String places[][]={{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
				{"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, 
				{"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, 
				{"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, 
				{"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
		char place[][]=new char[5][5];
		int[] answer = new int[5];
		int p[][]=new int[25][2];
		for(int i=0;i<25;i++)
			Arrays.fill(p[i],-1);
		int middle;
        Arrays.fill(answer,1);
        int a;
		for(int k=0;k<5;k++){
			a=0;
            for(int i=0;i<5;i++){
                for(int j=0;j<5;j++){
                    place[i][j]=places[k][i].charAt(j);
                    if(place[i][j]=='P'){
                    	p[a][0]=i;
                        p[a][1]=j;
                        a++;
                        }
                    }
            }
            for(int i=0;i<a-1;i++){
            	if(answer[k]==0)
            		break;
                for(int j=i+1;j<a;j++){
                    if((Math.abs(p[i][0]-p[j][0])+Math.abs(p[i][1]-p[j][1]))<=2){
                         if(p[i][0]==p[j][0]){
                               middle=(p[i][1]+p[j][1])/2;
                               if(place[p[i][0]][middle]!='X') {
                                   answer[k]=0;
                                   break;
                               }
                           }
                         else if(p[i][1]==p[j][1]){
                               middle=(p[i][0]+p[j][0])/2;
                               if(place[middle][p[i][1]]!='X') {
                                   answer[k]=0;
                                   break;
                               }
                           }
                         else{
                               if(p[i][1]>p[j][1]){
                                   if(place[p[j][0]][p[j][1]+1]!='X') {
                                       answer[k]=0;
                                       break;
                                   }
                                   if(place[p[i][0]][p[i][1]-1]!='X') {
                                       answer[k]=0;
                                       break;
                                   }
                               }
                               else if(p[i][1]<p[j][1]){
                                  if(place[p[j][0]][p[j][1]-1]!='X') {
                                       answer[k]=0;
                                       break;
                                  }
                                  if(place[p[i][0]][p[i][1]+1]!='X') {
                                       answer[k]=0; 
                                       break;
                                   }
                               }
                           }
                    }
                }
            }
          }
		System.out.println(Arrays.toString(answer));
	}
}
