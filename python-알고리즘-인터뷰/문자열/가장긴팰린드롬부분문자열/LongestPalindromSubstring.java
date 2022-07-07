import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * date: 22.07.07
 * memo: 시간터짐
 */

public class LongestPalindromSubstring {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String longestPalindrome = solution.longestPalindrome("a");
        System.out.println(longestPalindrome);
    }
    static class Solution {
        public String longestPalindrome(String s) {
            List<String> list = new ArrayList<>();
            int N = s.length();
            for(int i=0;i<N;i++){
                for(int j=i+1;j<=N;j++){
                    String sub = s.substring(i, j);
                    System.out.println(sub);
                    
                    if(palin(sub)){
                        list.add(sub);
                    }
                }
            }
            
            Collections.sort(list,(s1,s2)->{
                return Integer.compare(s2.length(), s1.length());
            });
            return list.get(0);
        }
    }

    public static boolean palin(String s){
        if(s.length()<=1){
            return true;
        }

        if(s.charAt(0) == s.charAt(s.length()-1)){
            return palin(s.substring(1, s.length()-1));
        }else{
            return false;
        }
    }
}
