#Problem 1
'''
import lab02
if __name__ =='__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
'''

#Problem 2
def check_sum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i **3
    total2 = n**2 * (n+1)**2 / 4
    if total == total2:
        return True
    else:
        return False

def check_sums_up_to_n(N):
    isAllTrue = True
    for i in range(1, N+1):
        boo = check_sum(i)
        isAllTrue = isAllTrue and boo
        if not isAllTrue:
            break
    return isAllTrue

#print(check_sums_up_to_n(109))

#Problem 3
x = 0
tot = 0

while x<=1000:

    tot += (-1)**x/(2*x+1)
    x += 1

pi = 4*tot
print(pi)
