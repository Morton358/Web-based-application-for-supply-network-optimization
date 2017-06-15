import random
import itertools
import math
from pandas import *
from operator import add
import mathModel
from pyLindo import *


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#block with prepearing data for transfering into solver
#///////////////////////////////////////////////////////

def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total

def sumRow(m, row):
    total = 0
    for column in range(len(m[0])):
        total += m[row][column]
    return total

countOfConstraints = ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E) + mathModel.E + mathModel.R +
                      mathModel.R + 2)
countOfDesitionVariables = (mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)

sumaA = 0
for i in range(mathModel.I):
    for r in range(mathModel.R):
        sumaA += (1 - 1/mathModel.V[r]) * mathModel.A1_R__1_I[i][r]


print('sumaA: ', sumaA)

sumaZ = 0
for r in range(mathModel.R):
    sumaZ += 1/mathModel.V[r] * mathModel.Z1_R[r]

print('sumaZ: ', sumaZ)

constOfConstraint7 = (sum(itertools.chain(mathModel.W, mathModel.Z)) + sumaA + sum(mathModel.A1_R__1_E_arr) +
                     sum(mathModel.Y) + sumaZ)
constOfConstraint6 = sum(mathModel.A1_R__1_I_arr) + sum(itertools.chain(mathModel.W, mathModel.Z))
constsOfConstraint5 = []
constsOfConstraint4 = []
constsOfConstraint3 = []
constsOfConstraint2 = mathModel.A1_R__1_E_arr
constsOfConstraint1 = mathModel.A1_R__1_I_arr

for iteratorR in range(mathModel.R):
    temporary5 = ((sumColumn(mathModel.A1_R__1_I, iteratorR) - mathModel.Z1_R[iteratorR]) / mathModel.V[iteratorR]
                 - mathModel.Y[iteratorR] - sumRow(mathModel.A1_R__1_E, iteratorR))
    constsOfConstraint5.append(temporary5)
    temporary4 = mathModel.G[iteratorR] * mathModel.V[iteratorR] + sumColumn(mathModel.A1_R__1_I, iteratorR)
    constsOfConstraint4.append(temporary4)

for iteratorE in range(mathModel.E):
    temporary3 = mathModel.K[iteratorE] + sumColumn(mathModel.A1_R__1_E, iteratorE)
    constsOfConstraint3.append(temporary3)

allConstsOfConstraints = []
allConstsOfConstraints.append(constOfConstraint7)
allConstsOfConstraints.extend(constsOfConstraint5)
allConstsOfConstraints.append(constOfConstraint6)
allConstsOfConstraints.extend(constsOfConstraint4)
allConstsOfConstraints.extend(constsOfConstraint3)
allConstsOfConstraints.extend(constsOfConstraint1)
allConstsOfConstraints.extend(constsOfConstraint2)


lessThenEqual = 'L'
equalTo = 'E'
greaterThenEqual = 'G'
signsOfConstrainExpressions = []
signOfConstrainExpression7 = lessThenEqual
signsOfConstrainExpressions.append(signOfConstrainExpression7)
signsOfConstrain5 = [equalTo for i in range(mathModel.R)]
signsOfConstrainExpressions.extend(signsOfConstrain5)
signOfConstrainExpression6 = lessThenEqual
signsOfConstrainExpressions.append(signOfConstrainExpression6)
signsOfConstrain4 = [lessThenEqual for i in range(mathModel.R)]
signsOfConstrainExpressions.extend(signsOfConstrain4)
signsOfConstrain3 = [greaterThenEqual for i in range(mathModel.E)]
signsOfConstrainExpressions.extend(signsOfConstrain3)
signsOfConstrain1 = [greaterThenEqual for i in range(mathModel.R * mathModel.I)]
signsOfConstrainExpressions.extend(signsOfConstrain1)
signsOfConstrain2 = [greaterThenEqual for i in range(mathModel.R * mathModel.E)]
signsOfConstrainExpressions.extend(signsOfConstrain2)


