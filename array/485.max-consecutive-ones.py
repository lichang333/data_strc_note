class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                cur_max = count if count > cur_max else cur_max 
                count = 0
        cur_max = count if count > cur_max else cur_max 
        return cur_max
