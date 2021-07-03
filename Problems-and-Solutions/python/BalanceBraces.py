# check for balanced braces for strings (only contains (), [],{})in a list
# returns a list of "YES" - for balanced and "NO" for not balanced

def checkBraces(values):
    result = []
    for value in values:
        value = list(value)
        stack = []
        for i in value:
            if len(stack) == 0:
                stack.append(i)
            elif i == ')':
                if stack[-1] != '(':
                    result.append("NO")
                    break
                else:
                    stack.pop()
            elif i == ']':
                if stack[-1] != '[':
                    result.append("NO")
                    break
                else:
                    stack.pop()
                    
            elif i == '}':
                if stack[-1] != '{':
                    result.append("NO")
                    break
                else:
                    stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            result.append("YES")
    if len(result) == 0:
        result.append("YES")        
    return result


            
                    
                    
                    
                    
            
        
        