constantsOfDecisionVariableOfConstrain7 = []
constantsOfDecisionVariableOfConstrain6 = ([1 for i in range(mathModel.I * mathModel.R)] +
                                           [0 for i in range(mathModel.R * mathModel.E)])
constantsOfDecisionVariableOfConstrain5i1 = []
constantsOfDecisionVariableOfConstrain5i2 = []
constantsOfDecisionVariableOfConstrain4i1 = []
constantsOfDecisionVariableOfConstrain4i2 = []
constantsOfDecisionVariableOfConstrain3i1 = []
constantsOfDecisionVariableOfConstrain3i2 = []
constantsOfDecisionVariableOfConstrain2i1 = []
constantsOfDecisionVariableOfConstrain2i2 = []
constantsOfDecisionVariableOfConstrain1i1 = []
constantsOfDecisionVariableOfConstrain1i2 = []

indeks = 0
for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)):
    if indeks + 1 > mathModel.R:
        indeks = 0
    constantsOfDecisionVariableOfConstrain7.append(1 - 1/mathModel.V[indeks])
    indeks += 1

for iter in range(mathModel.R):
    constantsOfDecisionVariableOfConstrain5i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain5i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain4i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain4i2.append([0 for i in range(mathModel.R * mathModel.E)])

for it in range(mathModel.E):
    constantsOfDecisionVariableOfConstrain3i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain3i2.append([0 for i in range(mathModel.R * mathModel.E)])

for itrator in range(mathModel.I * mathModel.R):
    constantsOfDecisionVariableOfConstrain1i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain1i2.append([0 for i in range(mathModel.R * mathModel.E)])

for ittrator in range(mathModel.R * mathModel.E):
    constantsOfDecisionVariableOfConstrain2i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain2i2.append([0 for i in range(mathModel.R * mathModel.E)])

iterator = 0
iteratorV = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain5i1:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < mathModel.I * mathModel.R:
        lists[iterator] = 1/mathModel.V[iteratorV]
        iterator += mathModel.R
    iteratorV += 1

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain5i2:
    indexOfLists += 1
    iterator = indexOfLists
    for i in range(mathModel.E):
        lists[iterator] = -1
        iterator += 1
    indexOfLists += mathModel.E-1

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain4i1:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < mathModel.I * mathModel.R:
        lists[iterator] = 1
        iterator += mathModel.R

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain3i2:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < mathModel.R * mathModel.E:
        lists[iterator] = 1
        iterator += mathModel.E

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain1i1:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = 1


iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain2i2:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = 1

constantsOfDecisionVariableOfConstrain5arr = []
constantsOfDecisionVariableOfConstrain4arr = []
constantsOfDecisionVariableOfConstrain3arr = []
constantsOfDecisionVariableOfConstrain2arr = []
constantsOfDecisionVariableOfConstrain1arr = []

for i in range(mathModel.R):
    constantsOfDecisionVariableOfConstrain5arr.extend(constantsOfDecisionVariableOfConstrain5i1[i] +
                                                      constantsOfDecisionVariableOfConstrain5i2[i])
    constantsOfDecisionVariableOfConstrain4arr.extend(constantsOfDecisionVariableOfConstrain4i1[i] +
                                                      constantsOfDecisionVariableOfConstrain4i2[i])

for i in range(mathModel.E):
    constantsOfDecisionVariableOfConstrain3arr.extend(constantsOfDecisionVariableOfConstrain3i1[i] +
                                                      constantsOfDecisionVariableOfConstrain3i2[i])

for i in range(mathModel.I * mathModel.R):
    constantsOfDecisionVariableOfConstrain1arr.extend(constantsOfDecisionVariableOfConstrain1i1[i] +
                                                      constantsOfDecisionVariableOfConstrain1i2[i])

