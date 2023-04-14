
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
                
def destroyTheGarden( n, m, arr, overlapped):
    uf = UnionFind(n)

    for i, j in overlapped:
        uf.union(i, j)

    # Group plants by their root
    groups = {}
    for i in range(1, n + 1):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    total_poison = 0
    # Find the maximum poison for each group thats 
    # enough to destroy all plants in the group
    for group in groups.values():
        max_poison = 0
        for plant in group:
            if arr[plant - 1] > max_poison:
                max_poison = arr[plant - 1]
        total_poison += max_poison

    return total_poison

    
# #Input:
# N = 5
# M = 2
# arr = [2, 3, 4, 5, 6]
# overlapped = [ [1, 5],
#                [3, 4]]

# #Output:
# #14

# #Explanation:
# #6 units of poison can destroy the first and the last plant,
# #3 units of poison can destroy the 2nd plant and 
# #5 units of poison can destroy the 3rd and the 4th plant.


# # Input:
# N = 4
# M = 3
# arr = [1, 2, 3, 4]
# overlapped = [[1, 2], [2, 3], [3, 4]]

# # Output:
# # 4

# # Explanation:
# # Geek can destroy the 4th plant with 4 units of poison and since it overlaps with the 3rd plant it also gets destroyed.
# # Now, when the third plant gets destroyed it also destroys the 2nd plant since it overlaps with third and requires less poison.
# # Similarly upon destroying second plant will also destroy the first one.

# N = 9
# M = 20
# arr = [4, 1, 0, 0, 0, 3, 3, 9, 9]
# overlapped = [    [5, 8], [8, 9], [2, 5], [6, 9], [3, 8], [3, 6], [7, 8], [4, 9], [6, 7],
#     [4, 5], [2, 9], [3, 4], [5, 9], [4, 6], [4, 7], [4, 8], [2, 6], [1, 3],
#     [2, 4], [3, 5]
# ]
#print(destroyTheGarden(N, M, arr, overlapped))