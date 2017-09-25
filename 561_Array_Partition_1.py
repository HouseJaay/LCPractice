class Solution(object):
    def arrayPairSum(self,nums):
        return sum(sorted(nums,reverse=True)[1::2])
