class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for item in prices:
            mini=min(mini,item)
            curr=item-mini
            profit=max(profit,curr)
        return profit