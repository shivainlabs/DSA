# "https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm=codolio"


# def findUnion(a, b):
#     # code here
#     dist = {}
    
#     for x in a:
#         if x not in dist:
#             dist[x] = 1
#         else:
#             dist[x] += 1
    
#     for y in b:
#         if y not in dist:
#             dist[y] = 1
#         else:
#             dist[y] += 1
    
#     return list(dist.keys())


# if __name__=="__main__":
#     a, b = [1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]
#     u = findUnion(a,b)
#     print(u)


        
class Solution:    
    def findUnion(self, a, b):
        # code here
        dist = set()
        
        for x in a:
            dist.add(x)
        
        for y in b:
            dist.add(y)
        
        return list(dist)
        
"""
For both set and dict

T.C -> O(n+m)
S.C -> O(n+m)

Approach : First one use dictionary and second one set

"""