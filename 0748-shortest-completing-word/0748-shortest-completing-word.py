class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        required = [0] * 26
        
        for ch in licensePlate.lower():
            if ch.isalpha():
                required[ord(ch) - ord('a')] += 1
        
        answer = None
        
        for word in words:
            count = [0] * 26
            
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            if all(count[i] >= required[i] for i in range(26)):
                if answer is None or len(word) < len(answer):
                    answer = word
        
        return answer