class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        maxlen=maxfreq=left=0
        for right in range(len(s)):
            dic[s[right]]=dic.get(s[right],0)+1
            maxfreq=max(maxfreq,dic[s[right]])
            while (right-left+1)-maxfreq>k:
                dic[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen