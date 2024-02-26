import numpy as np
import dimod
from dwave.system import LeapHybridSampler

# this example comes from section 2 of [https://arxiv.org/pdf/1811.11538.pdf]

# Minimise y = -5*a -3*b -8*c -6*c + 4*a*b + 8*a*c + 2*a*c + 10*c*d where 
# each of a, b, c, d are binary.

## Formulation One

# coefficient matrix
Q = np.array(
    [
        [-5, 2, 4, 0],
        [2, -3, 1, 0],
        [4, 1, -8, 5],
        [0, 0, 5, -6]
    ]
)

x = np.array([dimod.Binary(f'{i}') for i in range(4)])

# Using LeapHybridSampler(). Note that we could use many different solvers such as 
# dimod.SimulatedAnnealingSampler()
sampler = LeapHybridSampler()
answer = sampler.sample(x.T @ Q @ x)
print("Formulation One: Using LeapHybridSampler()")
print(answer)


## Formulation Two

# provide the linear and quadratic coefficients we have for each of a, b, c, d
linear =  {1: -5, 2: -3, 3: -8, 4: -6}
quadratic = {(1, 2): 4, (1, 3): 8, (2, 3): 2, (3, 4): 10}
offset = 0.0
vartype = dimod.BINARY

bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)

# Since this is a small problem, we may aswell use ExactSolver(), which calculates all possible 
# combinations

sampler = dimod.ExactSolver()
answer = sampler.sampler(bqm)
print("Formulation Two: Using ExactSolver()")
print(answer)



