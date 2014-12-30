class Solution:
    # @return a list of lists of length 3, [[val1, val2, val3]]
    def threeSum(self, num):
        i = 0   # for the first item
        result = []
        num.sort()
        while i < len(num) - 2:
            j = i + 1  # for the middle item
            k = len(num) - 1  # for the last item
            while j < k:
                if num[i] + num[j] + num[j] > 0 or num[i] + num[k] + num[k] < 0:
                    break
                if num[i] + num[j] + num[k] == 0:
                    result.append([num[i], num[j], num[k]])
                    j += 1
                    while j < k + 1 and num[j] == num[j - 1]:  # skip duplicate
                        j += 1
                    k -= 1
                    while k > j - 1 and num[k] == num[k + 1]:
                        k -= 1
                elif num[i] + num[j] + num[k] > 0:
                    # skip duplicate num[k + 1]
                    k -= 1
                    while k > j - 1 and num[k] == num[k + 1]:
                        k -= 1
                else:
                    # skip duplicate num[j - 1]
                    j += 1
                    while j < k + 1 and num[j] == num[j - 1]:
                        j += 1
            # skip duplicate num[i - 1]
            i += 1
            while i < len(num) - 1 and num[i] == num[i - 1]:
                i += 1
        return result
