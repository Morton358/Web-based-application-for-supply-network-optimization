# Example RBF Layer code for oBB
from obb import obb_rbf
from numpy import sin, ones
from numpy.random import rand, seed
import mathModel
import prepareDataLINDO
import prepareDataoBB

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
D = prepareDataLINDO.countOfDesitionVariables
print('D:', D)
# Constraints
l = prepareDataoBB.lowerBoundsoBB
print('\nl: ', l)
u = prepareDataoBB.upperBoundsoBB
print('\nu: ', u)
A = prepareDataoBB.flat_matrixOfDecisionVariables
print('\nA: ', A)
b = prepareDataLINDO.allConstsOfConstraints
print('\nb: ', b)
if len(A) == len(b):
    print('count of A lists is the same as the b length ')
else:
    print('count of A lists is NOT the same as the b length!!!!!!!!!!!!!')
# Required functions
for i in range(len(prepareDataLINDO.constantsOfFunctionFit)):
    f = lambda x: sum(prepareDataLINDO.constantsOfFunctionFit[i] * x)

# Generate 10*D sample points for RBF approximation
seed(5) # !!Sample points have to be the same on all processors!!
pts = rand(10*D, D)

# Scale points so they lie in [l,u]
for i in range(0, D):
    pts[:, i] = l[i] + (u[i] - l[i]) * pts[:, i]

# Name objective function
f.__name__ = 'RBF Math model'

# Run oBB
xs, fxs, tol, itr = obb_rbf(f, pts, l, u, alg, mod, A=A, b=b, tol=tol)