class Solution(object):
    def findComplement(self,num):
        toBits = lambda n: '' if n==0 else toBits(int(n/2))+str(n%2)
        toInt = lambda l: 0 if len(l)==0 else 2*toInt(l[:-1])+int(l[-1])
        reverse = lambda s: '0' if s=='1' else '1'
        return toInt(list(map(reverse,toBits(num))))
