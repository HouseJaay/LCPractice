class Solution(object):
    def twoSum(self,nums,target):
        args = sorted(range(len(nums)),key = lambda x:nums[x])
        argmin,argmax = 0,len(nums)-1
        nums.sort()
        while(nums[argmin]+nums[argmax]!=target):
            if nums[argmin]+nums[argmax]>target:
                argmax -= 1
            else:
                argmin += 1
        return [args[argmin],args[argmax]]

ins = Solution()
print(ins.twoSum([11,2,7,15],9))

