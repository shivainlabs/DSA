# "https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?utm=codolio"


# class Solution:
#     def rotate(self, arr):
#         last = arr.pop() # O(1)
#         arr.insert(0,last) # O(n) Because of shifting the elements
#         return arr
        
        
"""
T.C -> O(n)
S.C -> O(1)

Approach: Remove the last element from an array and insert it,
at the begining, and return modified array

"""

# class Solution:
#     def rotate(self, arr):
#         last = arr[-1]
#         arrc = arr.copy()
        
#         for i in range(1,len(arr)):
#             arr[i] = arrc[i-1]
        
#         arr[0] = last
        
#         return arr


"""

T.C -> O(n)
S.C -> O(n)

Approach: Traversing list and using copy of that list for modification

"""

class Solution:
    def rotate(self, arr):
        last = arr[-1]

        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]

        arr[0] = last

"""
Time:  O(n)
Space: O(1)

Approach: standard in-place shifting, right shift, move right → left.

"""
