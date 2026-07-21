class Solution {
    public int singleNonDuplicate(int[] nums) {
        int l = 0, r=nums.length - 1;

        while(l<=r){
            int mid = (l+r)/2;
            if((mid-1<0 || nums[mid] != nums[mid-1]) && (mid+1 == nums.length || nums[mid] != nums[mid+1]))
                return nums[mid];
            int leftSize = (mid-1 >= 0 && nums[mid-1] == nums[mid]) ? mid -1: mid;
            if(leftSize % 2 == 0){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
}