class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -1
        second = -1
        index = -1

        for i, num in enumerate(nums):
            if num > largest:
                second = largest
                largest = num
                index = i
            elif num >= second:
                second = num

        if largest >= 2 * second:
            return index
        return -1