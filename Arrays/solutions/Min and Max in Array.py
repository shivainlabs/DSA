"https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1"

class Solution:
    def getMinMax(self, arr):
        # code here
        maxi = arr[0]
        mini = arr[0]
        
        for x in arr[1:]:
            if x > maxi:
                maxi = x
            if x < mini:
                mini = x
        
        return [mini,maxi]
        

"""

T.C -> O(n)
S.C -> O(1)

Approach : Storing two variable, and traverse the array updating our
variables accordingly


"""