from dimod.generators import and_gate
from dwave.system import LeapHybridSampler

## Found [here](https://docs.ocean.dwavesys.com/en/stable/overview/samplers.html)

## Using a bqm to solve an and gate problem

bqm = and_gate('x1', 'x2', 'y1')
sampler = LeapHybridSampler()
answer = sampler.sample(bqm)
print(answer)