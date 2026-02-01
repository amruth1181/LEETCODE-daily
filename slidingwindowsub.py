class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsums = sum(nums[:k])
        curr = maxsums
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums) - k + 1):
            curr += (nums[k + i - 1] - nums[i - 1])
            if curr > maxsums:
                maxsums = curr

        return maxsums / k
#use sliding window instead of another loop to find the sum of the array
#add the element that to be added to the sliced sum and remove the first element