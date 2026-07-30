class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k