import numpy as np
from dimod import ConstrainedQuadraticModel, Binary
from dwave.system import LeapHybridCQMSampler
"""
MARKOWITZ PORTFOLIO OPTIMISATION

In this file, we consider ten stocks with random returns, deviations and correlations. We would like
to find the optimal set to invest in given some constraints:

• We would like to garuntee a minimum return
• We would like to invest in exactly n of the 10 stocks

Given these, we formualte the problem as a constrained quadtratic model (CQM) and solve
using the LeapHybridCQMSampler to find an approximate solution.
"""

## The expeted return of 10 stocks
expected_return = 10 * np.random.randn(10)

## The correlation between each pair of stocks (must be symmetric).
_ = np.random.randn(10)
correlation = np.outer(_, _)

## standard deviation of each stock.
stdev = np.random.randn(10)

## The risk matrix. ij'th entry is the risk associated with choosing the pair (i, j). 
risk_matrix = correlation * np.outer(stdev, stdev)

## We pick n out of the 10 stocks.
n = 5

## Target return.
goal = 50

## x is a vector of binary values.
x = np.array([Binary(f"{i}") for i in range(10)])


cqm = ConstrainedQuadraticModel()

## Set constraints for the model.
cqm.set_objective(x.T @ risk_matrix @ x)
cqm.add_constraint(x @ x == 7, "stocks_invested_in")
cqm.add_constraint(expected_return @ x >= goal, "goal_return")

## Solve using a CQM sampler.
sampler = LeapHybridCQMSampler()
answer = sampler.sample_cqm(cqm)
print(answer.first)

## OUTPUT
# Sample(sample={'0': 1.0, '1': 0.0, '2': 0.0, '3': 1.0, '4': 1.0, '5': 1.0, '6': 1.0, '7': 0.0, '8': 0.0, '9': 1.0}, 
# energy=0.5418436964125114, num_occurrences=1, is_satisfied=array([False, False]), is_feasible=False)

"""
'is_satisfied=array([False, False])' shows that both constraints were not met exactly, so with these parameters 
there is no exact solution but this provides the lowest energy state. We invest in stocks 0, 3, 5, 6, 7, 9 and no others. 
"""




