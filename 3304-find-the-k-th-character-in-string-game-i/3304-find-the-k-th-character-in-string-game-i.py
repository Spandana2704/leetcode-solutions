class Solution(object):
    def kthCharacter(self, k):
        word = "a"

        while len(word) < k:
            new_word = ""

            for ch in word:
                new_word += chr(ord(ch) + 1)

            word += new_word

        return word[k - 1]