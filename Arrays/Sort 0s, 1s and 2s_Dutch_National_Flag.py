"https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?utm=codolio"

# class Solution:
#     def sort012(self, arr):
#         # code here
#         c0,c1,c2 = 0,0,0
        
#         for x in arr:
#             if x == 0:
#                 c0 += 1
#             elif x == 1:
#                 c1 += 1
#             else:
#                 c2 += 1
        
#         index = 0
        
#         for i in range(c0):
#             arr[index] = 0
#             index += 1
        
#         for i in range(c1):
#             arr[index] = 1
#             index += 1
        
#         for i in range(c2):
#             arr[index] = 2
#             index += 1
        
""" 
T.C - O(n)
S.C - O(1)
Approach : Count the occurrences of 0, 1, and 2, 
then overwrite the array in sorted order using those counts
"""


class Solution:
    def sort012(self, arr):
        # code here
        
        n = len(arr)
        
        lo = 0
        mid = 0
        hi = n-1
        
        while (mid<=hi):
            
            if (arr[mid]==0):
                arr[mid],arr[lo] = arr[lo],arr[mid]
                lo += 1
                mid += 1
            
            elif (arr[mid]==1):
                mid += 1
            
            else:
                arr[mid],arr[hi] = arr[hi],arr[mid]
                hi -= 1
                

"""
Approach: Dutch National Flag / 3-way partitioning

TC: O(n)
SC: O(1)

"""