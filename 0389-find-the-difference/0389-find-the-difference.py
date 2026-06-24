class Solution(object):
    def findTheDifference(self, s, t):
        xor = 0

        for ch in s:
            xor ^= ord(ch)

        for ch in t:
            xor ^= ord(ch)

        return chr(xor)