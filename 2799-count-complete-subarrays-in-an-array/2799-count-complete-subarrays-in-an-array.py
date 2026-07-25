class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic={}
        unique=len(set(nums))
        left=ans=0
        for right in range(len(nums)):
            dic[nums[right]]=dic.get(nums[right],0)+1
            while len(dic)==unique:
                ans+=len(nums)-right
                dic[nums[left]]-=1
                if dic[nums[left]]==0:
                    del dic[nums[left]]
                left+=1
        return ans