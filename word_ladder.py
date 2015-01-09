from collections import deque


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        wordLen = len(start)
        queue = deque([(start, 1)])
        while queue:
            curr = queue.popleft()
            curWord = curr[0]
            curLength = curr[1]
            if curWord == end:
                return curLength
            for i in xrange(wordLen):
                part1 = curWord[:i]
                part2 = curWord[i+1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if curWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in dict:
                            queue.append((nextWord, curLength + 1))
                            dict.remove(nextWord)  # delete once used
        return 0
