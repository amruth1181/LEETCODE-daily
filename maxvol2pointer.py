class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        i = 0
        n = len(height)
        j = n - 1
        while i < j:
            curr_vol = min(height[i], height[j]) * (j - i)
            vol = max(curr_vol, vol)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return vol

#11