for i in range(mathModel.R * mathModel.E):
    constantsOfDecisionVariableOfConstrain2arr.extend(constantsOfDecisionVariableOfConstrain2i1[i] +
                                                      constantsOfDecisionVariableOfConstrain2i2[i])

constantsOfDecisionVariableOfConstrain5 = \
    ([constantsOfDecisionVariableOfConstrain5arr[y:y + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]
                                            for y in range(0, len(constantsOfDecisionVariableOfConstrain5arr),
                                                           ((mathModel.I * mathModel.R) +
                                                            (mathModel.R * mathModel.E)))])
constantsOfDecisionVariableOfConstrain4 = \
    ([constantsOfDecisionVariableOfConstrain4arr[z:z + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]
      for z in range(0, len(constantsOfDecisionVariableOfConstrain4arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E)))])
constantsOfDecisionVariableOfConstrain3 = \
    ([constantsOfDecisionVariableOfConstrain3arr[t:t + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]
      for t in range(0, len(constantsOfDecisionVariableOfConstrain3arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E)))])
constantsOfDecisionVariableOfConstrain2 = \
    ([constantsOfDecisionVariableOfConstrain2arr[x:x + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]
      for x in range(0, len(constantsOfDecisionVariableOfConstrain2arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E)))])
constantsOfDecisionVariableOfConstrain1 = \
    ([constantsOfDecisionVariableOfConstrain1arr[v:v + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]
      for v in range(0, len(constantsOfDecisionVariableOfConstrain1arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E)))])


matrixOfDecisionVariables = []
matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain7)

for i in range(len(constantsOfDecisionVariableOfConstrain5)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain5[i])

matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain6)

for i in range(len(constantsOfDecisionVariableOfConstrain4)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain4[i])

count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain3)):
    for j in constantsOfDecisionVariableOfConstrain3[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint3:', count, "\n",
      'count all elements in constraint3: ', allCount)
if count == (mathModel.R * mathModel.E):
    print('constants of decision variable of constrain 3 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 3')

for i in range(len(constantsOfDecisionVariableOfConstrain3)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain3[i])

print('constantsOfDecisionVariableOfConstrain1 :', constantsOfDecisionVariableOfConstrain1)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain1)):
    for j in constantsOfDecisionVariableOfConstrain1[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint1:', count, "\n",
      'count all elements in constraint1: ', allCount)
if count == (mathModel.I * mathModel.R):
    print('constants of decision variable of constrain 1 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 1')

for i in range(len(constantsOfDecisionVariableOfConstrain1)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain1[i])

print('constantsOfDecisionVariableOfConstrain2 :', constantsOfDecisionVariableOfConstrain2)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain2)):
    for j in constantsOfDecisionVariableOfConstrain2[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint2:', count, "\n",
      'count all elements in constraint2: ', allCount)
if count == (mathModel.R * mathModel.E):
    print('constants of decision variable of constrain 2 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 2')

for i in range(len(constantsOfDecisionVariableOfConstrain2)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain2[i])


lastEleemOfMatrix = 0
columnStartIndices = []
nonZeroCoeficients = []
rowIndices = []
indexOfNoZeroElement = -1
previousJ = -1
for j in range(len(matrixOfDecisionVariables[0])):
    for i in range(len(matrixOfDecisionVariables)):
        if matrixOfDecisionVariables[i][j] != 0:
            nonZeroCoeficients.append(matrixOfDecisionVariables[i][j])
            lastEleemOfMatrix = matrixOfDecisionVariables[i][j]
            rowIndices.append(i)
            indexOfNoZeroElement += 1
            if previousJ != j:
                columnStartIndices.append(indexOfNoZeroElement)
                previousJ = j
columnStartIndices.append(indexOfNoZeroElement+1)



lowerBounds = []
upperBounds = []
pointersToCharacters = []
lowerBounds.extend(0 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))
upperBounds.extend(1.0E+30 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))
#pointersToCharacters.extend('I' for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))


