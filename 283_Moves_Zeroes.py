class Solution(object):
    def moveZeroes_old(self,nums):
        end_nozero = len(nums)-1
        for i in range(len(nums)):
            n = nums.pop(0)
            if n == 0:
                nums.append(0)
                end_nozero -= 1
            else:
                nums.insert(end_nozero,n)
        
    def moveZeroes(self,nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero += 1



ins = Solution()
nums = [0, 1, 0, 3, 12]
ins.moveZeroes(nums)
print(nums)
