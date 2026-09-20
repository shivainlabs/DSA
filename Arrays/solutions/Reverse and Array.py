# https://www.geeksforgeeks.org/problems/reverse-an-array/1


"""
T.C -> O(n/2) ~ O(n)
S.C -> O(1)

Approach: 

Use two pointer one is at the begining and second at the end, swaping each other
move i forward and j backward until they meet each other

"""

class Solution:
    def reverseArray(self, arr):
        # code here
        i = 0
        j = len(arr)-1
        
        while i < j:
            # arr[j],arr[i] = arr[i],arr[j]
            
            val = arr[i]
            arr[i] = arr[j]
            arr[j] = val
            
            i += 1
            j -= 1        