
# What is sparse data: it is the data that has mostly unused elements, like elements that don not carry my info.[1 , 0 , 2 , 0 ,4 ,5 , 6 ,8 ,9 ,1 ,3 , 2]

# Sparse data example : [1 ,0 , 3 ,0 , 0 , 0 , 0 ,9 , 0 , 1 , 0] 
# Dense Array : [1, 2, 3, 4, 2, 1, 8 , 3] 

# How to work with sparse data?
# scipy has as module scipy.sparse function.There are 2 matrices in this sparse:CSC(Compresses sparse column) and CSR(Compresses sparse Row).

# CSR Matrices - here we will create a CSR matrices:

import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([0,0,0,2,0,0,0,1, 0 , 2])
print(csr_matrix(wajahat))

# Sparse matrix Methods:

import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([[0,0,0,] , [0,6,0] ,[1, 0 , 2]])
print(csr_matrix(wajahat).data)

# What if we wants to count non-zeros , we can do this via count_nonzero() method:

import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([[0,0,0,] , [0,6,0] ,[1, 0 , 2]])
print(csr_matrix(wajahat).count_nonzero())

# For removing the zero elements from the matrix we will use eliminate_zeros():

import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([[0,0,0,] , [0,6,0] ,[1, 0 , 2]])

wajahatnew =csr_matrix(wajahat)
wajahatnew.eliminate_zeros()
print(wajahatnew)

# Eliminating duplicate entries with sum_duplicate() method:


import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([[0,0,0,] , [0,6,0] ,[1, 0 , 2]])

wajahatnew =csr_matrix(wajahat)
wajahatnew.sum_duplicates()
print(wajahatnew)

# Here we will convert csr to csc with the tocsc():

import numpy as np
from scipy.sparse import csr_matrix
wajahat =np.array([[0,0,0,] , [0,6,0] ,[1, 0 , 2]])
wajahatnew =csr_matrix(wajahat).tocsc()
print(wajahatnew)



#__________________BEST OF LUCK ____________________#