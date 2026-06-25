class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        count=0
        for i in range(len(nums)):
            count_tar=0
            for j in range(i,len(nums)):       
                if nums[j]==target:
                    count_tar+=1
                if count_tar>(j-i+1-count_tar):
                    count+=1
        return count
        