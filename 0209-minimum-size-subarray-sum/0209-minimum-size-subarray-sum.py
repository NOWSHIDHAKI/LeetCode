import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=sums=0
        ans=math.inf
        for right in range(len(nums)):
            sums+=nums[right]
            while sums>=target:
                ans=min(ans,right-left+1)
                sums-=nums[left]
                left+=1
        if ans==math.inf:
            return 0
        else:
            return ans