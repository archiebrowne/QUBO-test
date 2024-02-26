import numpy as np
from dimod import BinaryQuadraticModel, Binary
from dwave.system import LeapHybridSampler

# A first attempt at solving a QUBO problem on four variables

# Square symmetric matrix correlation matrix
Q = np.array([
    [0.4, 0.1, -0.5, 0.2],
    [0.1, -0.3, 0.5, 1.2],
    [-0.5, 0.5, -0.1, 0.9],
    [0.2, 1.2, 0.9, 0.5]
])

x = np.array([Binary(f'{i}') for i in range(4)])

# LeapHybridSampler is used to solve arbitrary BQM problems 
sampler = LeapHybridSampler()

# Feed the quantity we wish to minimise
answer = sampler.sample(x.T @ Q @ x)
print(answer)

## OUTPUT:
#     0  1  2  3 energy num_oc.
#  0  1  0  1  0   -0.7       1
# ['BINARY', 1 rows, 1 samples, 4 variables]

# i.e x = [1, 0, 1, 0] minimises the quantity x.T Q x
