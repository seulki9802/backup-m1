def check(topping, result, i, d):
    while 1:
        i += d*1
        
        cake1 = set(topping[:i])
        cake2 = set(topping[i:])
        
        if len(cake1) != len(cake2):
            return result
        else:
            result += 1
        
def solution(topping):
    result = 0
    
    i = int(len(topping) / 2)
    d = 0
    while 1:
        
        cake1 = set(topping[:i])
        cake2 = set(topping[i:])

        # stop
        if d > 0 and len(cake1) > len(cake2):
            return 0
        elif d < 0 and len(cake1) < len(cake2):
            return 0

        # get direction
        if len(cake1) > len(cake2):
            d = -1
        elif len(cake1) < len(cake2):
            d = +1

        else:
            # find!
            result += 1
            
            if d==0:
                result1 = check(topping, result, i, -1)
                result2 = check(topping, result, i, 1)
                return result1 + result2
                
            else:
                print("?")
                return check(topping, result, i, d)

        i += d*1


topping = [1, 2, 3, 1, 4]
a = solution(topping)
print(a)