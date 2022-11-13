def solution(topping):
    result = 0
    i = 0
    while i != len(topping):

        i0 = topping[:i]
        i1 = topping[i:]
        
        if len(set(i0)) == len(set(i1)):
            result += 1
            topping = list(set(i0)) + i1
            
            i -= len(i0) - len(set(i0))
            
        i += 1
        
    return result
