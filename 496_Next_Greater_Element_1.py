class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        cache = {}
        st = []
        for n in nums:
            if len(st)==0:
                st.append(n)
            elif st[-1] > n:
                st.append(n)
            else:
                while st and st[-1]<n:
                    cache[st.pop()]=n
                st.append(n)
        result = []
        for key in findNums:
            if key in cache:
                result.append(cache[key])
            else:
                result.append(-1)
        return result

ins = Solution()
print(ins.nextGreaterElement([2,4],[1,2,3,4]))
