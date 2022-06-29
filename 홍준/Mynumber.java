package Algorithm;


public class Selfnumber {

	public static void main(String[] args) {
		
		int non[]=new int [10000];
    	int check=0;
    	int i=1;
    	while(i!=10001) {
    		String a=Integer.toString(i);
    		check=i;
    		for(int j=0;j<a.length();j++) {
    			check+=Character.getNumericValue(a.charAt(j));
    		}
    		if(check>10000) {
    			i++;
    			continue;
    		}
    		else if(non[check-1]==0) {
    			non[check-1]=check;
    		 }
    		i++;
    		
    		}
		for(i=0;i<10000;i++) {
			if(non[i]==0) {
				System.out.println(i+1);
			}
		}
		
		
	}

    
<<<<<<< HEAD
}
=======
}
>>>>>>> branch 'main' of https://github.com/sseungki98/Algorithm_Study.git
