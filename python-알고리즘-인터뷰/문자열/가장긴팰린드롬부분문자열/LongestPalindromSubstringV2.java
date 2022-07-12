import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * date: 22.07.13
 * memo: 재귀로 돌면 시간터진다.
 */

public class LongestPalindromSubstringV2 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String longestPalindrome = solution.longestPalindrome("a");
        System.out.println(longestPalindrome);
    }
    static class Solution {
        static String val;
        static int N;
        public String longestPalindrome(String s) {
            val = s;
            N = s.length();
            int max = 0;
            String maxVal = "";

            if(N==1){
                return s;
            }

            for(int i=0;i<N;i++){
                int e1 = i+1;
                int e2 = i+2;

                int s1 = i;
                int s2 = i;

                while(s1 >=0 && e1 < N && palin(s1, e1)){
                    s1 --;
                    e1 ++;
                }

                s1++;
                e1--;

                while(s2 >= 0 && e2 < N && palin(s2, e2)){
                    s2 --;
                    e2 ++;
                }

                s2++;
                e2--;

                if(e1 < N && max < e1-s1+1){
                    maxVal = val.substring(s1,e1+1);
                    max = e1-s1+1;
                }
                if(e2< N && max < e2-s2+1){
                    maxVal = val.substring(s2,e2+1);
                    max = e2-s2+1;
                }
            }
            return maxVal;
        }
        public static boolean palin(int start, int end){
            if(start >= end){
                return true;
            }
            if(val.charAt(start) != val.charAt(end)){
                return false;
            }
            return palin(start+1, end-1);
         }
    }


}
