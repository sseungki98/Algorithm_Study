import java.io.*;
import java.util.*;

public class BJ_25758 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        HashMap<Character,Integer>front=new HashMap<>();
        HashMap<Character,Integer>Back=new HashMap<>();
        Set<String> gene=new HashSet<>();
        StringTokenizer st=new StringTokenizer(br.readLine());
        Set<Character> call=new TreeSet<>();
        String line;
        int tmp;
        for(int i=0;i<n;i++) {
            line = st.nextToken();
            gene.add(line);
            tmp=front.getOrDefault(line.charAt(0),0);
            front.put(line.charAt(0),tmp+1);
            tmp=Back.getOrDefault(line.charAt(1),0);
            Back.put(line.charAt(1),tmp+1);
        }

        for(Character F_key:front.keySet()){
            for(Character B_key:Back.keySet()){
                if(Back.get(B_key)==1&&front.get(F_key)==1){
                    if(gene.contains(Character.toString(F_key)+B_key))
                        continue;
                }
                if(Character.compare(F_key,B_key)>=0)
                    call.add(F_key);
                else
                    call.add(B_key);
            }
        }
        System.out.println(call.size());
        Iterator iterator=call.iterator();
        while(iterator.hasNext())
            System.out.print(iterator.next()+" ");


    }


}
