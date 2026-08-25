//TC: O(n)
//SC: O(1)
// https://leetcode.com/problems/jump-game-ii/solutions/5292559/video-keep-near-and-far-position-and-get-a780/ 
class Solution {
    public int jump(int[] nums) {
        int near = 0, far = 0, jumps = 0;

        while(far < nums.length - 1){
            int farthest = 0;
            for (int i=near;i <= far; i++)
                farthest = Math.max(farthest, i + nums[i]);
            near = far + 1;
            far = farthest;
            jumps += 1;
        }
        return jumps;
    }
}