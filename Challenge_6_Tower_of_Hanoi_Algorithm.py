# Challenge 6: Tower of Hanoi Algorithm


def towerOfHanoi(N : int, from_rod : str, to_rod : str, aux_rod : str) -> None:
    """ Complexity Analysis
        Approach : Optimal Approach
        Time Complexity : O(2^n) -> Exponential
        Space Complexity : O(n) -> Linear
    """
    if N == 1:
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return
    
    towerOfHanoi(N - 1, from_rod, aux_rod, to_rod)
    print(f"Disk {N} moved from {from_rod} to {to_rod}")
    towerOfHanoi(N - 1, aux_rod, to_rod, from_rod)

N=4
print(f"Input : N = {N} ")
towerOfHanoi(N, "A", 'C', 'B')