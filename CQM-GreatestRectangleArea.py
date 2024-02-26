from dimod import ConstrainedQuadraticModel, Integer

## Found [here](https://docs.ocean.dwavesys.com/en/stable/overview/formulation.html)

## Given a rectangle has perimeter '8', what is the maximum area it can attain?

# Initialise side lengths
i = Integer('i', upper_bound=4)
j = Integer('j', upper_bound=4)

# Initiialise Model
cqm = ConstrainedQuadraticModel()

# We wish to maximise `i * j`, i.e minimise `-i * j`
cqm.set_objective(-i*j)

# The perimeter cannot exceed `8`
cqm.add_constraint(2*i+2*j <= 8, "Max Perimeter")