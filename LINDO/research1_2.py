import itertools
from pandas import *
from operator import mul
import mathModel
from pyLindo import *
import time


def generator_input_data():
    arrays_of_data = []
    for iter_e in range(3, 26):
        for iter_r in range(3, 6):
            for iter_i in range(3, 16):
                temp = [iter_i, iter_r, iter_e]
                arrays_of_data.append(temp)

    return arrays_of_data


data = {}
for counter in range(897):
    data["ext{}".format(counter)] = mathModel.Modell(generator_input_data()[counter])
    temp_obj = data["ext{}".format(counter)]
    print('ilość rolników: ', temp_obj.I, '\n', 'ilość przedsiębiorstw: ', temp_obj.R, '\n',
          'ilość konsumentów: ', temp_obj.E)
    with open('research1_2.txt', 'a') as plik:
        plik.write('{} {} \n {} {} \n {} {} \n'.format('ilość rolników: ', temp_obj.I,
                                                       'ilość przedsiębiorstw: ', temp_obj.R,
                                                       'ilość konsumentów: ', temp_obj.E))
        plik.close()


    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # block with prepearing data for transfering into solver
    # ///////////////////////////////////////////////////////

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


    countOfConstraints = ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E) + temp_obj.E + temp_obj.R +
                          temp_obj.R + 2 + (temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E))
    countOfDesitionVariables = ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E) + (temp_obj.I * temp_obj.R) +
                                (temp_obj.R * temp_obj.E))

    sumaA = 0
    for i in range(temp_obj.I):
        for r in range(temp_obj.R):
            sumaA += (1 - 1 / temp_obj.V[r]) * temp_obj.A1_R__1_I[i][r]

    print('sumaA: ', sumaA)

    sumaZ = 0
    for r in range(temp_obj.R):
        sumaZ += 1 / temp_obj.V[r] * temp_obj.Z1_R[r]

    print('sumaZ: ', sumaZ)

    constOfConstraint7 = (sum(itertools.chain(temp_obj.W, temp_obj.Z)) + sumaA + sum(temp_obj.A1_R__1_E_arr) +
                          sum(temp_obj.Y) + sumaZ)
    constOfConstraint6 = sum(temp_obj.A1_R__1_I_arr) + sum(itertools.chain(temp_obj.W, temp_obj.Z))
    constsOfConstraint5 = []
    constsOfConstraint4 = []
    constsOfConstraint3 = []
    constsOfConstraint2 = temp_obj.A1_R__1_E_arr
    constsOfConstraint1 = temp_obj.A1_R__1_I_arr
    constsOfConstraint8 = [0] * (temp_obj.I * temp_obj.R)
    constsOfConstraint9 = [0] * (temp_obj.R * temp_obj.E)

    for iteratorR in range(temp_obj.R):
        temporary5 = ((sumColumn(temp_obj.A1_R__1_I, iteratorR) - temp_obj.Z1_R[iteratorR]) / temp_obj.V[iteratorR]
                      - temp_obj.Y[iteratorR] - sumRow(temp_obj.A1_R__1_E, iteratorR))
        constsOfConstraint5.append(temporary5)
        temporary4 = temp_obj.G[iteratorR] * temp_obj.V[iteratorR] + sumColumn(temp_obj.A1_R__1_I, iteratorR)
        constsOfConstraint4.append(temporary4)

    for iteratorE in range(temp_obj.E):
        temporary3 = temp_obj.K[iteratorE] + sumColumn(temp_obj.A1_R__1_E, iteratorE)
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
    signsOfConstrain5 = [equalTo for i in range(temp_obj.R)]
    signsOfConstrainExpressions.extend(signsOfConstrain5)
    signOfConstrainExpression6 = lessThenEqual
    signsOfConstrainExpressions.append(signOfConstrainExpression6)
    signsOfConstrain4 = [lessThenEqual for i in range(temp_obj.R)]
    signsOfConstrainExpressions.extend(signsOfConstrain4)
    signsOfConstrain3 = [greaterThenEqual for i in range(temp_obj.E)]
    signsOfConstrainExpressions.extend(signsOfConstrain3)
    signsOfConstrain1 = [greaterThenEqual for i in range(temp_obj.R * temp_obj.I)]
    signsOfConstrainExpressions.extend(signsOfConstrain1)
    signsOfConstrain2 = [greaterThenEqual for i in range(temp_obj.R * temp_obj.E)]
    signsOfConstrainExpressions.extend(signsOfConstrain2)
    signsOfConstrain8 = [lessThenEqual for i in range(temp_obj.R * temp_obj.I)]
    signsOfConstrainExpressions.extend(signsOfConstrain8)
    signsOfConstrain9 = [lessThenEqual for i in range(temp_obj.R * temp_obj.E)]
    signsOfConstrainExpressions.extend(signsOfConstrain9)

    constantsOfDecisionVariableOfConstrain7 = []
    constantsOfDecisionVariableOfConstrain6 = ([1 for i in range(temp_obj.I * temp_obj.R)] +
                                               [0 for i in range(temp_obj.R * temp_obj.E)] +
                                               [0 for i in range((temp_obj.I * temp_obj.R) +
                                                                 (temp_obj.R * temp_obj.E))])
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
    for i in range((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)):
        if indeks + 1 > temp_obj.R:
            indeks = 0
        constantsOfDecisionVariableOfConstrain7.append(1 - 1 / temp_obj.V[indeks])
        indeks += 1
    constantsOfDecisionVariableOfConstrain7 += [0 for i in range((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E))]

    for iter in range(temp_obj.R):
        constantsOfDecisionVariableOfConstrain5i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain5i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain5i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain5i4.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain4i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain4i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain4i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain4i4.append([0 for i in range(temp_obj.R * temp_obj.E)])

    for it in range(temp_obj.E):
        constantsOfDecisionVariableOfConstrain3i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain3i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain3i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain3i4.append([0 for i in range(temp_obj.R * temp_obj.E)])

    for itrator in range(temp_obj.I * temp_obj.R):
        constantsOfDecisionVariableOfConstrain1i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain1i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain1i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain1i4.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain8i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain8i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain8i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain8i4.append([0 for i in range(temp_obj.R * temp_obj.E)])

    for ittrator in range(temp_obj.R * temp_obj.E):
        constantsOfDecisionVariableOfConstrain2i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain2i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain2i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain2i4.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain9i1.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain9i2.append([0 for i in range(temp_obj.R * temp_obj.E)])
        constantsOfDecisionVariableOfConstrain9i3.append([0 for i in range(temp_obj.I * temp_obj.R)])
        constantsOfDecisionVariableOfConstrain9i4.append([0 for i in range(temp_obj.R * temp_obj.E)])

    iterator = 0
    iteratorV = 0
    indexOfLists = -1
    for lists in constantsOfDecisionVariableOfConstrain5i1:
        indexOfLists += 1
        iterator = indexOfLists
        while iterator < temp_obj.I * temp_obj.R:
            lists[iterator] = 1 / temp_obj.V[iteratorV]
            iterator += temp_obj.R
        iteratorV += 1

    iterator = 0
    indexOfLists = -1
    for lists in constantsOfDecisionVariableOfConstrain5i2:
        indexOfLists += 1
        iterator = indexOfLists
        for i in range(temp_obj.E):
            lists[iterator] = -1
            iterator += 1
        indexOfLists += temp_obj.E - 1

    iterator = 0
    indexOfLists = -1
    for lists in constantsOfDecisionVariableOfConstrain4i1:
        indexOfLists += 1
        iterator = indexOfLists
        while iterator < temp_obj.I * temp_obj.R:
            lists[iterator] = 1
            iterator += temp_obj.R

    iterator = 0
    indexOfLists = -1
    for lists in constantsOfDecisionVariableOfConstrain3i2:
        indexOfLists += 1
        iterator = indexOfLists
        while iterator < temp_obj.R * temp_obj.E:
            lists[iterator] = 1
            iterator += temp_obj.E

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
        lists[iterator] = 1 / temp_obj.Q_TIR

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
        lists[iterator] = 1 / temp_obj.Q

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

    for i in range(temp_obj.R):
        constantsOfDecisionVariableOfConstrain5arr.extend(constantsOfDecisionVariableOfConstrain5i1[i] +
                                                          constantsOfDecisionVariableOfConstrain5i2[i] +
                                                          constantsOfDecisionVariableOfConstrain5i3[i] +
                                                          constantsOfDecisionVariableOfConstrain5i4[i])
        constantsOfDecisionVariableOfConstrain4arr.extend(constantsOfDecisionVariableOfConstrain4i1[i] +
                                                          constantsOfDecisionVariableOfConstrain4i2[i] +
                                                          constantsOfDecisionVariableOfConstrain4i3[i] +
                                                          constantsOfDecisionVariableOfConstrain4i4[i])

    for i in range(temp_obj.E):
        constantsOfDecisionVariableOfConstrain3arr.extend(constantsOfDecisionVariableOfConstrain3i1[i] +
                                                          constantsOfDecisionVariableOfConstrain3i2[i] +
                                                          constantsOfDecisionVariableOfConstrain3i3[i] +
                                                          constantsOfDecisionVariableOfConstrain3i4[i])

    for i in range(temp_obj.I * temp_obj.R):
        constantsOfDecisionVariableOfConstrain1arr.extend(constantsOfDecisionVariableOfConstrain1i1[i] +
                                                          constantsOfDecisionVariableOfConstrain1i2[i] +
                                                          constantsOfDecisionVariableOfConstrain1i3[i] +
                                                          constantsOfDecisionVariableOfConstrain1i4[i])
        constantsOfDecisionVariableOfConstrain8arr.extend(constantsOfDecisionVariableOfConstrain8i1[i] +
                                                          constantsOfDecisionVariableOfConstrain8i2[i] +
                                                          constantsOfDecisionVariableOfConstrain8i3[i] +
                                                          constantsOfDecisionVariableOfConstrain8i4[i])

    for i in range(temp_obj.R * temp_obj.E):
        constantsOfDecisionVariableOfConstrain2arr.extend(constantsOfDecisionVariableOfConstrain2i1[i] +
                                                          constantsOfDecisionVariableOfConstrain2i2[i] +
                                                          constantsOfDecisionVariableOfConstrain2i3[i] +
                                                          constantsOfDecisionVariableOfConstrain2i4[i])
        constantsOfDecisionVariableOfConstrain9arr.extend(constantsOfDecisionVariableOfConstrain9i1[i] +
                                                          constantsOfDecisionVariableOfConstrain9i2[i] +
                                                          constantsOfDecisionVariableOfConstrain9i3[i] +
                                                          constantsOfDecisionVariableOfConstrain9i4[i])

    constantsOfDecisionVariableOfConstrain5 = \
        ([constantsOfDecisionVariableOfConstrain5arr[y:y + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for y in range(0, len(constantsOfDecisionVariableOfConstrain5arr),
                         ((temp_obj.I * temp_obj.R) +
                          (temp_obj.R * temp_obj.E)) * 2)])
    constantsOfDecisionVariableOfConstrain4 = \
        ([constantsOfDecisionVariableOfConstrain4arr[z:z + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for z in range(0, len(constantsOfDecisionVariableOfConstrain4arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])
    constantsOfDecisionVariableOfConstrain3 = \
        ([constantsOfDecisionVariableOfConstrain3arr[t:t + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for t in range(0, len(constantsOfDecisionVariableOfConstrain3arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])
    constantsOfDecisionVariableOfConstrain2 = \
        ([constantsOfDecisionVariableOfConstrain2arr[x:x + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for x in range(0, len(constantsOfDecisionVariableOfConstrain2arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])
    constantsOfDecisionVariableOfConstrain1 = \
        ([constantsOfDecisionVariableOfConstrain1arr[v:v + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for v in range(0, len(constantsOfDecisionVariableOfConstrain1arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])

    constantsOfDecisionVariableOfConstrain8 = \
        ([constantsOfDecisionVariableOfConstrain8arr[k:k + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for k in range(0, len(constantsOfDecisionVariableOfConstrain8arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])

    constantsOfDecisionVariableOfConstrain9 = \
        ([constantsOfDecisionVariableOfConstrain9arr[p:p + ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2]
          for p in range(0, len(constantsOfDecisionVariableOfConstrain9arr), ((temp_obj.I * temp_obj.R) +
                                                                              (temp_obj.R * temp_obj.E)) * 2)])

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
    columnStartIndices.append(indexOfNoZeroElement + 1)

    lowerBounds = []
    upperBounds = []
    pointersToCharacters = []
    lowerBounds.extend(0 for i in range(((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2))
    upperBounds.extend(1.0E+30 for i in range(((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2))
    pointersToCharacters.extend('C' for i in range((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)))
    pointersToCharacters.extend('I' for i in range((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)))

    J1_I_FIT = []
    for i in temp_obj.J1_I:
        for iteratorR in range(temp_obj.R):
            J1_I_FIT.append(i)

    J1_R_FIT = []
    for i in temp_obj.J1_R:
        for iteratorE in range(temp_obj.E):
            J1_R_FIT.append(i)

    J1_R__1_I_FIT = []
    J1_R__1_E_FIT = []

    J1_R__1_I_FIT.extend(list(map(mul, temp_obj.J1_R__1_I_arr, temp_obj.M1_R__1_I)))
    # J1_R__1_I_FIT = [round(elem, 2) for elem in J1_R__1_I_FIT]

    J1_R__1_E_FIT.extend(list(map(mul, temp_obj.J1_R__1_E_arr, temp_obj.M1_R__1_E)))
    # J1_R__1_E_FIT = [round(elem, 2) for elem in J1_R__1_E_FIT]

    constantsOfFunctionFit = J1_I_FIT + J1_R_FIT + J1_R__1_I_FIT + J1_R__1_E_FIT
    print('Constants of function fit: ', constantsOfFunctionFit, "\n",
          'Length of array of constants of func. fit: ', len(constantsOfFunctionFit))

    flat_matrixOfDecisionVariables = [item for sublist in matrixOfDecisionVariables for item in sublist]

    # \\\\\\\\\\\\\
    # some tests:
    # /////////////
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
    if len(constantsOfDecisionVariableOfConstrain7) == ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2:
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
    if count == ((temp_obj.I + temp_obj.E) * temp_obj.R) and \
            allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2) * temp_obj.R):
        print('constants of decision variable of constrain 5 is fine')
    else:
        print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 5')

    # checking constantsOfDecisionVariableOfConstrain6
    print('constantsOfDecisionVariableOfConstrain6 :', constantsOfDecisionVariableOfConstrain6)
    if len(constantsOfDecisionVariableOfConstrain6) == ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2:
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
    if count == (temp_obj.I * temp_obj.R) and \
            allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2) * temp_obj.R):
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
    if count == (temp_obj.R * temp_obj.E) and allCount == ((((temp_obj.I * temp_obj.R) +
                                                             (temp_obj.R * temp_obj.E)) * 2) * temp_obj.E):
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
    if count == (temp_obj.I * temp_obj.R) and allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2)
                                                           * (temp_obj.I * temp_obj.R)):
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
    if count == (temp_obj.R * temp_obj.E) and allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2)
                                                           * (temp_obj.R * temp_obj.E)):
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
    if count == ((temp_obj.I * temp_obj.R) * 2) and \
            allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2) *
                         (temp_obj.I * temp_obj.R)):
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
    if count == ((temp_obj.R * temp_obj.E) * 2) and \
            allCount == ((((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2) *
                         (temp_obj.R * temp_obj.E)):
        print('constants of decision variable of constrain 9 is fine')
    else:
        print('SOMETHING WRONG WITH CONSTANTS OF DESITION VARIABLES 9')

    # some other tests:
    if len(temp_obj.M1_R__1_I) == len(temp_obj.J1_R__1_I_arr):
        print("M1_R__1_I and J1_R__1_I_arr have the same length")
    else:
        print("M1_R__1_I AND J1_R__1_I_arr HAVE DIFFERENT LENGTH")

    if len(temp_obj.M1_R__1_E) == len(temp_obj.J1_R__1_E_arr):
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
        print(
            'count of constraint equal to count of constants on the right hand of contraint expressions and their signs')
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

    if len(columnStartIndices) - 1 == ((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) * 2:
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

    if len(nonZeroCoeficients) == (((temp_obj.I * temp_obj.R) + (temp_obj.R * temp_obj.E)) +  # constraint 7
                                   ((temp_obj.I + temp_obj.E) * temp_obj.R) +  # constraint 5
                                   (temp_obj.I * temp_obj.R) +  # constraint 6
                                   (temp_obj.I * temp_obj.R) +  # constraint 4
                                   (temp_obj.R * temp_obj.E) +  # constraint 3
                                   (temp_obj.I * temp_obj.R) +  # constraint 1
                                   (temp_obj.R * temp_obj.E) +  # constraint 2
                                   ((temp_obj.I * temp_obj.R) * 2) +  # constraint 8
                                   ((temp_obj.R * temp_obj.E) * 2)):  # constraint 9
        print('Length of non zero coeficients of decision variables is correct')
    else:
        print('LENGTH OF NON ZERO COEFICIENTS OF DECISION VARIABLES IS NOT CORRECT', "\n",
              'Checking why length of non zero coefocoents is not correct:')

    print('pointersToCharacters: ', pointersToCharacters)
    print('len non zero coeficients: ', len(nonZeroCoeficients))
    print('len row indices: ', len(rowIndices))
    print('len column start indices: ', len(columnStartIndices))

    # \\\\\\\\\\\\\\\\\\\\\\\\
    # for measure time of compilation
    # ////////////////////////
    start_time = time.time()

    # \\\\\\\\\\\\\\
    # model data
    # //////////////

    nCons = countOfConstraints  # count of constrains
    nVars = countOfDesitionVariables  # count of decision variables
    nDir = 1  # direction 1 - it`s minimisation of function fit
    dObjConst = 0.0  # constant term in the objective function
    adC = N.array(constantsOfFunctionFit, dtype=N.double)  # coficients of variables in function fit
    adB = N.array(allConstsOfConstraints, dtype=N.double)  # constant on the right hand
    # of constrain expressions
    acConTypes = N.array(signsOfConstrainExpressions, dtype=N.character)  # signs of the
    # constrain expressions
    nNZ = len(nonZeroCoeficients)  # the number of nonzero coefficients in the constraint matrix
    anBegCol = N.array(columnStartIndices, dtype=N.int32)  # column-start indices
    pnLenCol = N.asarray(None)  # if no blanks are been lefy in matrix = None
    adA = N.array(nonZeroCoeficients, dtype=N.double)  # nonzero coefficients
    anRowX = N.array(rowIndices, dtype=N.int32)  # row indices
    pdLower = N.array(lowerBounds, dtype=N.double)  # lower bounds for desition variables
    pdUpper = N.array(upperBounds, dtype=N.double)  # upper bounds for desition variables
    pachVarType = N.array(pointersToCharacters, dtype=N.character)  # A pointer to a character vector
    # containing the type of each variable (‘C’, ‘B’, ‘I’, or ‘S’ for continuous, binary, general integer or
    # semi-continuous, respectively.)

    print("\nnCons", nCons, "\nnVars", nVars, "\nnDir", nDir, "\ndObjCons", dObjConst, "\nlen adC", len(adC), "\nadC",
          adC, "\nlen adB", len(adB), "\nadB", adB, "\nlen acConTypes", len(acConTypes), "\nacConTypes", acConTypes)
    print("\nnNZ", nNZ, "\nlen anBegCol", len(anBegCol), "\nanBegCol", anBegCol, "\npnLenCol", pnLenCol, "\nlen adA",
          len(adA), "\nadA", adA, "\nlen anRowX", len(anRowX), "\nanRowX", anRowX, "\nlen pdLower", len(pdLower),
          "\npdLower", pdLower, "\nlen pdUpper", len(pdUpper), "\npdUpper", pdUpper)
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # create LINDO environment and model objects
    # //////////////////////////////////////////
    LicenseKey = N.array('', dtype='S1024')
    lindo.pyLSloadLicenseString('/home/morton/lindoapi/license/lndapi110.lic',
                                LicenseKey)
    pnErrorCode = N.array([-1], dtype=N.int32)  # A reference to an integer to return the error code
    pEnv = lindo.pyLScreateEnv(pnErrorCode, LicenseKey)

    pModel = lindo.pyLScreateModel(pEnv, pnErrorCode)

    geterrormessage(pEnv, pnErrorCode[0])

    # pszFname = "/home/morton/My_Files/Politechnika_Wroclawska/DYPLOM/Program/LINDO/input.mps"

    # \\\\\\\\\\\\\\\\\\\\\\\\\
    # load data into the model
    # /////////////////////////
    print("Loading LP data...")
    errorcode = lindo.pyLSloadLPData(pModel, nCons, nVars, nDir, dObjConst, adC, adB, acConTypes, nNZ, anBegCol,
                                     pnLenCol,
                                     adA, anRowX, pdLower, pdUpper)
    geterrormessage(pEnv, errorcode)

    errorcode = lindo.pyLSloadVarType(pModel, pachVarType)  # When use pachVarType (for example in MIP problem)

    lindo.pyLSwriteMPSFile(pModel, "something.mps", 0)

    # \\\\\\\\\\\\\\\
    # solve the model
    # ///////////////
    print("Solving the model...")
    pnStatus = N.array([-1], dtype=N.int32)
    # errorcode = lindo.pyLSoptimize(pModel, LSconst.LS_METHOD_FREE, pnStatus)
    errorcode = lindo.pyLSsolveMIP(pModel, pnStatus)
    geterrormessage(pEnv, errorcode)

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # retrieve the objective value
    # //////////////////////////////
    dObj = N.array([-1.0], dtype=N.double)
    # errorcode = lindo.pyLSgetInfo(pModel, LSconst.LS_DINFO_POBJ, dObj)
    errorcode = lindo.pyLSgetInfo(pModel, LSconst.LS_DINFO_MIP_OBJ, dObj)
    geterrormessage(pEnv, errorcode)
    print("Objective is: %.5f" % dObj[0])
    print("")
    with open('research1_2.txt', 'a') as plik:
        plik.write("Objective is: %.5f \n" % dObj[0])
        plik.close()

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # retrieve the primal solution
    # /////////////////////////////
    padPrimal = N.empty((nVars), dtype=N.double)
    # errorcode = lindo.pyLSgetPrimalSolution(pModel, padPrimal)
    errorcode = lindo.pyLSgetMIPPrimalSolution(pModel, padPrimal)
    geterrormessage(pEnv, errorcode)
    print("Primal solution is: ")
    #for x in padPrimal:
        #print("%.5f" % x)
        #with open('research1_2.txt', 'a') as plik:
            #plik.write("Primal solution is: %.5f \n" % x)
    #plik.close()

    # delete LINDO model pointer
    errorcode = lindo.pyLSdeleteModel(pModel)
    geterrormessage(pEnv, errorcode)

    # delete LINDO environment pointer
    errorcode = lindo.pyLSdeleteEnv(pEnv)
    geterrormessage(pEnv, errorcode)

    # show time of execution
    print("--- %s seconds ---" % (time.time() - start_time))