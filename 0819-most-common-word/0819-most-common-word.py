import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()

        words = re.findall(r'[a-z]+', paragraph)

        banned = set(banned)

        count = {}

        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1

        return max(count, key=count.get)