#Needed for array() and dot()
from numpy import *


#Printing matrices using NumPy:

#Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = array(M_listoflists)
#Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = array([[1,-2,3],[3,10,1],[1,5,3]])
x = array([75,10,-11])
b = dot(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

#To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def print_matix(M_lol):
    M = array(M_lol)
    print(M)

def lead_ind(row):
    for elem in range(len(row)):
        if row[elem] != 0:
            return elem
    return len(row)

def get_row_to_swap(M, start_i):
    min = lead_ind(M[start_i])
    mini = start_i
    for i in range(start_i, len(M)):
        a = lead_ind(M[i])
        if(a < min):
            min = a
            mini = i
    return mini

def add_rows_coefs(r1, c1, r2, c2):
    new_row = [0]*len(r1)
    for i in range(len(r1)):
        new_row[i] = c1*r1[i] + c2*r2[i]
    return new_row

def eliminate(M, row_to_sub, best_lead_ind):
    temp_row = []
    for i in range(len(M[row_to_sub])):
        temp_row.append(M[row_to_sub][i] / M[row_to_sub][best_lead_ind])
    for i in range(row_to_sub+1, len(M)):
        if (M[i][best_lead_ind] != 0):
            temp = add_rows_coefs(temp_row,-M[i][best_lead_ind], M[i], 1)
            M[i] = temp

def eliminatereverse(M, row_to_sub, best_lead_ind):
    temp_row = []
    for i in range(len(M[row_to_sub])):
        temp_row.append(M[row_to_sub][i] / M[row_to_sub][best_lead_ind])
    for i in range(row_to_sub+1, len(M)):
        if (M[i][best_lead_ind] != 0):
            temp = add_rows_coefs(temp_row,-M[i][best_lead_ind], M[i], 1)
            M[i] = temp

def forward_step(M):
    print("Starting Forward step")
    starti = 0
    while(starti < min(len(M), len(M[0]))): # or other condition):
        current_rownum = get_row_to_swap(M, starti)
        M[starti],  M[current_rownum] = M[current_rownum], M[starti]  
        print("swapping row " + str(current_rownum) + " with row " + str(starti))
        print_matix(M) 
        if(lead_ind(M[starti]) != len(M[starti])):
            eliminate(M, starti, lead_ind(M[starti]))
            print("eliminating elements in column " + str(lead_ind(M[starti])))
            print_matix(M) 
        starti += 1
    
# M = [[2,3], [3,4]]
# print(M)
# eliminate(M, 0, 0)
# print(M)
#forward_step(M_listoflists)

#N = [[ 0,  0,  1,  0,  2],[ 1,  0,  2,  3,  4],[ 3,  0,  4,  2,  1],[ 1,  0,  1,  1,  2]]
#forward_step(N)
#N = [[1,2,], [5,7], [10, 30]]
#forward_step(N)

def backward_step(M):
    print("Starting Backward step")
    #N = []
    #Efor i in range(len(M)-1, -1 ,-1):
        #N.append(M[i])
    
    starti = 0 #min(len(M), len(M[0])-1
    while starti < min(len(M), len(M[0])): #make >= if needed
        M.reverse()
        lead_pos = lead_ind(M[starti])
        if(lead_pos != len(M[starti])):
            eliminate(M, starti, lead_pos)
            M.reverse()
            print("eliminating elements in column " + str(lead_pos))
            print_matix(M)
            
        else:
            M.reverse()
        starti += 1
        #M.reverse()
  #  M.reverse()
    print("Now dividing every row by its leading coefficient")
    for i in range(len(M)):
        a = lead_ind(M[i])
        if(a!= len(M[i])):
            b = M[i][a]
            if(a<len(M[0])) :
                for j in range(len(M[i])):
                # print(len(M[i]))
                    M[i][j] /= b
                    #print(M[i][j]/b)
    print_matix(M)

N2 = [[  1,  -2,   3,  22],[  3,  10,   1, 314],[  1,   5  , 3 , 92]]
forward_step(N2)
backward_step(N2)
#print(M_listoflists)
#M_listoflists[0], M_listoflists[1] = M_listoflists[1] , M_listoflists[0]
#print(M_listoflists)
# N = [[1,2], [5,7], [10, 49]]
# forward_step(N)
# backward_step(N)

def solve(M, b): #Solves Mx = b
    orig = array(M)
    for i in range(len(M)):
        M[i].append(b[i])
    forward_step(M)
    backward_step(M)
    ans = [0] * (len(M[0])-1)
    all_zero = [0]*len(M[0])
    all_0_except_last = [0] * (len(M[0])-1)
    # for i in range(len(M)-1, -1, -1):
    #     if(M[i] == all_zero):
    #         #ans.append(0) # Free variable so remains 0
    #     elif (M[i][0:len(M[0])-1] == all_0_except_last ):
    #         return "No Solution"
        
    #     else:
    #         #ans.append(M[i][len(M[0])])
    #         ans[i] = M[i][len(M[0])]
    #ans.reverse()
    for i in range(len(M)):
        currentvar = lead_ind(M[i])
        if(currentvar < len(M[0]) and M[i][currentvar] == 1):
            ans[i] = M[i][len(M[0]) -1]
        elif(M[i] == all_zero):
            ans[i] = 0
        elif(M[i][0:len(M[0])-1] == all_0_except_last):
            return "No Solution"
    print("x = ")
    print(ans)
    print("Verifying that Mx = b.")
    check = dot(orig, array(ans))
    print("Mx:")
    print_matix(check)
    print("b:")
    print(b)
    return ans

N3 = [[1,-2,3], [3,10,1], [1,5,3]]
b = [22,314,92]
solve(N3, b)

N4 = [[1,2,3,4], [1,3,1, 15]]
b = [15,19]
solve(N4, b)

