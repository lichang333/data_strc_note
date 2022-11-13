class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            # if int(math.log(n,10)) % 2 == 1:
            if len(str(n)) % 2 == 0:
                count += 1
        return count
