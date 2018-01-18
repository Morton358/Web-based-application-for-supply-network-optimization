# -*- coding: utf-8 -*-
import itertools
from pandas import *
from operator import mul
import mathModel



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
                      mathModel.R + 2 + (mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))
countOfDesitionVariables = ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E) + (mathModel.I * mathModel.R) +
                            (mathModel.R * mathModel.E))

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
constsOfConstraint8 = [0] * (mathModel.I * mathModel.R)
constsOfConstraint9 = [0] * (mathModel.R * mathModel.E)

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
allConstsOfConstraints.extend(constsOfConstraint8)
allConstsOfConstraints.extend(constsOfConstraint9)


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
signsOfConstrain8 = [lessThenEqual for i in range(mathModel.R * mathModel.I)]
signsOfConstrainExpressions.extend(signsOfConstrain8)
signsOfConstrain9 = [lessThenEqual for i in range(mathModel.R * mathModel.E)]
signsOfConstrainExpressions.extend(signsOfConstrain9)


constantsOfDecisionVariableOfConstrain7 = []
constantsOfDecisionVariableOfConstrain6 = ([1 for i in range(mathModel.I * mathModel.R)] +
                                           [0 for i in range(mathModel.R * mathModel.E)] +
                                           [0 for i in range((mathModel.I * mathModel.R) +
                                                             (mathModel.R * mathModel.E))])
constantsOfDecisionVariableOfConstrain5i1 = []
constantsOfDecisionVariableOfConstrain5i2 = []
constantsOfDecisionVariableOfConstrain5i3 = []
constantsOfDecisionVariableOfConstrain5i4 = []
constantsOfDecisionVariableOfConstrain4i1 = []
constantsOfDecisionVariableOfConstrain4i2 = []
constantsOfDecisionVariableOfConstrain4i3 = []
constantsOfDecisionVariableOfConstrain4i4 = []
constantsOfDecisionVariableOfConstrain3i1 = []
constantsOfDecisionVariableOfConstrain3i2 = []
constantsOfDecisionVariableOfConstrain3i3 = []
constantsOfDecisionVariableOfConstrain3i4 = []
constantsOfDecisionVariableOfConstrain2i1 = []
constantsOfDecisionVariableOfConstrain2i2 = []
constantsOfDecisionVariableOfConstrain2i3 = []
constantsOfDecisionVariableOfConstrain2i4 = []
constantsOfDecisionVariableOfConstrain1i1 = []
constantsOfDecisionVariableOfConstrain1i2 = []
constantsOfDecisionVariableOfConstrain1i3 = []
constantsOfDecisionVariableOfConstrain1i4 = []
constantsOfDecisionVariableOfConstrain8i1 = []
constantsOfDecisionVariableOfConstrain8i2 = []
constantsOfDecisionVariableOfConstrain8i3 = []
constantsOfDecisionVariableOfConstrain8i4 = []
constantsOfDecisionVariableOfConstrain9i1 = []
constantsOfDecisionVariableOfConstrain9i2 = []
constantsOfDecisionVariableOfConstrain9i3 = []
constantsOfDecisionVariableOfConstrain9i4 = []

indeks = 0
for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)):
    if indeks + 1 > mathModel.R:
        indeks = 0
    constantsOfDecisionVariableOfConstrain7.append(1 - 1/mathModel.V[indeks])
    indeks += 1
constantsOfDecisionVariableOfConstrain7 += [0 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))]

for iter in range(mathModel.R):
    constantsOfDecisionVariableOfConstrain5i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain5i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain5i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain5i4.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain4i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain4i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain4i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain4i4.append([0 for i in range(mathModel.R * mathModel.E)])

for it in range(mathModel.E):
    constantsOfDecisionVariableOfConstrain3i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain3i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain3i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain3i4.append([0 for i in range(mathModel.R * mathModel.E)])

for itrator in range(mathModel.I * mathModel.R):
    constantsOfDecisionVariableOfConstrain1i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain1i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain1i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain1i4.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain8i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain8i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain8i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain8i4.append([0 for i in range(mathModel.R * mathModel.E)])

for ittrator in range(mathModel.R * mathModel.E):
    constantsOfDecisionVariableOfConstrain2i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain2i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain2i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain2i4.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain9i1.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain9i2.append([0 for i in range(mathModel.R * mathModel.E)])
    constantsOfDecisionVariableOfConstrain9i3.append([0 for i in range(mathModel.I * mathModel.R)])
    constantsOfDecisionVariableOfConstrain9i4.append([0 for i in range(mathModel.R * mathModel.E)])


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

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain8i1:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = 1 / mathModel.Q_TIR

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain8i3:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = -1

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain9i2:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = 1 / mathModel.Q

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain9i4:
    indexOfLists += 1
    iterator = indexOfLists
    lists[iterator] = -1

