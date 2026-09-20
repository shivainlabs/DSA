"https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1"

# def segregateElements(arr):
#         # code here
        
#         for i in range(len(arr)):
            
#             j = i
#             while (j>0 and arr[j]>=0 and arr[j-1]<0):
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 j -= 1
#             print("ith",i,"arr",arr)

# if __name__ == "__main__":
#     # arr = list(map(int, input().split()))
#     arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
#     segregateElements(arr)
#     print(*arr)


# Get-Content .\testdata\move_negative\fileInput.txt | python "Move all negative elements to end.py"
# Get-Content .\testdata\move_negative\fileInput.txt | python ".\Move all negative elements to end.py" > .\testdata\move_negative\myOutput.txt


def segregateElements(arr):
    # code here
    pos_arr = []
    neg_arr = []
    
    for i in range(len(arr)):

        if arr[i] >= 0:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])
    
    arr[:] = pos_arr + neg_arr
    print(arr)

if __name__ == "__main__":
    arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
    segregateElements(arr)
    print(*arr)

"""

T.C -> O(n)
S.C -> O(n)

Approach : Auxiliary arrays / partition using two temporary lists


"""
