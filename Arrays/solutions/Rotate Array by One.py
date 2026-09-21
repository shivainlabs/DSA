# "https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?utm=codolio"

class Solution:
    def rotate(self, arr):
        last = arr.pop() # O(1)
        arr.insert(0,last) # O(n) Because of shifting the elements
        return arr
        
        
"""
T.C -> O(n)
S.C -> O(1)

Approach: Remove the last element from an array and insert it,
at the begining, and return modified array

"""