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
D = 8
print('D:', D)
# Constraints
l = [0 for i in range(D)]
print('\nl: ', l)
u = [1000000 for i in range(D)]
print('\nu: ', u)
A = ([0.5412844036697249, 0.5412844036697249, 0.5412844036697249, 0.5412844036697249, 0.5412844036697249,
     0.5412844036697249, 0.5412844036697249, 0.5412844036697249, 0.4587155963302752, 0, 0.4587155963302752,
     0, -1, -1, 0, 0, 0, 0.4587155963302752, 0, 0.4587155963302752, 0, 0, -1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 1,
     0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])
print('\nA: ', A)
b = ([17824259.779816516, -66752.80733944954, -28053.97247706422, 17729453, 300724.82, 171419.12, 9128, 37283, 43486,
     10914, 39459, 33991, 2603, 2896, 3229, 4424])
print('\nb: ', b)
if len(A) == len(b):
    print('count of A lists is the same as the b length ')
else:
    print('count of A lists is NOT the same as the b length!!!!!!!!!!!!!')
# Required functions
constantsOfFunctionFit = ([2.910074166666667, 2.910131666666667, 2.6800458333333337, 2.680064166666667,
                          1.321977777777778, 1.320888888888889, 1.5905, 1.591611111111111])
for i in range(len(constantsOfFunctionFit)):
    f = lambda x: sum(constantsOfFunctionFit[i] * x)

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