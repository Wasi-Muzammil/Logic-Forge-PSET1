def RemoveInvalidParentheses(expr: str) -> list:
    """ Complexity Analysis
        Approach : Optimal Approach
        Time Complexity : O(2^n) -> Exponential Due to Recursive DFS BackTracking
        Space Complexity : O(n) -> Linear
    """
    

    left_remove = 0
    right_remove = 0
    for ch in expr:
        if ch == '(':
            left_remove += 1
        elif ch == ')':
            if left_remove > 0:
                left_remove -= 1
            else:
                right_remove += 1

    results = set()

    dfs(expr,results,0, 0, left_remove, right_remove, [])

    return list(results)


def dfs(expr : str, results : set, index : int, left_count : int, left_rem : int, right_rem : int, path : list):
        """
        expr       : Expression String
        results    : set
        index      : current index in expr
        left_count : number of '(' currently kept not yet matched by ')'
        left_rem   : how many '(' still allowed to remove
        right_rem  : how many ')' still allowed to remove
        path       : list of chars for the current built string 
        """

        if index == len(expr):
            if left_rem == 0 and right_rem == 0 and left_count == 0:
                results.add("".join(path))
            return

        ch = expr[index]

        if ch == '(':
            if left_rem > 0 and not (index > 0 and expr[index - 1] == '('):
                dfs(expr, results,index + 1, left_count, left_rem - 1, right_rem, path)

            path.append('(')
            dfs(expr, results,index + 1, left_count + 1, left_rem, right_rem, path)
            path.pop()

        elif ch == ')':
            if right_rem > 0 and not (index > 0 and expr[index - 1] == ')'):
                dfs(expr, results,index + 1, left_count, left_rem, right_rem - 1, path)

            if left_count > 0:
                path.append(')')
                dfs(expr, results,index + 1, left_count - 1, left_rem, right_rem, path)
                path.pop()

        else:
            path.append(ch)
            dfs(expr, results,index + 1, left_count, left_rem, right_rem, path)
            path.pop()


print(RemoveInvalidParentheses("()())()")) 
print(RemoveInvalidParentheses("(a)())()")) 
print(RemoveInvalidParentheses(")("))        
print(RemoveInvalidParentheses("()"))       
print(RemoveInvalidParentheses("abc"))
print(RemoveInvalidParentheses("((("))