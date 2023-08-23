
# Working with graphs: we have a module name scipy.sparse.csgraph

# Adjacency matrix : nxn matrix  where n is number of elements in a graph.

# Connected components:

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
wajahat = np.array([[0 , 1 , 2 ] , [1 , 0 , 0] , [2 ,0 , 0]])
wajahatnew = csr_matrix(wajahat)
print(connected_components(wajahatnew))

# Dijkstra method: for finding the shortest path in a graph from one elements to another.
# it take 3 args: return_predecessors,indices(index of element) ,limit(Maximum weight between elements):

# Here we will find the shortest path from element 1 to 2:
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
wajahat = np.array([[0 , 1 , 2 ] , [1 , 0 , 0] , [2 ,0 , 0]])
wajahatnew = csr_matrix(wajahat)
print(dijkstra(wajahatnew , return_predecessors=True , indices=0))


# Continue remaining 3 to 4 topics ............... i will uploaded after Machine Learning concepts..#



#__________________BEST OF LUCK ____________________#