import heapq

def minimizeComputers(n, k, arr):  
    #define the binary search function to find the minimum number of computers
    def binary_search(left, right):
        while left <= right:
            mid = (left + right) // 2
            if can_complete(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    # define the function to check if it is possible to complete the exam using X computers
    def can_complete(X):
        heap = []
        for i in range(X):
            heapq.heappush(heap, 0)
        for time in arr:
            min_time = heapq.heappop(heap)
            min_time += time
            if min_time > k:
                return False
            heapq.heappush(heap, min_time)
        return True

    #perform the binary search to find the minimum number of computers
    return binary_search(1, n)


# Input :
# n = 4
# k = 5
# A = [2, 1, 2, 1]

## Output :
# 2

## Explaination :
## Geek has 2 computers and at time t=0, 1st and 2nd students comes to give the exam on C1 and C2 respectively (C1 and C2 is computer 1 and computer 2). 
## Third student comes at t=1 on C2 after 2nd student finishes. 
## At t=2 first student finishes and 4th student comes on C1. 
## At t=3 both 3rd and 4th student finishes the exam. 
## It can be shown that it is not possible to finish the exam with 1 computer in 5 units of time.

# # Input :
# n = 4
# k = 6
# A = [3, 4, 5, 3]

# # Output :
# # 3

# # Explaination :
# # At time t=0 first, second and third student sits on computer.
# # At time t=3 first student completes and 4th student sits.
# # At time t=6 everyone has completed the exam.
# # It can be shown that we require atleast 3 computers to complete the exam in required time.

# print(minimizeComputers(n, k, A))