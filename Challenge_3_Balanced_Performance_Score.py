# Challenge 3: Balanced Performance Score

# Scores Array of Team A
scoresA = [1,3]

# Scores Array of Team B
scoresB = [2]


def findMedianSortedArrays(scoresA : list, scoresB : list) -> float :
    """Complexity Analysis
    Approach : Average
    Time Complexity : O(m + n) -> Linear
    Space Complexity : O(1) -> Constant

    Here m = length of Team B's Array
    Here n = length of Team A's Array

    """

    n, m = len(scoresA), len(scoresB)
    total = n + m

    i = j = 0
    count = 0

    prev = curr = 0

    while count <= total // 2:
        prev = curr

        if i < n and (j >= m or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1

        count += 1

    if total % 2 == 0:
        return (prev + curr) / 2
    else:
        return curr
    
print(f"Input:  scoresA = {scoresA}, scoresB = {scoresB}")
print(f"Median : {findMedianSortedArrays(scoresA,scoresB)}")