#Problem 1
def power(x,n):
    if n == 1:
        return x
    return x * power(x, n-1)

#print(power(1,10))
#Problem 2
def interleave(L1, L2):
    if len(L1) == 1:
        return [L1[0], L2[0]]
    
    return interleave(L1[0:len(L1)-1], L2[0:len(L2)-1]) + [L1[len(L1)-1], L2[len(L2)-1] ]

    
#print(interleave([1,2,-1], [4,3,6]))
# Problem 3
def reverse_rec(L):
    if len(L) == 1:
        return [L[0]]
    return [L[len(L)-1]] + reverse_rec(L[0:len(L)-1])
    
#print(reverse_rec([1,2,3,4,5]))

#Problem 4
def zigzag(L):
    if len(L) == 1:
        return [L[len(L)//2]]
    return zigzag(L[1:len(L)-1]) + [L[0]] + [L[len(L)-1]]

#print(zigzag([1, 2, 3, 4, 5]))



#Problem 5
#t = ")" ()       ")(()"  " " "(well (I think) recursion works like that (as far as I know)""



t = "(well (I think) recursion works )((())like that (as far as I know))"
#"( ( ) ) ( ( ( ) ) ( ) )"

#" (   )"

def is_balanced(s):
    if s.find("(") == -1 and s.find(")") == -1:
        return True
        
    elif  s.find("(") == -1 or s.find(")") == -1:
        return False
    left = s.find("(")  
    right = s.find(")")
    if(left > right):  
        return False
    if right + 1 == len(s):
        
        snew = s[0:left] + s[left+1:right]
    else:
        snew = s[0:left] + s[left+1:right] + s[right+1:]
    return is_balanced(snew)
        
print(is_balanced(t))