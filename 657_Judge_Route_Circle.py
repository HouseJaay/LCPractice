class Solution(object):
    def judgeCircle(self,moves):
        def move(posi,dirc):
            if dirc == 'U':
                posi[0] += 1
            elif dirc == 'D':
                posi[0] -= 1
            elif dirc == 'L':
                posi[1] -= 1
            elif dirc == 'R':
                posi[1] += 1
        posi = [0,0]
        for dirc in moves:
            move(posi,dirc)
        if posi[0]==0 and posi[1]==0:
            return True
        else:
            return False

ins = Solution()
print(ins.judgeCircle('UD'))
print(ins.judgeCircle('RR'))
