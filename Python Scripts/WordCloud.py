class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = {}
        for i in nums:
            if str(i) in numbers:
                # Increment the value
                numbers[str(i)] += 1
            else:
                numbers[str(i)] = 1
        print(numbers)
