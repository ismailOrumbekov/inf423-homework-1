class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) == 1:
            return 1
        counter = 1
        max_counter = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                if nums[i] > nums[i - 1]:
                    counter += 1
                else:
                    if counter > max_counter:
                        max_counter = counter
                    counter = 1

        if counter > max_counter:
            max_counter = counter

        return max_counter