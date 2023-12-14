import sympy 
from numpy import linalg as LA
A=10000/3
B=-5000/3
from sympy import *

m = Matrix([[A,B,B],  [B,A,A], [B,B,A]]) 
M = [[A,B,B],  [B,A,B], [B,B,A]]


e, V=LA.eig(M)
print(V)
coords=sqrt(5000)*V
print(coords)
#print("Matrix : {} ".format(M))

                                                                                                     
# Use sympy.eigenvects() method  
#M_eigenvects = M.eigenvects()   

#print("Eigenvects of a matrix : {}".format(M_eigenvects))   