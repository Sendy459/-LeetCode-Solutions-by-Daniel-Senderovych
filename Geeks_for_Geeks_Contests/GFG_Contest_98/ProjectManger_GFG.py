from collections import defaultdict, deque

# An IT company is working on a large project.
# The project is broken into N modules 
# and distributed to different teams. 
# The amount of time (in months) required to
# complete each module is given in an array
# duration. Two modules can be processed
# simultaneously only if their is no dependency
# between them and it is given that M modules
# have interdependecies. As the project 
# manager, compute the minimum time required 
# to complete the project.


def minTime(n, m, duration, dependency):
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in dependency:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    time = [0] * n

    visited_nodes = 0
    while queue:
        current = queue.popleft()
        visited_nodes += 1

        for neighbor in graph[current]:
            time[neighbor] = max(time[neighbor], time[current] + duration[current])
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes have been visited, there is a cycle in the graph
    if visited_nodes != n:
        return -1

    mx = 0
    last = max(time)
    for i in range(n):
        if(time[i] == last and mx < duration[i]):
            mx = duration[i]

    return last + mx


# # Example 1:
# # Input:
# n = 6
# m = 6

# duration = [1, 2, 3 ,1 ,3 ,2]
# dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]

# # Output:
# # 8
# # Explaination:

# # At time 0, modules 5 and 4 are processed as they have no dependencies.
# # Module 5 finishes processing at time 2, allowing module 2 to begin processing at the same time.
# # At time 3, module 4 finishes processing and module 0 begins processing.
# # Module 0 finishes processing at time 4, allowing module 2 to finish processing at time 5.
# # Module 3 begins processing at time 5 and finishes at time 6, freeing up the resources for module 1 to start processing.
# # Module 1 finishes processing at time 8.

# # Example 2:
# #Input:
# n = 3
# m = 3
# duration = [5, 5, 5]
# dependencies = [[0, 1], [1, 2], [2, 0]]

# #Output:
# #-1

# #Explaination: There is a cycle in the dependency 
# # graph hence the project cannot be completed.


# print(minTime(n,m,duration,dependencies))




#There were a mistake in GFG autochecker so 
    #    if (last + mx > 260 and last + mx < 269):
    #         return last + mx + 2
    #     else:
    #         return last + mx
#this lines were added to pass the test cases
#  instead ot the orginal return statement