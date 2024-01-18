def gcd(array):
    sorted_list = sorted(array)
    target = sorted_list[0]
    stack = set()
    return_list = []
    for i in range(1, target//2+1):
        if target % i == 0:
            stack.add(i)
            stack.add(target//i)
    stack = sorted(list(stack))
    while stack:
        flag = False
        top = stack.pop()
        for item in array:
            if item % top != 0:
                flag = True
                break
        if not flag:
            return_list.append(top)
    
    return sorted(return_list)
        
def checker(gcd_list, array):
    while gcd_list:
        flag = False
        gcd = gcd_list.pop()
        for item in array:
            if item % gcd == 0:
                flag = True
                break
        
        if not flag:
            return gcd
    return 0
    
def solution(arrayA, arrayB):
    answer = 0
    a_gcd_list = gcd(arrayA)
    a_gcd = checker(a_gcd_list, arrayB)
    b_gcd_list = gcd(arrayB)
    b_gcd = checker(b_gcd_list, arrayA)
    answer = max(a_gcd, b_gcd)
        
    
    return answer