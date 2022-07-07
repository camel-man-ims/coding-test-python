import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/*
 * date: 22.07.07
 * link: https://leetcode.com/problems/most-common-word/submissions/
 * 문자 아닌 값들을 치환하면 &nbsp가 하나 더 생긴다
 * 어떻게 처리하지? 했는데 생각해보니 해당 생긴 쓰레기 값 "  " 들을 " " 한칸으로 바꿔주면 됐다.
 * hint: https://heestory217.tistory.com/121 
 */

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.mostCommonWord("Bob. hIt, baLl", new String[]{"hit","bob"});
    }
    static class Solution {
        public String mostCommonWord(String paragraph, String[] banned) {
            paragraph = paragraph.replaceAll("[^\\w]", " ").replace("  "," ").toLowerCase();
            String[] split = paragraph.split(" ");

            Map<String,Integer> map = new HashMap<>();
            
            for(String s : split){
                if(s.contains(" ")) continue;
                s = s.toLowerCase();
                map.put(s, map.getOrDefault(s,0)+1);
            }

            Set<String> keys = map.keySet();
            Set<String> ban = new HashSet<>();

            for(String b : banned){
                ban.add(b);
            }

            int max =0 ;
            String maxVal = "";
            for(String k : keys){
                if(ban.contains(k)) continue;
                
                int mv = map.get(k);

                if(mv > max){
                    max = mv;
                    maxVal = k;
                }
            }
            return maxVal;
        }
    }
}
