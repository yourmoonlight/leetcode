class Solution:
    def countAndSay(self, n):
        result = "1"

        for _ in xrange(n - 1):
            current = result[0]
            curCount = 1
            temp = ""
            for i in result[1:]:
                if i == current:
                    curCount += 1
                else:
                    temp += str(curCount) + current
                    current = i
                    curCount = 1
            temp += str(curCount) + current
            result = temp
        return result
