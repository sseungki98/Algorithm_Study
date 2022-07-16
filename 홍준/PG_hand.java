package Algo_study;
import java.io.*;

public class PG_hand {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String line=br.readLine();
		int numbers[]=new int[line.length()];
		for(int i=0;i<line.length();i++)
			numbers[i]=Character.getNumericValue(line.charAt(i));
		String hand=br.readLine();
		br.close();
        int a=0;
        int b=0;
        int Lnow=10;
        int Rnow=12;
        String answer = "";
        
        for(int i=0;i<numbers.length;i++){
            if(numbers[i]==0)
                numbers[i]=11;
            if(numbers[i]==1||numbers[i]==4||numbers[i]==7){
                answer=answer+"L";
                Lnow=numbers[i];
            }
            else if(numbers[i]==3||numbers[i]==6||numbers[i]==9){
                answer=answer+"R";
                Rnow=numbers[i];
            }
            else{
                if(Rnow%3==0)
                    a=Math.abs((Rnow-1)-numbers[i])/3+1;
                else if(Rnow%3==2)
                    a=Math.abs(Rnow-numbers[i])/3;
                if(Lnow%3==1)
                    b=Math.abs((Lnow+1)-numbers[i])/3+1;
                else if(Lnow%3==2)
                    b=Math.abs(Lnow-numbers[i])/3;
                if(a>b){
                    Lnow=numbers[i];
                    answer=answer+"L";
                }
                else if(b>a){
                    Rnow=numbers[i];
                    answer=answer+"R";
                }
                else if(a==b){
                    if(hand.equals("right")){
                        Rnow=numbers[i];
                        answer=answer+"R";
                    }
                    else if(hand.equals("left")){
                        Lnow=numbers[i];
                        answer=answer+"L";
                    }
                }
           
                    }
                }

	}

}