constantsOfDecisionVariableOfConstrain9arr = []
constantsOfDecisionVariableOfConstrain8arr = []
constantsOfDecisionVariableOfConstrain5arr = []
constantsOfDecisionVariableOfConstrain4arr = []
constantsOfDecisionVariableOfConstrain3arr = []
constantsOfDecisionVariableOfConstrain2arr = []
constantsOfDecisionVariableOfConstrain1arr = []

for i in range(mathModel.R):
    constantsOfDecisionVariableOfConstrain5arr.extend(constantsOfDecisionVariableOfConstrain5i1[i] +
                                                      constantsOfDecisionVariableOfConstrain5i2[i] +
                                                      constantsOfDecisionVariableOfConstrain5i3[i] +
                                                      constantsOfDecisionVariableOfConstrain5i4[i])
    constantsOfDecisionVariableOfConstrain4arr.extend(constantsOfDecisionVariableOfConstrain4i1[i] +
                                                      constantsOfDecisionVariableOfConstrain4i2[i] +
                                                      constantsOfDecisionVariableOfConstrain4i3[i] +
                                                      constantsOfDecisionVariableOfConstrain4i4[i])

for i in range(mathModel.E):
    constantsOfDecisionVariableOfConstrain3arr.extend(constantsOfDecisionVariableOfConstrain3i1[i] +
                                                      constantsOfDecisionVariableOfConstrain3i2[i] +
                                                      constantsOfDecisionVariableOfConstrain3i3[i] +
                                                      constantsOfDecisionVariableOfConstrain3i4[i])

for i in range(mathModel.I * mathModel.R):
    constantsOfDecisionVariableOfConstrain1arr.extend(constantsOfDecisionVariableOfConstrain1i1[i] +
                                                      constantsOfDecisionVariableOfConstrain1i2[i] +
                                                      constantsOfDecisionVariableOfConstrain1i3[i] +
                                                      constantsOfDecisionVariableOfConstrain1i4[i])
    constantsOfDecisionVariableOfConstrain8arr.extend(constantsOfDecisionVariableOfConstrain8i1[i] +
                                                      constantsOfDecisionVariableOfConstrain8i2[i] +
                                                      constantsOfDecisionVariableOfConstrain8i3[i] +
                                                      constantsOfDecisionVariableOfConstrain8i4[i])

for i in range(mathModel.R * mathModel.E):
    constantsOfDecisionVariableOfConstrain2arr.extend(constantsOfDecisionVariableOfConstrain2i1[i] +
                                                      constantsOfDecisionVariableOfConstrain2i2[i] +
                                                      constantsOfDecisionVariableOfConstrain2i3[i] +
                                                      constantsOfDecisionVariableOfConstrain2i4[i])
    constantsOfDecisionVariableOfConstrain9arr.extend(constantsOfDecisionVariableOfConstrain9i1[i] +
                                                      constantsOfDecisionVariableOfConstrain9i2[i] +
                                                      constantsOfDecisionVariableOfConstrain9i3[i] +
                                                      constantsOfDecisionVariableOfConstrain9i4[i])

