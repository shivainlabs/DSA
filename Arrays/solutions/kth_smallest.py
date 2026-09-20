"https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1?utm=codolio"

class Solution:
    def kthSmallest(self, arr, k):
        k = k - 1   # convert to 0-based index

        def partition(low, high):
            pivot = arr[high]
            i = low

            for j in range(low, high):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[high] = arr[high], arr[i]
            return i

        low = 0
        high = len(arr) - 1

        while low <= high:
            p = partition(low, high)

            if p == k:
                return arr[p]
            elif p < k:
                low = p + 1
            else:
                high = p - 1
                
"""
T.C 

Best, Avg, Worst = O(n), O(n), O(n^2)

S.C -> O(1)

Approach: In-place Quickselect using partitioning; 
after each partition, discard the half that 
cannot contain the kth smallest element.


"""