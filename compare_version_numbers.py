class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1 = len(version1)
        len2 = len(version2)
        maxlen = max(len1, len2)
        for i in range(maxlen):
            v1token = 0
            if i < len1:
                v1token = int(v1[i])
            v2token = 0
            if i < len2:
                v2token = int(v2[i])
            if v1token < v2token:
                return -1
            if v1token > v2token:
                return 1
        return 0
