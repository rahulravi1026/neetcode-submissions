class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # number of window chars that are "useful" (covered by s1)
        good = 0
        for i in range(26):
            good += min(s1Count[i], s2Count[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if good == len(s1):
                return True

            # remove left char
            c = ord(s2[l]) - ord('a')
            s2Count[c] -= 1
            if s2Count[c] < s1Count[c]:   # we dropped a char s1 needed
                good -= 1
            l += 1

            # add right char
            c = ord(s2[r]) - ord('a')
            if s2Count[c] < s1Count[c]:   # s1 still needs this char
                good += 1
            s2Count[c] += 1

        return good == len(s1)