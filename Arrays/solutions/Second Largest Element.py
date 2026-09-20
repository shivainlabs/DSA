# https://takeuforward.org/plus/dsa/problems/second-largest-element?utm=codolio

"""
TC: O(n) 
SC: O(1)

Approach: 

Maintain two variables, first_largest and second_largest.
Traverse the array once and update these variables whenever
a larger or second-largest distinct element is found.


"""

class Solution:
    def secondLargestElement(self, nums):
        first_largest = float('-inf')
        second_largest = float('-inf')

        for x in nums:
            print(x,first_largest,second_largest)
            if x > first_largest:
                second_largest = first_largest
                first_largest = x                
        
            if (x > second_largest) and (x != first_largest):                
                second_largest = x
            
        return -1 if second_largest == float('-inf') else second_largest

