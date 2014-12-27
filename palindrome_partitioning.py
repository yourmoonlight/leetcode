class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        result = []
        if self.isPalindrome(s):
            result.append([s])
        for i in range(1, len(s)):
            head = s[:i]
            if not self.isPalindrome(head):
                continue
            tailPartion = self.partition(s[i:])
            result.extend([[head] + item for item in tailPartion])
        return result

    def isPalindrome(self, s):
        begin, end = 0, len(s) - 1
        while begin < end:
            if s[begin] != s[end]:
                return False
            else:
                begin += 1
                end -= 1
        return True
