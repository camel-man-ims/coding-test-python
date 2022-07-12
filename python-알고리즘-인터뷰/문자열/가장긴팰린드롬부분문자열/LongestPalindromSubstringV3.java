import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * date: 22.07.13
 */

public class LongestPalindromSubstringV3 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String longestPalindrome = solution.longestPalindrome("babad");
        System.out.println(longestPalindrome);
    }
    static class Solution {
        static String val;
        static int N;
        public String longestPalindrome(String s) {
            val = s;
            N = s.length();
            int max = 0;
            String maxVal = String.valueOf(s.charAt(0));

            if(N==1){
                return s;
            }
            for(int i=0;i<N;i++){
                String s1 = palin(i, i+1);
                String s2 = palin(i, i+2);

                if(s1.length() > max){
                    max = s1.length();
                    maxVal = s1;
                }
                if(s2.length() > max){
                    max = s2.length();
                    maxVal = s2;
                }
            }
            return maxVal;
        }
        public static String palin(int start, int end){
            if(end >= N) return "";
            while(start >= 0 && end < N && val.charAt(start) == val.charAt(end)){
                start --;
                end ++;
            }
            start++;
            end--;
            
            return val.substring(start, end+1);
         }
    }


}
