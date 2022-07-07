import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/*
 * 이전(22년10월) 풀이
 */

public class GroupAnagramV2 {
    public static void main(String[] args) {
        
    }
    static class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
            Map<String,List<String>> map = new HashMap<>();

            for(String s : strs){
                char[] chars = s.toCharArray();
                Arrays.sort(chars);
                String s1 = Arrays.toString(chars);
                if(map.containsKey(s1)){
                    map.get(s1).add(s);
                }else{
                    map.put(s1,new ArrayList<>());
                    map.get(s1).add(s);
                }
            }
            List<List<String>> res = new ArrayList<>();

            Set<String> strings = map.keySet();

            for(String s : strings){
                res.add(map.get(s));
            }

            return res;
        }
    }
}
