"https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1"

# class Solution:
#     def maxSubarraySum(self, arr):
#         # Code here
        
#         n = len(arr)
#         maxi = arr[0]
#         for i in range(n):
#             for j in range(i+1,n+1):
#                 arr_sum = sum(arr[i:j])
#                 if arr_sum > maxi:
#                     maxi = arr_sum
        
#         return maxi

"""
Gives TLE Error

T.C -> O(n^2)
S.C -> O(1)

Approach: Run two nested loops to iterate over all possible subarrays
,and find the maximum sum. 
The outer loop will mark the starting point of a subarray and 
inner loop will mark the ending point of the subarray.

"""


class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        maxEnding = arr[0]
        res = arr[0]
        
        for i in range(1,len(arr)):
            # Either extend the previous subarray or start 
            # new from current element
            maxEnding = max(maxEnding+arr[i],arr[i])
            res = max(res,maxEnding) 
            # update result if new array sum is larger
        
        return res
"""
T.C -> O(n)
S.C -> O(1)

Approach:
At each element, decide whether 
it's better to extend the previous subarray,
or start a new subarray, while keeping track of the best sum seen so far.

"""
            