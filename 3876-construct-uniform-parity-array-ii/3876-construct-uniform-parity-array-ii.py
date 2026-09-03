class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        mn = min(nums1)

        possible_even = True
        for x in nums1:
            if x % 2 == 1:
                if x - mn <= 0 or (x - mn) % 2 != 0:
                    possible_even = False
                    break

        if possible_even:
            return True

        possible_odd = True
        for x in nums1:
            if x % 2 == 0:
                if x - mn <= 0 or (x - mn) % 2 != 1:
                    possible_odd = False
                    break

        return possible_odd