class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        maxlen = max(len(a), len(b))

        a = a.zfill(maxlen)
        b = b.zfill(maxlen)

        carry = 0
        result = ""
        for i in range(maxlen - 1, -1, -1):
            r = carry
            r += 1 if a[i] == "1" else 0
            r += 1 if b[i] == "1" else 0
            result = ("0" if r % 2 == 0 else "1") + result
            carry = 0 if r < 2 else 1
        if carry != 0:
            result = "1" + result
        return result.zfill(maxlen)
