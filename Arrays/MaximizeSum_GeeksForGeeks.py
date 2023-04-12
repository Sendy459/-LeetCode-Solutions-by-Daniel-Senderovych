def maximumSum(n, A):
    B = A.sort()
    max_sum = 0
    for i in range(n):
        max_sum += (i+1) * A[i]
    return max_sum

# Problem Description:
# You are given an array A of size N.
# Your goal is to construct an array B of size N where
# B[i] = i * A[i] for all 1 ≤ i ≤ N.
# However, before constructing array B, you can swap the 
# elements of array A at most N^2 times (possibly 0 times).
# Your task is to find the maximum possible sum
# of the elements in array B after performing such operations.

# Input Example:
n = 2
A = [2 ,1]
# Output :
# 5
# Explaination :
# If we do not swap the elements the sum is 2*1 + 1*2 = 4
# But if we swap the sum is 1*1 + 2*2 = 5

# Input :
# n = 3
# A = 1 1 1
# Output :
# 6
# Explaination :
# The maximum sum possible is 6 after even after swapping any number of times.
print(maximumSum(n, A))