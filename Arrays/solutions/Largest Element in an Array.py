"https://takeuforward.org/plus/dsa/problems/largest-element?utm=codolio"

# Approach:
# Assume first element is maximum.
# Traverse the array and update maximum when needed.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def largestElement(self, nums):
        maximum = nums[0]
        for x in nums:
            if x > maximum:
                maximum = x
        return maximum