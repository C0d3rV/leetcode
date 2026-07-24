class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }

        int reverseNum = 0;
        int dupX = x;
        while (x > 0){
            int lastDigit = x%10;
            reverseNum = reverseNum * 10 + lastDigit;
            x = x/10;
        }
        if (reverseNum == dupX){
            return true;
        }
        else{
            return false;
        }
    }
}