J1_I_FIT = []
for i in mathModel.J1_I:
    for iteratorR in range(mathModel.R):
        J1_I_FIT.append(i)

J1_R_FIT = []
for i in mathModel.J1_R:
    for iteratorE in range(mathModel.E):
        J1_R_FIT.append(i)

J1_R__1_I_FIT = []
J1_R__1_E_FIT = []
for i in mathModel.J1_R__1_I_arr:
    J1_R__1_I_FIT.append(i / mathModel.Q_TIR)

for i in mathModel.J1_R__1_E_arr:
    J1_R__1_E_FIT.append(i / mathModel.Q)

print(J1_I_FIT, J1_R_FIT, J1_R__1_I_FIT, J1_R__1_E_FIT)

something1 = [sum(x) for x in zip(J1_I_FIT, J1_R__1_I_FIT)]
something2 = [sum(x) for x in zip(J1_R_FIT, J1_R__1_E_FIT)]
print('something1: ', something1)
print('something2: ', something2)
if len(something1) == len(something2):
    print('all right with something')
constantsOfFunctionFit = something1 + something2
print('Constants of function fit: ', constantsOfFunctionFit)

'''constantsOfFunctionFitNew = []
for i in constantsOfFunctionFit:
    constantsOfFunctionFitNew.append(round(i, 7))
print('New constants of function fit: ', constantsOfFunctionFitNew)
print('and len: ', len(constantsOfFunctionFit))
print('Constants Of Function Fit: ', constantsOfFunctionFit)'''


#\\\\\\\\\\\\\
# some tests:
#/////////////
print('Verification of data:', "\n",
      'constOfConstraint7 :', constOfConstraint7, "\n",
      'constOfConstraint6 :', constOfConstraint6, "\n",
      'constOfConstraint5 :', constsOfConstraint5, "\n",
      'constOfConstraint4 :', constsOfConstraint4, "\n",
      'constOfConstraint3 :', constsOfConstraint3, "\n",
      'constOfConstraint2 :', constsOfConstraint2, "\n",
      'constOfConstraint1 :', constsOfConstraint1, "\n",
      'Constants on the right hand of constrain expressions: ', allConstsOfConstraints, "\n",
      'Signs of the constrain expressions: ', signsOfConstrainExpressions, "\n",
      'constantsOfDecisionVariableOfConstrain7: ', constantsOfDecisionVariableOfConstrain7, "\n",
      'constantsOfDecisionVariableOfConstrain6: ', constantsOfDecisionVariableOfConstrain6, "\n",
      'Length of constantsOfDecisionVariableOfConstrain5: ', len(constantsOfDecisionVariableOfConstrain5), "\n",
      'Matrix of decision variables: ', "\n", DataFrame(matrixOfDecisionVariables), "\n",
      'column-start indices: ', columnStartIndices, "\n",
      'non zero elements: ', nonZeroCoeficients, "\n",
      'row indices: ', rowIndices, "\n",

      )

if countOfDesitionVariables == len(matrixOfDecisionVariables[0]) == len(constantsOfFunctionFit) == \
        len(lowerBounds) == len(upperBounds):
    print('countOfDesitionVariables equal to count of the first row in matrix of Decision Variables ')
else:
    print('countOfDesitionVariables IS NOT equal to count of the first row in matrix of Decision Variables !!!')

if countOfConstraints == len(allConstsOfConstraints) == len(signsOfConstrainExpressions) == \
        len(matrixOfDecisionVariables):
    print('count of constraint equal to count of constants on the right hand of contraint expressions and their signs')
else:
    print(
        'count of constraint _NOT_ equal to count of constants on the right hand of '
        'contraint expressions and their signs')

if len(constantsOfDecisionVariableOfConstrain5[0]) == len(constantsOfDecisionVariableOfConstrain7) == len(
        constantsOfDecisionVariableOfConstrain6) == len(constantsOfDecisionVariableOfConstrain4[0]) == len(
        constantsOfDecisionVariableOfConstrain3[0]) == len(constantsOfDecisionVariableOfConstrain2[0]) == len(
        constantsOfDecisionVariableOfConstrain1[0]):
    print('all length of constantsOfDecisionVariableOfConstrain are the same')
