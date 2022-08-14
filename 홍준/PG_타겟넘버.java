class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        int sum=0;
        int tmp=0;
        for(int i=0;i<numbers.length;i++){
            sum=sum+numbers[i];
        }
        for(int i=0;i<numbers.length;i++){
            tmp=sum;
            tmp=tmp-2*numbers[i];
            if(tmp==target){
                answer=answer+1;
                continue;
            }
            else if(tmp<target)
                continue;
            answer=find(numbers,target,i,tmp,answer);
        }
        return answer;
    }
    public static int find(int[] numbers,int target,int index,int tmp,int answer){
        int a=tmp;
        if(tmp==target)
            return answer+1;
        else if(tmp<target)
            return answer;
        for(int j=index+1;j<numbers.length;j++){
            a=tmp;
            a=a-2*numbers[j];
            answer=find(numbers,target,j,a,answer);
        }
        return answer;
    }
}
