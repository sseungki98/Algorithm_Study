class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        int sum[]=new int[n];
        int a=1;
        String line;
        String[] answer =new String[n];
        for(int i=0;i<n;i++){
            line="";
            sum[i]=(arr1[i]|arr2[i]);
            for(int j=n-1;j>=0;j--){
                a=1<<j;
                if((sum[i]&a)==a){
                    line=line+"#";
                    }
                else{
                    line=line+" ";
                } 
            }
            answer[i]=line;
        }
        return answer;
    }
}