else:
    print('hmm.. some length of constantsOfDecisionVariableOfConstrain are different from other !!!')

if len(columnStartIndices) - 1 == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)):
    print('columnStartIndices have good length')
else:
    print('columnStartIndices have BAD length!!!')

if len(nonZeroCoeficients) == len(rowIndices):
    print('length of nonZeroCoeficients are the same as rowIndices')
else:
    print('length of nonZeroCoeficients are NOT the same as rowIndices!!!')

if countOfConstraints == len(matrixOfDecisionVariables) == len(allConstsOfConstraints) == \
        len(signsOfConstrainExpressions):
    print('count of constraint is fine')
else:
    print('count wrong')

if len(nonZeroCoeficients) == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E) +
                                   (mathModel.I * mathModel.R) + (mathModel.R * mathModel.E) +
                                   (mathModel.I * mathModel.R) + (mathModel.I * mathModel.R) +
                                   (mathModel.R * mathModel.E) + (mathModel.I * mathModel.R) +
                                   (mathModel.R * mathModel.E)):
    print('Length of non zero coeficients of decision variables is correct')
else:
    print('LENGTH OF NON ZERO COEFICIENTS OF DECISION VARIABLES IS NOT CORRECT', "\n",
          'Checking why length of non zero coefocoents is not correct:')
    if len(constantsOfDecisionVariableOfConstrain7) == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)):
        print('constants of decision variable of constrain 7 is fine')
    else:
        print('constants of decision variable of constrain 7 is NOT fine', "\n",
              'len of constants of desition variable 7:', len(constantsOfDecisionVariableOfConstrain7), "\n",
              'factual length: ', ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))

    count = 0
    allCount = 0
    for i in range(len(constantsOfDecisionVariableOfConstrain5)):
        for j in constantsOfDecisionVariableOfConstrain5[i]:
            allCount += 1
            if j != 0:
                count += 1
    if count == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)):
        print('constants of decision variable of constrain 5 is fine')
    else:
        print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 5', "\n",
              'count of nonZero in constraint5:', count, "\n",
              'count all elements in constraint5: ', allCount)

    count = 0
    allCount = 0
    for j in constantsOfDecisionVariableOfConstrain6:
        allCount += 1
        if j != 0:
            count += 1
    if count == (mathModel.I * mathModel.R):
        print('constants of decision variable of constrain 6 is fine')
    else:
        print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 6', "\n",
              'count of nonZero in constraint6:', count, "\n",
              'count all elements in constraint6: ', allCount)

    count = 0
    allCount = 0
    for i in range(len(constantsOfDecisionVariableOfConstrain4)):
        for j in constantsOfDecisionVariableOfConstrain4[i]:
            allCount += 1
            if j != 0:
                count += 1
    if count == (mathModel.I * mathModel.R):
        print('constants of decision variable of constrain 4 is fine')
    else:
        print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 4', "\n",
              'count of nonZero in constraint4:', count, "\n",
              'count all elements in constraint4: ', allCount)

print('len non zero coeficients: ', len(nonZeroCoeficients))
print('len row indices: ', len(rowIndices))
print('len column start indices: ', len(columnStartIndices))
# \\\\\\\\\\\\\\
# model data
#//////////////

