def list1_start_with_list2(list1, list2):
    ans = True
    if(len(list2) == 0 and len(list1) != 0):
        ans = False
    if(len(list1) < len(list2)):
        ans = False
    else:
        for i in range(len(list2)):
            if(list1[i] != list2[i]):
                ans = False
                break
    return ans

#print(list1_start_with_list2([], []))

#Problem 2 #note this function takes 2 list and works with the larger one (contrary to instructions)
def match_pattern(list1, list2):
    if len(list1)==0 and  len(list2)==0:
        return True
    
    
    if len(list1) >= len(list2):
        maxList = list1
        minList = list2
    else:
        maxList = list2
        minList = list1
    if(len(minList) == 0):
        return False

    i = 0
    while( i < len(maxList) - len(minList) + 1): #condition for i < len(lista) - len(listb)
       
        if maxList[i: i+len(minList)] == minList:
           return True
        i += 1

    return False

#print(match_pattern([4,20,100], [4,20,100]))
    


def repeats(list0):
    ans = False
    if(len(list0) <= 1):
        return ans
    for i in range(len(list0) - 1):   # i goes from the first element to the second last element of the list
        if(list0[i] == list0[i+1]):   # comparing the current and next element of the list
            ans = True
    return ans

#print(repeats([20, 30, 50, 50]))

def print_matrix_dim(M):
    m = len(M)
    n = len(M[0])
    print(m, 'x', n)

M = [[0]]
#print_matrix_dim(M)
def mult_M_v(M, v):
    n = len(M[0])
    new_vec = []
    m= len(M)
    size = len(v)
    if(n == size):
        
        for i in range(m):
            sum = 0
            for j in range (n):
                sum += M[i][j] * v[j]

            new_vec.append(sum)
                         
               
    else:
        print("Dimensions do not match. Multiplication not possible")
    return new_vec
    
#print(mult_M_v([[1,2,3], [4,5,6]], [1,2,3]))

def matrix_mult (A, B):
    print("ask prof cluett")
    s = len(B[0])
    r = len(B)
    p = len(A)
    q = len(A[0])
    AB = [[0 for a in range(s)]for b in range(p)]
    
    if(q == r):    #p x s matrix output
        for i in range(p):
            for j in range(s):
                sum = 0
                for x in range(q):
                    sum += A[i][x] * B[x][j]
                    #print(sum)
                #print(sum)
                AB[i][j] = sum
                #print(AB)
                        #AB[i][j] += A[i][x] * B[x][j]
    return AB

#print(matrix_mult([[1,2],[3,4]], [[8,9], [10,11]]))
print(matrix_mult([[1,2,3],[4,5,6]], [[7,8], [9,10], [11,12]]))
    initialize()
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("textbooks")
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("resting", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 130)
    print(get_cur_health())
    print(get_cur_hedons())