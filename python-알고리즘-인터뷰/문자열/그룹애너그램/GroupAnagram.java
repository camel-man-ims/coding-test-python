import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * date: 22.07.08
 * 왜 틀렸다고 나오는지 모르겠다.
 */

public class GroupAnagram {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<String>> groupAnagrams = solution.groupAnagrams(new String[]{"bdddddddddd","bbbbbbbbbbc"});

        for(List<String> li : groupAnagrams){
            System.out.println(li);
        }

    }
    static class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
            Map<String,List<String>> map = new HashMap<>();
            
            for(String s : strs){
                String en = extractNumber(s);
                
                if(!map.containsKey(en)){
                    map.put(en,new ArrayList<>());
                }
                map.get(en).add(s);
            }
            List<List<String>> res = new ArrayList<>();

            Set<String> keys = map.keySet();
            
            for(String key : keys){
                res.add(map.get(key));
            }

            return res;
        }

        private String extractNumber(String s) {
            int[] arr = new int[26];
            s = s.toLowerCase();

            for(int i=0;i<s.length();i++){
                arr[s.charAt(i)-'a']++;
            }
            StringBuilder sb = new StringBuilder();

            for(int i=0;i<26;i++){
                sb.append(arr[i]);
            }
            return sb.toString();
        }
    }
}
