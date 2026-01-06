# Challenge 2: Password Recovery Window

# Log string
log = "a"

# Pattern String
pattern = "aa"

def Minimum_Window_Substring1(log:str , pattern:str) -> str:
    """Complexity Analysis
    Approach : Brute Force
    Time Complexity : O(n x (m² + n)) 
    Space Complexity : O(n)  -> Linear 

    here m = len(pattern)

    """


    if len(log) < len(pattern): return ""
    
    all_sub_str = {}
    n = len(log) 

    for i in range(n):
        sub_str = ""
        str_dict = {}
        for j in range(len(pattern)):
            str_dict[f"{pattern[j]}"] = pattern.count(pattern[j])
        count = 0
        for k in range(i,n):
            if log[k] not in str_dict:
                str_dict[log[k]] = -1

            if (log[k] in pattern and str_dict[log[k]] > 0):
                count +=1
                str_dict[log[k]] -= 1
            else:
                str_dict[log[k]] -= 1
            sub_str += log[k]

            if count == len(pattern):
                all_sub_str[i] = len(sub_str)        
                break

    minlen_str_lst = []

    for k,v in all_sub_str.items():
        minlen_str_lst.append(v)

    if not minlen_str_lst: return ""
    length = min(minlen_str_lst)
    idx = 0

    for k,v in all_sub_str.items():
        if v == length:
            idx = k
            break

    return log[idx:idx+length]

        
def Minimum_Window_Substring2(log : str, pattern : str) -> str:
    """ Complexity Analysis
    Approach : Optimal Solution
    Time Complexity : O(n + m) -> Linear
    Space Complexity : O(m) 

    here m = len(pattern)

    """
        
    if len(log) < len(pattern):
        return ""

    str_dict = {}
    for ch in pattern:
        str_dict[ch] = str_dict.get(ch, 0) + 1

    required = len(pattern)
    count = 0

    left = 0
    min_len = float('inf')
    start = 0

    for right in range(len(log)):
        if log[right] in str_dict:
            if str_dict[log[right]] > 0:
                count += 1
            str_dict[log[right]] -= 1

        while count == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                start = left

            if log[left] in str_dict:
                str_dict[log[left]] += 1
                if str_dict[log[left]] > 0:
                    count -= 1
            left += 1

    if min_len == float('inf'):
        return ""

    return log[start:start + min_len]


print(f"Input:  log = '{log}', pattern = '{pattern}'")
print(f"Brute Force : {Minimum_Window_Substring1(log,pattern)}")
print(f"Optimal : {Minimum_Window_Substring2(log,pattern)}")

