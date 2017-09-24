class Solution(object):
    def conv2bits(self,value,bits):
        if value==0:
            return bits[::-1]
        else:
            bits.append(value%2)
            return self.conv2bits(int(value/2),bits)
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xbits = self.conv2bits(x,[])
        ybits = self.conv2bits(y,[])
        if len(xbits) != len(ybits):
            if len(xbits) > len(ybits):
                d = len(xbits)-len(ybits)
                zeros = [0 for x in range(d)]
                zeros.extend(ybits)
                ybits = zeros
            else:
                d = len(ybits)-len(xbits)
                zeros = [0 for x in range(d)]
                zeros.extend(xbits)
                xbits = zeros
        count = 0
        for i in range(len(xbits)):
            if xbits[i] == ybits[i]:
                pass
            else:
                count += 1
        return count

ins = Solution()
print(ins.hammingDistance(1,4))
