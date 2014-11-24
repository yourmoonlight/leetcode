class Solution:
    # @return a tuple, (index1, index2)
    def two_sum(self, num, target):
        index = []
        numtosort = num[:]
        numtosort.sort()
        i = 0
        j = len(num) - 1
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in xrange(0, len(num)):
                    if num[k] == numtosort[i]:
                        index.append(k)
                        break
                for k in xrange(len(num) - 1, -1, -1):
                    if num[k] == numtosort[j]:
                        index.append(k)
                index.sort()
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1
        return (index[0] + 1, index[1] + 1)
