#1

def count_evens(L):
    count = 0
    for num in L:
        if num % 2 == 0:
            count += 1
    return count

#print(count_evens([1,2,7,9,10]))



#2
def list_to_str(lis):
    string = "["
    length = len(lis)
    if length == 0:
        string += "]"
    else:
        for i in range (length):
            if i == length-1:
                string += str(lis[i]) + "]"
            else:
                string += str(lis[i]) + ", "
    return string

#print(list_to_str([]))




#3
def lists_are_the_same(list1, list2):
    same = True
    if(len(list1) != len(list2)):
        same = False
    else:
        for i in range(len(list1)):
            if(list1[i] != list2[i]):
                same = False
                break
    return same

#print(lists_are_the_same([], []))

#4
def simplify_fraction(n,m):
    i = 1
    gcd = 1
    while(i<= n and i<=m):
        if(n % i == 0 and m % i == 0):
            gcd = i


        i += 1
    print(str(n//gcd) + "/" + str(m//gcd))
#simplify_fraction(5,7)



#5

#problem 3 from lab 3



import math
PI = math.pi

def sum_more_pi(n):
    ref = int(PI*(10**n))
    count = 1
    ans = (-1)**0/(2*0+1)
    while ref != int(4*ans*(10**n)):

        count += 1
        ans += (-1)**((count-1))/(2*(count-1)+1)
        #print(ans)
    return (count-1)
test = 5
print(int(PI*(10**test)))
a =sum_more_pi(test)
print(a)

x = 0
tot = 0

while x<=a:

    tot += (-1)**x/(2*x+1)
    x += 1

p = 4*tot
print(p)



#6

def euclid_iterative(a,b):
    r = a % b
    while(r!=0):
        a = b
        b = r
        r = a % b
    return b

def euclid(a,b):

    r = a % b
    if(r==0):
        return b
    else:
        a = b
        b = r
        return euclid(a, b)

#print(euclid_iterative(710, 50))

