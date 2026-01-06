# Challenge 1: Team Contribution Multiplier

# Contributions Array
contributions = [-1, 1, 0, -3, 3]


def Calculate_Contributions1(contributions:list) -> list:
    """Complexity Analysis
    Approach : Brute Force
    Time Complexity : O(n^2) -> Quadratic 
    Space Complexity : O(n)  -> Linear 
    """
    
    impact = []

    for i in range(len(contributions)):
        product=1
        for j in range(len(contributions)):
            if i == j:
                continue
            else:
                product*=contributions[j]
        impact.append(product)

    return impact

def Calculate_Contributions2(contributions:list) -> list:
    """Complexity Analysis
    Approach : Average
    Time Complexity : O(n)  -> Linear
    Space Complexity : O(n) -> Linear
    """
    
    n = len(contributions) 
    impact = [1]*n

    prefix_arr = [1]*n
    prefix = 1
    for i in range(1,n):
        prefix_arr[i] = contributions[i-1] * prefix
        prefix = prefix_arr[i]

    suffix_arr = [1]*n
    suffix = 1
    for j in range(n-2,-1,-1):
        suffix_arr[j] = suffix * contributions[j+1]
        suffix = suffix_arr[j]

    for k in range(n):
        impact[k] = prefix_arr[k] * suffix_arr[k]

    return impact

def Calculate_Contributions3(contributions:list) -> list:
    """Complexity Analysis
    Approach : Optimal / Best 
    Time Complexity : O(n)  -> Linear
    Space Complexity : O(1) -> Constant
    """
    
    n = len(contributions)
    impact = [1]*n

    prefix = 1
    for i in range(1,n):
        impact[i] *= prefix * contributions[i-1]
        prefix = impact[i]

    suffix = 1
    for j in range(n-2,-1,-1):
        suffix *= contributions[j+1]
        impact[j] *= suffix

    return impact

print(f"Contributions : {contributions}")
print(f"Brute Force Approach : {Calculate_Contributions1(contributions)}")
print(f"Average Approach : {Calculate_Contributions2(contributions)}")
print(f"Optimal Approach : {Calculate_Contributions3(contributions)}")

