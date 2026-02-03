class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high=0
        alt=0
        for i in range(len(gain)):
            alt+=gain[i]
            high=max(high,alt)

        return high
