import dimod
from dwave.system import LeapHybridSampler

"""
Given an undirecred graph G(V, E) where V is the set of vertices and E is the set of edges, the 
'MAXCUT' problem seeks to partition V into two sets such that the number of edges between the two
is as large as possible. 

We will consider a six node graph with the following collection of edges:

[(1, 2), (1, 4), (2, 4), (2, 6), (3, 4), (3, 5), (4, 6), (5, 6)]

We model the problem as follows. Use binary variables xi where xi = 1 if the vertex i
is in one set and xi = 0 if it is in the other. Then the quantity xi + xj - 2*xi*xj identifies 
wether the edge (i, j) is in the cut. It is equal to one if and only if exactly one of xi, xj
is equal to one. 

Then we wish to maximise the sum of each of these indicators. We formulate the problem as a QUBO 
and feed to the Dwave samplers. Equivalently we minimise the objective multiplied by -1. 
`dimod.BinaryQuadraticModel` is set up for minimisation and hence this is how we will give it the problem. 
"""

edges = [(1, 2), (1, 4), (2, 4), (2, 6), (3, 4), (3, 5), (4, 6), (5, 6)]

connections = {
    1 : [2, 4],
    2 : [1, 4, 6],
    3 : [4, 5],
    4 : [1, 2, 3, 6],
    5 : [3, 6],
    6 : [2, 4, 5]
}

# The coefficient of a linear term for each variable in the objective function is simply the 
# degree of the node, since the objective is a sum over the edges
linear = {i : -len(connections[i]) for i in range(1, 7)}

# The quadratic coefficients are all -2 since if there is a connection between i and j, the term 
# xi*xj only appears once in the objective function, when adding xi + xj - 2*xi*xj
quadratic = {edge : 2 for edge in edges}
offset = 0.0

# We are considering only binary options
vartype = dimod.BINARY

# Initialise the model
bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)

# LeapHybridSampler() is effective for a wide range of BQM problems (and probably overkill here)
sampler = LeapHybridSampler()
answer = sampler.sample(bqm)
print(answer)

## OUTPUT
#     1  2  3  4  5  6 energy num_oc.
#  0  1  0  1  0  0  1   -7.0       1
#  ['BINARY', 1 rows, 1 samples, 6 variables]

"""
So the correct partition of V is {1, 3, 6} and {2, 4, 5} giving a total of 7 cuts. 
"""
