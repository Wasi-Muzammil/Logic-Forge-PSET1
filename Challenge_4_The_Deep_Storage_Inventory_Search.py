# Challenge 4 : The Deep Storage Inventory Search

# imported Due to Heap Implementation
import heapq as pq

# Matrix to find Kth Element
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8


def KthSmallestElement1(matrix: list[list[int]] , k: int) -> int:
    """Complexity Analysis
    Approach : Brute Force
    Time Complexity : O(n^2 log(n^2)) 
    Space Complexity : O(n^2) 

    """
     
    array = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            array.append(matrix[i][j])
    array.sort()
    return array[k-1]


def KthSmallestElement2(matrix: list[list[int]], k: int) -> int:
    """Complexity Analysis
    Approach : Average But can be Improved
    Time Complexity : O(n^2 log(k)) 
    Space Complexity : O(k) 

    where k = smallest element in the matrix

    """
    heap = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pq.heappush(heap, -matrix[i][j]) 
            if len(heap) > k:
                pq.heappop(heap)

    return -heap[0]  


def count_less_equal(mid : int,n : int) -> int:
        """Complexity Analysis
            HELPER FUNCTION
        Time Complexity : O(n) 
        Space Complexity : O(1) 

        """
        count = 0
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count


def kthSmallestElement3(matrix : list[list[int]], k) -> int:
    """Complexity Analysis
    Approach : Optimal Solution
    Time Complexity : O(n x RANGE) 
    Space Complexity : O(1) 

    where RANGE = log(max - min)

    """
    n = len(matrix)

    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    while low < high:
        mid = low + (high - low) // 2

        if count_less_equal(mid,n) < k:
            low = mid + 1
        else:
            high = mid

    return low


print(f"Input: matrix = {matrix}, k = {k}")
print(f"Kth smallest Element Using Brute Force : {KthSmallestElement1(matrix,k)}")
print(f"Kth smallest Element Using Heap : {KthSmallestElement2(matrix,k)}")
print(f"Kth smallest Element Using Binary Search (Optimal) : {kthSmallestElement3(matrix,k)}")

