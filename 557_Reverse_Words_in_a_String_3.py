class Solution(object):
    def reverseWords(self,s):
        return ' '.join(map(lambda s: s[::-1],s.split(' ')))
