class Solution {
    public int smallestIndex(int[] nums) {
        int index = -1;
        for (int i = 0; i < nums.length; i++) {
            int digitSum = 0;
            int num = nums[i];
            while (num > 0) {
                digitSum += num % 10;
                num /= 10;
            }
            if (i == digitSum) {
                index = i;
                break;
            }
        }
        return index;
    }
        
    }
