class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        result = float('inf')
        resultdif = float('inf')
        i = 0
        num.sort()
        while i < len(num) - 2:
            j = i + 1
            k = len(num) - 1
            while j < k:
                temp = num[i] + num[j] + num[k]
                if temp == target:
                    return temp
                elif temp < target:
                    if target - temp < resultdif:
                        resultdif = target - temp
                        result = temp
                    j += 1
                    while j < k + 1 and num[j] == num[j - 1]:
                        j += 1
                else:
                    if temp - target < resultdif:
                        resultdif = temp - target
                        result = temp
                    k -= 1
                    while k > j - 1 and num[k] == num[k + 1]:
                        k -= 1
            i += 1
            while i < len(num) - 1 and num[i] == num[i - 1]:
                i += 1
        return result
