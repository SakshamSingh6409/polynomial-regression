import numpy as np
n=int(input("Enter No of Data Points: "))
x=[]
y=[]
i=0
#collecting Data Points
while i<n:
    x.append(float(input(f"\nEnter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))
    i+=1
X=[]
Y=[]
for i in range(n):
    X.append([x**i for x in x])
    Y.append([y[i]])
X=np.linalg.inv(np.linalg.matrix_transpose(X))
Y=np.matrix(Y)
A=X*Y
print(X)
print(Y)
print(A)
#fixing in the below part is required 
print("best polynomial regression fit is: \nY=",end="")
for i in range(n):
    print(f"{A[i][0]}x^{i}",end="")