import java.util.*;

public class Main{
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "A man, a plan, a canal: Panama".replace(" ", "").replaceAll("[^a-zA-Z]","").toLowerCase();

        boolean palindrome = solution.isPalindrome(s);
        System.out.println(palindrome);
    }
    static class Solution {
        public boolean isPalindrome(String s) {
            s = s.replace(" ", "").replaceAll("[^a-zA-Z0-9]","").toLowerCase();
            return recurse(s);
        }

        public boolean recurse(String s){
            if (s.length() <= 1){
                return true;
            }

            if(s.charAt(0) == s.charAt(s.length()-1)){
                return recurse(s.substring(1,s.length()-1));
            }else{
                return false;
            }
        }
    }
}
