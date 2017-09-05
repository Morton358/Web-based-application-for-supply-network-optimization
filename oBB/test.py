# Example RBF Layer code for oBB
from obb import obb_rbf
from numpy import sin, ones
from numpy.random import rand, seed

# Input Settings
# Algorithm (T1, T2_individual, T2_synchronised, T2_synchronised_rr)
alg = 'T1'

# Model type (q - norm quadratic, g/Hz/lbH/E0/Ediag - min eig. quadratic,
# c - norm cubic, gc - gershgorin cubic)
mod = 'c'

# Tolerance
tol = 1e-2

# Set up sum of sines test function
# Dimension
D = 2
# Constraints
l = -1*ones(D)
print('\nl: ', l)
u = 1*ones(D)
print('\nu: ', u)
A = -1*ones((1,D))
print('\nA: ', A)
b = 1
print('\nb: ', b)
# Required functions
f = lambda x: sum(sin(x))

# Generate 10*D sample points for RBF approximation
seed(5) # !!Sample points have to be the same on all processors!!
pts = rand(10*D, D)

# Scale points so they lie in [l,u]
for i in range(0,D):
    pts[:,i] = l[i] + (u[i]-l[i])*pts[:,i]

# Name objective function
f.__name__ = 'RBF Sum of Sins'

# Run oBB
xs, fxs, tol, itr = obb_rbf(f, pts, l, u, alg, mod, A=A, b=b, tol=tol)