class Solution(object):
    def matrixReshape(self,nums,r,c):
        if(len(nums)*len(nums[0]) != r*c):
            return nums
        
        oneRow = []
        for row in nums:
            oneRow += row
        result = []
        for i in range(r):
            result.append(oneRow[i*c:(i+1)*c])
        return result

ins = Solution()
print(ins.matrixReshape([[1,2],[3,4]],6,1))

