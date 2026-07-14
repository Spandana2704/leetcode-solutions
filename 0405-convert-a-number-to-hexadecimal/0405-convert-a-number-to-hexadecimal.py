class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        if num < 0:
            num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        res = []

        while num:
            res.append(hex_chars[num & 15])  # last 4 bits
            num >>= 4

        return "".join(res[::-1])