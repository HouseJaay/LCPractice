class Solution(object):
    def findWords(self,words):
        row = {1:'qwertyuiop',2:'asdfghjkl',3:'zxcvbnm'}
        dict_row = {}
        for key,value in row.items():
            for c in value:
                dict_row[c] = key
        result = []
        for word in words:
            if len(set(map(lambda c:dict_row[c],word.lower())))==1:
                result.append(word)

        return result

ins = Solution()
print(ins.findWord(["Hello", "Alaska", "Dad", "Peace"]))
