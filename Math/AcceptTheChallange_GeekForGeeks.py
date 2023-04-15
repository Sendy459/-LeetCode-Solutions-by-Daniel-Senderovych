# Geekina gave Geek a challenge, she asked Geek to choose any positive number (say x) and perform the operation at least twice - 
# Add x to your current score and double the value of x. 
# The challenge here is you must perform the above operation at least twice and after performing the above operation your score should be exactly k. 
# Could you help Geek by giving him largest x to start with or return -1 if such x does not exist? 
# Note: Initially the score is 0


# # easy solution
# def acceptTheChallenge(k):
#     n = k//3
#     for i in range(n, 0, -1):
#         score = 0
#         x = i
#         while(score < k):
#             score += x
#             x *= 2
#             if(score == k):
#                 return i
#     return -1
            
## advanced solution
# score = x + 2 * (x + 2 * (x + ... + 2 * (x + 2 * 0)))
#       = x + 2 * (x + 2 * (x + ... + 2 * x))
#       = x + 2 * (x * (2^n - 1))
#       = x * (2^(n+1) - 1)


def acceptTheChallenge(k):
    n = 2
    while True:
        divisor = 2**n - 1
        if divisor > k:
            return -1
        elif k % divisor == 0:
            x = k // divisor
            if x <= k // 3:
                return x
        n += 1
        
print(acceptTheChallenge(8))
# Output:
# -1

# Explanation:
# It can be shown that there does not exist any x that can help Geek to have a score of exactly 8.
print(acceptTheChallenge(7))
# Output:
# 1

# Explanation:
# Geek will choose x = 1 and do the following operations - 
# Add 1 to score and double x. Therefore x = 2 and Score = 1
# Now add 2 to score and double x. Therefore x = 4 and Score = 3
# Now add 4 to the score and double x. Therefore x = 8 and Score = 7.
print(acceptTheChallenge(28))
print(acceptTheChallenge(33))