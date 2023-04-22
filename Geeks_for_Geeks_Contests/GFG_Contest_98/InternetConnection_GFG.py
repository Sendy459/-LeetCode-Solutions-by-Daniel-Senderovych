import copy
from typing import List

# Alice, a network engineer, is tasked with determining
# whether the preinstalled WiFi in her office covers the
# entire office area or not. The office area is represented
# by a 2D matrix of size N*N containing binary numbers,
# with 0 indicating the office area and 1 representing the
#  location of the WiFi. In addition, a rang integer is
#  given to indicate the coverage range of the WiFi given
#  in Eight directions.
# Help Alice to return true if given router are enough to
# determine that internet is available to whole office
# premises else return false.

def internetCoverage(range_: int, n: int, wifi: List[List[int]]) -> bool:
    def check(i, j):
        if i < 0 or i >= n or j < 0 or j >= n:
            return
        wificopy[i][j] = 1
    wificopy = copy.deepcopy(wifi)
    for i in range(n):
        for j in range(n):
            if wifi[i][j] == 1:
                for x in range(i - range_ + 1, i + range_):
                    for y in range(j - range_ + 1, j + range_):
                        check(x, y)

    for i in range(n):
        for j in range(n):
            if wificopy[i][j] == 0:
                return False
    return True
       
#Example 1:

# range_ = 2
# n = 3
# wifi = [[0, 0, 1],
#         [0, 0, 0],
#         [1, 0, 0]]

# Output : 
# False

# Explaination : 
# After calculating the internet coverage
# of the wifi, we will get the matrix as 
# wifi = [[0, 1, 1]
#        ,[1 ,1 ,1],
#         [1, 1, 0]],
# we can see that wifi is not covering all
# the area, hence we return False.

#Example 2:
# range_ = 2 
# n = 2  
# wifi = [[1, 0],
#         [0, 1]]
#Output : 
# True

# Explaination : 
# After calculating the internet coverage of
# the wifi, we will get the matrix as 
# wifi = [[1, 1],
#         [1 ,1]], 
# we can see that wifi is covering all the
# area, hence we return True.

# print(internetCoverage(range_, n, wifi))