constantsOfDecisionVariableOfConstrain5 = \
    ([constantsOfDecisionVariableOfConstrain5arr[y:y + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
                                            for y in range(0, len(constantsOfDecisionVariableOfConstrain5arr),
                                                           ((mathModel.I * mathModel.R) +
                                                            (mathModel.R * mathModel.E))*2)])
constantsOfDecisionVariableOfConstrain4 = \
    ([constantsOfDecisionVariableOfConstrain4arr[z:z + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for z in range(0, len(constantsOfDecisionVariableOfConstrain4arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])
constantsOfDecisionVariableOfConstrain3 = \
    ([constantsOfDecisionVariableOfConstrain3arr[t:t + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for t in range(0, len(constantsOfDecisionVariableOfConstrain3arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])
constantsOfDecisionVariableOfConstrain2 = \
    ([constantsOfDecisionVariableOfConstrain2arr[x:x + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for x in range(0, len(constantsOfDecisionVariableOfConstrain2arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])
constantsOfDecisionVariableOfConstrain1 = \
    ([constantsOfDecisionVariableOfConstrain1arr[v:v + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for v in range(0, len(constantsOfDecisionVariableOfConstrain1arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])

constantsOfDecisionVariableOfConstrain8 = \
    ([constantsOfDecisionVariableOfConstrain8arr[k:k + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for k in range(0, len(constantsOfDecisionVariableOfConstrain8arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])

constantsOfDecisionVariableOfConstrain9 = \
    ([constantsOfDecisionVariableOfConstrain9arr[p:p + ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2]
      for p in range(0, len(constantsOfDecisionVariableOfConstrain9arr), ((mathModel.I * mathModel.R) +
                                                                          (mathModel.R * mathModel.E))*2)])

matrixOfDecisionVariables = []



matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain7)

for i in range(len(constantsOfDecisionVariableOfConstrain5)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain5[i])

matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain6)

for i in range(len(constantsOfDecisionVariableOfConstrain4)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain4[i])

for i in range(len(constantsOfDecisionVariableOfConstrain3)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain3[i])

for i in range(len(constantsOfDecisionVariableOfConstrain1)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain1[i])

for i in range(len(constantsOfDecisionVariableOfConstrain2)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain2[i])

for i in range(len(constantsOfDecisionVariableOfConstrain8)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain8[i])

for i in range(len(constantsOfDecisionVariableOfConstrain9)):
    matrixOfDecisionVariables.append(constantsOfDecisionVariableOfConstrain9[i])

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
lowerBounds.extend(0 for i in range(((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2))
upperBounds.extend(1.0E+30 for i in range(((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2))
pointersToCharacters.extend('C' for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))
pointersToCharacters.extend('I' for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))


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

J1_R__1_I_FIT.extend(list(map(mul, mathModel.J1_R__1_I_arr, mathModel.M1_R__1_I)))
#J1_R__1_I_FIT = [round(elem, 2) for elem in J1_R__1_I_FIT]

J1_R__1_E_FIT.extend(list(map(mul, mathModel.J1_R__1_E_arr, mathModel.M1_R__1_E)))
#J1_R__1_E_FIT = [round(elem, 2) for elem in J1_R__1_E_FIT]

constantsOfFunctionFit = J1_I_FIT + J1_R_FIT + J1_R__1_I_FIT + J1_R__1_E_FIT
print('Constants of function fit: ', constantsOfFunctionFit, "\n",
      'Length of array of constants of func. fit: ', len(constantsOfFunctionFit))

flat_matrixOfDecisionVariables = [item for sublist in matrixOfDecisionVariables for item in sublist]

#\\\\\\\\\\\\\
# some tests:
#/////////////
print('TESTS: ')
print('Verification of data:', "\n",
      'constOfConstraint7 :', constOfConstraint7, "\n",
      'constOfConstraint6 :', constOfConstraint6, "\n",
      'constOfConstraint5 :', constsOfConstraint5, "\n",
      'constOfConstraint4 :', constsOfConstraint4, "\n",
      'constOfConstraint3 :', constsOfConstraint3, "\n",
      'constOfConstraint2 :', constsOfConstraint2, "\n",
      'constOfConstraint1 :', constsOfConstraint1, "\n",
      'constsOfConstraint8 :', constsOfConstraint8, "\n",
      'constsOfConstraint9 :', constsOfConstraint9, "\n",
      'Constants on the right hand of constrain expressions: ', allConstsOfConstraints, "\n",
      'Length of constants on the right hand of constrain expressions: ', len(allConstsOfConstraints), "\n",
      'Signs of the constrain expressions: ', signsOfConstrainExpressions, "\n",
      'Length of signs of the constrain expressions: ', len(signsOfConstrainExpressions), "\n",
      'Matrix of decision variables: ', "\n", DataFrame(matrixOfDecisionVariables), "\n",
      'Flat matrix: ', flat_matrixOfDecisionVariables, "\n",
      'column-start indices: ', columnStartIndices, "\n",
      'non zero elements: ', nonZeroCoeficients, "\n",
      'row indices: ', rowIndices, "\n",
      )
# checking constantsOfDecisionVariableOfConstrain7
print('constantsOfDecisionVariableOfConstrain7 :', constantsOfDecisionVariableOfConstrain7)
if len(constantsOfDecisionVariableOfConstrain7) == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2:
    print('constants of decision variable of constrain 7 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 7')

# checking constantsOfDecisionVariableOfConstrain5
print('constantsOfDecisionVariableOfConstrain5 :', constantsOfDecisionVariableOfConstrain5)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain5)):
    for j in constantsOfDecisionVariableOfConstrain5[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint5:', count, "\n",
      'count all elements in constraint5: ', allCount)
if count == ((mathModel.I + mathModel.E) * mathModel.R) and \
                allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2) * mathModel.R):
    print('constants of decision variable of constrain 5 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 5')


# checking constantsOfDecisionVariableOfConstrain6
print('constantsOfDecisionVariableOfConstrain6 :', constantsOfDecisionVariableOfConstrain6)
if len(constantsOfDecisionVariableOfConstrain6) == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2:
    print('constants of decision variable of constrain 6 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 6')

# checking constantsOfDecisionVariableOfConstrain4
print('constantsOfDecisionVariableOfConstrain4 :', constantsOfDecisionVariableOfConstrain4)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain4)):
    for j in constantsOfDecisionVariableOfConstrain4[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint4:', count, "\n",
      'count all elements in constraint4: ', allCount)
if count == (mathModel.I * mathModel.R) and \
                allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2) * mathModel.R):
    print('constants of decision variable of constrain 4 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 4')

# checking constantsOfDecisionVariableOfConstrain3
print('constantsOfDecisionVariableOfConstrain3 :', constantsOfDecisionVariableOfConstrain3)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain3)):
    for j in constantsOfDecisionVariableOfConstrain3[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint3:', count, "\n",
      'count all elements in constraint3: ', allCount)
if count == (mathModel.R * mathModel.E) and allCount == ((((mathModel.I * mathModel.R) +
                                                               (mathModel.R * mathModel.E))*2) * mathModel.E):
    print('constants of decision variable of constrain 3 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 3')


# checking constantsOfDecisionVariableOfConstrain1
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
if count == (mathModel.I * mathModel.R) and allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2)
                                                             * (mathModel.I * mathModel.R)):
    print('constants of decision variable of constrain 1 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 1')


# checking constantsOfDecisionVariableOfConstrain2
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
if count == (mathModel.R * mathModel.E) and allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2)
                                                             * (mathModel.R * mathModel.E)) :
    print('constants of decision variable of constrain 2 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 2')


# checking constantsOfDecisionVariableOfConstrain8
print('constantsOfDecisionVariableOfConstrain8 :', constantsOfDecisionVariableOfConstrain8)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain8)):
    for j in constantsOfDecisionVariableOfConstrain8[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint8:', count, "\n",
      'count all elements in constraint8: ', allCount)