nCons = countOfConstraints # count of constrains
nVars = countOfDesitionVariables # count of decision variables
nDir = 1 # direction 1 - it`s minimisation of function fit
dObjConst = 0.0 # constant term in the objective function
adC = N.array(constantsOfFunctionFit, dtype=N.double) # coficients of variables in function fit
adB = N.array(allConstsOfConstraints, dtype=N.double) # constant on the right hand of constrain expressions
acConTypes = N.array(signsOfConstrainExpressions, dtype=N.character) # signs of the constrain expressions
nNZ = len(nonZeroCoeficients)  # the number of nonzero coefficients in the constraint matrix
anBegCol = N.array(columnStartIndices, dtype=N.int32) # column-start indices
pnLenCol = N.asarray(None) # if no blanks are been lefy in matrix = None
adA = N.array(nonZeroCoeficients, dtype=N.double) # nonzero coefficients
anRowX = N.array(rowIndices, dtype=N.int32) # row indices
pdLower = N.array(lowerBounds, dtype=N.double) # lower bounds for desition variables
pdUpper = N.array(upperBounds, dtype=N.double) # upper bounds for desition variables
#pachVarType = N.array(pointersToCharacters,dtype=N.character) # A pointer to a character vector containing the type
# of each variable (‘C’, ‘B’, ‘I’, or ‘S’ for continuous, binary, general integer or semi-continuous, respectively.)

print("\nnCons", nCons, "\nnVars", nVars, "\nnDir", nDir, "\ndObjCons", dObjConst, "\nlen adC", len(adC), "\nadC",
      adC, "\nlen adB", len(adB),"\nadB", adB, "\nlen acConTypes", len(acConTypes), "\nacConTypes", acConTypes)
print("\nnNZ", nNZ, "\nlen anBegCol", len(anBegCol), "\nanBegCol", anBegCol, "\npnLenCol", pnLenCol, "\nlen adA",
      len(adA), "\nadA", adA, "\nlen anRowX", len(anRowX), "\nanRowX", anRowX, "\nlen pdLower", len(pdLower),
      "\npdLower", pdLower, "\nlen pdUpper", len(pdUpper), "\npdUpper", pdUpper)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#create LINDO environment and model objects
#//////////////////////////////////////////
LicenseKey = N.array('', dtype='S1024')
lindo.pyLSloadLicenseString('/home/morton/My_Files/Politechnika_Wroclawska/DYPLOM/lindoapi/license/lndapi100.lic',
                            LicenseKey)
pnErrorCode = N.array([-1], dtype=N.int32) # A reference to an integer to return the error code
pEnv = lindo.pyLScreateEnv(pnErrorCode, LicenseKey)

pModel = lindo.pyLScreateModel(pEnv, pnErrorCode)

geterrormessage(pEnv, pnErrorCode[0])


#\\\\\\\\\\\\\\\\\\\\\\\\\
#load data into the model
#/////////////////////////
print("Loading LP data...")
errorcode = lindo.pyLSloadLPData(pModel, nCons, nVars, nDir, dObjConst, adC, adB, acConTypes, nNZ, anBegCol, pnLenCol,
                                 adA, anRowX, pdLower, pdUpper)
geterrormessage(pEnv, errorcode)


#\\\\\\\\\\\\\\\
#solve the model
#///////////////
print("Solving the model...")
pnStatus = N.array([-1], dtype=N.int32)
errorcode = lindo.pyLSoptimize(pModel, LSconst.LS_METHOD_FREE, pnStatus)
geterrormessage(pEnv, errorcode)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the objective value
#//////////////////////////////
dObj = N.array([-1.0], dtype=N.double)
errorcode = lindo.pyLSgetInfo(pModel, LSconst.LS_DINFO_POBJ, dObj)
geterrormessage(pEnv, errorcode)
print("Objective is: %.5f" % dObj[0])
print("")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the primal solution
#/////////////////////////////
padPrimal = N.empty((nVars), dtype=N.double)
errorcode = lindo.pyLSgetPrimalSolution(pModel, padPrimal)
geterrormessage(pEnv, errorcode)
print("Primal solution is: ")
for x in padPrimal:
    print("%.5f" % x)


#delete LINDO model pointer
errorcode = lindo.pyLSdeleteModel(pModel)
geterrormessage(pEnv, errorcode)

#delete LINDO environment pointer
errorcode = lindo.pyLSdeleteEnv(pEnv)
geterrormessage(pEnv, errorcode)
