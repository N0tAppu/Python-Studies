'''
def indentity(arr,r,c):
    for i in range (0,r):
        for j in range(0,c):
            if arr[i][i] != 1:
                return 0
    for i in range (0,r):
        for j in range(0,c):
            if i != j:
                if arr[i][j] != 0:
                return 0
    return 1  

r = int(input("Enter no of rows: "))
c = int(input("Enter no of Cols: "))
if r != c:
    print("Matrix dimension invlaid for Identity Check!")
    exit()
else:
    arr = []
    for i in range (r):
        inner =[]
        for j in range(c):
            n = int(input(f"Enter Element {i}{j}: "))
            inner.append(n)
        arr.append(inner)
    flag = indentity(arr,r,c)
    if flag >=1:
        print("Your Matrix is an Identity Matrix!")
    else:
        print("Your Matrix is not an Identity Matrix!")
'''

#upper triangular matrix

def mat(arr,r):
    Upper = True
    Lower = True
    for i in range(r):
        for j in range(r):
            if i>j  and arr[i][j] != 0:
                Upper = False
            elif j> i and arr[i][j]!=0:
                Lower = False
    if Upper == True and Lower == False:
        return "Your Matrix is A Upper Triangular Matrix"
    elif Upper == False and Lower == True:
        return "Your Matrix is a Lower Triangular Matrix"
    elif Upper == True and Lower == True:
        identity = True
        Diagonal = True
        for i in range(r):
            if arr[i][i] != 0:
                identity = False
                Diagonal = True
            else:
                identity= True
                Diagonal = False
        if identity==True:
            return "Your Matrix is an Identity Matrix"
        elif Diagonal == True:
            return "Your Matrix is a Diagonal Matrix"
    else:
        return "This is a normal Square Matrix"

arr = []
r = int(input("Enter No of Rows:"))
c = int(input("ENter no of Cols: "))
if r !=c:
    print("Operation can be only done on a Square Matrix!")
    exit()
else:
    for i in range(r):
        inner = []
        for j in range(c):
            n = int(input(f"Enter Element A[{i}][{j}]: "))
            inner.append(n)
        arr.append(inner)
    print("Your Matrix:")
    for row in arr:
        print(row)
    print(mat(arr,r))





        

                 

    