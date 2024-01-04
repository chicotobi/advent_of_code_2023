import scipy.sparse
import scipy.sparse.csgraph

data = [1,1,1,1,1]
i = [0,1,2,3,4]
j = [1,2,3,4,0]

a = scipy.sparse.coo_matrix((data,(i,j)), shape = (5,5))

b = scipy.sparse.csgraph.shortest_path(a)