if count == ((mathModel.I * mathModel.R)*2) and \
                allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2) *
                                 (mathModel.I * mathModel.R)):
    print('constants of decision variable of constrain 8 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 8')


# checking constantsOfDecisionVariableOfConstrain9
print('constantsOfDecisionVariableOfConstrain9 :', constantsOfDecisionVariableOfConstrain9)
count = 0
allCount = 0
for i in range(len(constantsOfDecisionVariableOfConstrain9)):
    for j in constantsOfDecisionVariableOfConstrain9[i]:
        allCount += 1
        if j != 0:
            count += 1
print('count of nonZero in constraint9:', count, "\n",
      'count all elements in constraint9: ', allCount)
if count == ((mathModel.R * mathModel.E)*2) and \
                allCount == ((((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2) *
                                 (mathModel.R * mathModel.E)):
    print('constants of decision variable of constrain 9 is fine')
else:
    print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 9')

# some other tests:
if len(mathModel.M1_R__1_I) == len(mathModel.J1_R__1_I_arr):
    print("M1_R__1_I and J1_R__1_I_arr have the same length")
else:
    print("M1_R__1_I AND J1_R__1_I_arr HAVE DIFFERENT LENGTH")


if len(mathModel.M1_R__1_E) == len(mathModel.J1_R__1_E_arr):
    print("M1_R__1_E and J1_R__1_E_arr have the same length")
else:
    print("M1_R__1_E AND J1_R__1_E_arr HAVE DIFFERENT LENGTH")

print('J1_I_FIT: ', J1_I_FIT, "\n",
      'J1_R_FIT: ', J1_R_FIT, "\n",
      'J1_R__1_I_FIT: ', J1_R__1_I_FIT, "\n",
      'J1_R__1_E_FIT: ', J1_R__1_E_FIT)


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
        constantsOfDecisionVariableOfConstrain1[0]) == len(constantsOfDecisionVariableOfConstrain8[0]) == len(
        constantsOfDecisionVariableOfConstrain9[0]):
    print('all length of constantsOfDecisionVariableOfConstrain are the same')
else:
    print('hmm.. some length of constantsOfDecisionVariableOfConstrain are different from other !!!')

if len(columnStartIndices) - 1 == ((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E))*2:
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

if len(nonZeroCoeficients) == (((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)) + # constraint 7
                            ((mathModel.I + mathModel.E) * mathModel.R) + # constraint 5
                            (mathModel.I * mathModel.R) + # constraint 6
                            (mathModel.I * mathModel.R) + # constraint 4
                            (mathModel.R * mathModel.E) + # constraint 3
                            (mathModel.I * mathModel.R) + # constraint 1
                            (mathModel.R * mathModel.E) + # constraint 2
                            ((mathModel.I * mathModel.R) * 2) + # constraint 8
                            ((mathModel.R * mathModel.E) * 2) ): # constraint 9
    print('Length of non zero coeficients of decision variables is correct')
else:
    print('LENGTH OF NON ZERO COEFICIENTS OF DECISION VARIABLES IS NOT CORRECT', "\n",
          'Checking why length of non zero coefocoents is not correct:')

print('pointersToCharacters: ', pointersToCharacters)
print('len non zero coeficients: ', len(nonZeroCoeficients))
print('len row indices: ', len(rowIndices))
print('len column start indices: ', len(columnStartIndices))