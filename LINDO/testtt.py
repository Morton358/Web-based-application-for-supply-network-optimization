import random
import itertools
import math
from pandas import *
from operator import add
from pyLindo import *



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Mathemetical model of problem
#//////////////////////////////

I = 5 #random.randint(2, 20) # 3
R = 3 #random.randint(2, 10) # 3
E = 4 #random.randint(2, 50) # 5
i = [] # numery jednostek sprzedającej surowiec
r = [] # numery/indeksy jednostek produkcyjnych
e = [] # numery/indeksy klientów którzy tworzą zapotrzebowanie w produkcii jednostek produkcyjnych
W = [] # ilość surowca u każdego z sprzedawców
G = [] # obserwowana produkcyjna moc każdego z zakładów produkcyjnych
K = [] # obserwowany popyt/zapotrzebowanie na produkcje przedsiębiorstwa każdego klienta
V = [] # współczynnik produkcji dla przeliczania ilości surowca na ilość produktu na każdym zakładzie produkcyjnym
J1_I = [] # koszt jednostkowy surowca u każdego sprzedawcy
J1_R = [] # koszt jednostkowy przetwórstwa owocowo-warzywnej produkcji na każdym zakładzie produkcyjnym
J1_R__1_I_arr = [] # koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych (jeden ciąg kosztów)
J1_R__1_I = [] # koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych (podzielono od każdej jednostki sprzedającej surowiec do wszystkich zalładów produkcyjnych)
J1_R__1_E_arr = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (jeden ciąg kosztów)
J1_R__1_E = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (podzielono od każdego zakładu produkcyjnego do wszystkich klientów)
S = [] # koszty uruchomienia zakładów produkcyjnych
Q = 900 # pojemność auta dla transportowania gotowej produkcji (w litrach)
Q_TIR = 24000 # pojemność auta, które transportuje surowiec (w kilogramach)
# Q_TIR_all = [1/Q_TIR] * I * R  # dla zapisywania w funkcje celu
Z = [] # ilości już zakupionych surowców u sprzedawców (kg)
Z1_R = [] # ilość już przywiezionego surowca do zakładów produkcyjnych (kg)
Z1_R_in_l = [] # ilość już przywiezionego surowca do zakładów produkcyjnych (l)
Y = [] # ilość już wyprodukowanych produktów na zakładach produkcyjnych ale nie dowiezionych jeszcze do klientów
A1_R__1_I_arr = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych (jeden ciąg ilości)
A1_R__1_I = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych (lists of lists)
A1_R__1_E_arr = [] # ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych do klientów (jeden ciąg ilości)
A1_R__1_E = [] #  ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych do klientów (lists of lists)
c1_R__1_I_arr = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (jeden ciąg strat)
c1_R__1_I = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (lists of lists)
c1_R__1_E_arr = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (jeden ciąg strat)
c1_R__1_E = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (lists of lists)
C = [] # strata przy produkcji, na zakładach produkcyjnych
X1_R__1_I_arr = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy od sprzedawców do zakładów produkcyjnych (jeden ciąg ilości)
X1_R__1_I = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy od sprzedawców do zakładów produkcyjnych (lists of lists)
X1_R__1_E_arr = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy od zakładów produkcyjnych do klientów (jeden ciąg ilości)
X1_R__1_E = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy od zakładów produkcyjnych do klientów (lists of lists)
W1_I = [] # ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców
D1_R = [] # ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować na zakładach produkcyjnych
W_all = 0 # ogólna dostępna ilość surowca do przetwarzania (u sprzedawców i na zakładach produkcyjnych)
K_all = 0 # ilość produktu którą jeszcze trzeba wyprodukować, żeby spełnić ogólne zapotrzebowanie klientów
G_all = 0 # suma produkcyjnej mocy wszystkich zakładów produkcyjnych
P1_I = [] # koszty zakupionych surowców od 0 do i-ego sprzedawcy
P1_R = [] # koszty produkowania produktów od 0 do r-ego zakładów produkcyjnych
P1_R__1_I_arr = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakładu produkcyjnego (jeden ciąg kosztów)
P1_R__1_I = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakładu produkcyjnego (list of lists)
P1_R__1_E_arr = [] # koszt przewozu produktów z r-ego zakładu produkcyjnego do e-ego klienta (jeden ciąg kosztów)
P1_R__1_E = [] # koszt przewozu produktów z r-ego zakładu produkcyjnego do e-ego klienta (list of lists)
P_all = [] # koszt całkowity


for k in range(I):
    i.append(k)
    Wi = random.randint(500000, 10000000) # Ilość surowca w kg.
    W.append(Wi)
    Ji = round(random.uniform(0.5, 3.0), 2) # koszt surowca od 0.5 zł do 3 zł za kilogram
    J1_I.append(Ji)
    for k in range(R):
        Jri = round(random.uniform(1, 3.5), 2) # cena za 1 km przewozu surowca autem cięzarowym
        J1_R__1_I_arr.append(Jri)
        Ari = random.randint(0, 50000) # ogólna ilość surowca, którą było przetransportowano od i-ego sprzedawcy do r-ego zakładu produkcyjnego
        A1_R__1_I_arr.append(Ari)
        cri = random.randint(0, 50000) # strata przy transportowaniu surowca od i-ego sprzedawcy do r-ego zakładu produkcyjnego
        c1_R__1_I_arr.append(cri)
        Xri = random.randint(0, 100000) # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy od i-ego sprzedawcy do r-ego zakładu produkcyjnego
        X1_R__1_I_arr.append(Xri)

    Zi = random.randint(10, 25000) # Ilość już zakupionego surowca u I-ego sprzedawcy w kg.
    Z.append(Zi)

J1_R__1_I = [J1_R__1_I_arr[y:y + R] for y in range(0, len(J1_R__1_I_arr), R)]
A1_R__1_I = [A1_R__1_I_arr[t:t + R] for t in range(0, len(A1_R__1_I_arr), R)]
c1_R__1_I = [c1_R__1_I_arr[p:p + R] for p in range(0, len(c1_R__1_I_arr), R)]
X1_R__1_I = [X1_R__1_I_arr[c:c + R] for c in range(0, len(X1_R__1_I_arr), R)]


for k in range(R):
    r.append(k)
    Gr = random.randint(50000, 150000) # Produkcyjna moc zakładu produkcyjnego w l. na miesiąc
    Vr = round(random.uniform(1, 2.5), 2) # współczynnik produkcji surowiec na produkt (od 1 do 2)
    G.append(Gr)
    V.append(Vr)
    Jr = round(random.uniform(1, 1.9), 2) # cena od 1 do 1.9 zł za wyprodukowania 1 l. soku
    J1_R.append(Jr)
    for k in range(E):
        Jre = round(random.uniform(0.4, 2.0), 2) # cena za 1 km przewozu produkcji
        J1_R__1_E_arr.append(Jre)
        Are = random.randint(0, 5000) # ogólna ilość produktu, którą było przetransportowano od r-ego zakładu produkcyjnego do e-ego klienta
        A1_R__1_E_arr.append(Are)
        cre = random.randint(0, 5000) # strata przy transportowaniu produktu od r-ego zakładu produkcyjnego do e-ego klienta
        c1_R__1_E_arr.append(cre)
        Xre = Xri = random.randint(0, 50000) # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy od r-ego zakładu produkcyjnego do e-ego klienta
        X1_R__1_E_arr.append(Xre)

    Sr = random.randint(3500, 6500) # koszt uruchomienia zakładów produkcyjnych
    S.append(Sr)
    Zr = random.randint(5000, 100000) # Ilość już przywiezionego surowca do R-ego zakładu produkcyjnego w kg.
    Z1_R.append(Zr)
    Yr = random.randint(500, 100000)  # ilość wyprodukowanego produktu na r-ym zakładzie produkcyjnym (w l.)
    Y.append(Yr)
    Cr = random.randint(500, 100000) # strata przy produkcji, na r-ym zakładzie produkcyjnym
    C.append(Cr)

J1_R__1_E = [J1_R__1_E_arr[y:y + E] for y in range(0, len(J1_R__1_E_arr), E)]
A1_R__1_E = [A1_R__1_E_arr[t:t + E] for t in range(0, len(A1_R__1_E_arr), E)]
c1_R__1_E = [c1_R__1_E_arr[p:p + E] for p in range(0, len(c1_R__1_E_arr), E)]
X1_R__1_E = [X1_R__1_E_arr[c:c + E] for c in range(0, len(X1_R__1_E_arr), E)]

for k in range(E):
    e.append(k)
    Ke = random.randint(500, 50000) #Popyt klienta na produkcję przedsiębiorstwa w l.
    K.append(Ke)

W1_I = list(map(sum, X1_R__1_I)) # ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców

D1_R = list(map(sum, X1_R__1_E)) # ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować na zakładach produkcyjnych

W_all = sum(itertools.chain(W, Z, Z1_R)) # ogólna dostępna ilość surowca do przetwarzania (u sprzedawców i na zakładach produkcyjnych);

K_all = sum(K) - sum(Y) # ilość produktu którą jeszcze trzeba wyprodukować, żeby spełnić ogólne zapotrzebowanie klientów

ki = 0
for k in Z1_R:
    Z1_R_in_l.append(k/V[ki])
    ki += 1

G_all = sum(G) - sum(Z1_R_in_l) # suma produkcyjnej mocy wszystkich zakładów produkcyjnych

ki = 0
for k in W1_I:
    P1_I.append(k * J1_I[ki])
    ki += 1

ki = 0
for k in D1_R:
    P1_R.append((k * J1_R[ki]) + S[ki])
    ki += 1

list_index = 0
for list in X1_R__1_I:
    number_index = 0
    for number in list:
        P1_R__1_I_arr.append((math.ceil(number / Q_TIR)) * J1_R__1_I[list_index][number_index])
        number_index += 1
    list_index += 1

P1_R__1_I = [P1_R__1_I_arr[y:y + R] for y in range(0, len(P1_R__1_I_arr), R)]

list_index = 0
for list in X1_R__1_E:
    number_index = 0
    for number in list:
        P1_R__1_E_arr.append((math.ceil(number / Q) * J1_R__1_E[list_index][number_index]))
        number_index += 1
    list_index += 1

P1_R__1_E = [P1_R__1_E_arr[z:z + E] for z in range(0, len(P1_R__1_E_arr), E)]


P_all = sum(P1_I) + sum(P1_R) + sum(P1_R__1_I_arr) + sum(P1_R__1_E_arr)


print('numery jednostek sprzedającej surowiec: ', "\n",
      i, "\n",
      'numery/indeksy jednostek produkcyjnych: ', "\n",
      r, "\n",
      'numery/indeksy klientów którzy tworzą zapotrzebowanie w produkcii jednostek produkcyjnych: ', "\n",
      e, "\n",
      'ilość surowca u każdego z sprzedawców:', "\n",
      W, "\n",
      'obserwowana produkcyjna moc każdego z zakładów produkcyjnych: ', "\n",
      G, "\n",
      'obserwowany popyt/zapotrzebowanie na produkcje przedsiębiorstwa każdego klienta: ', "\n",
      K, "\n",
      'współczynnik produkcji dla przeliczania ilości surowca na ilość produktu na każdym zakładzie produkcyjnym:', "\n",
      V, "\n",
      'koszt jednostkowy surowca u każdego sprzedawcy: ', "\n",
      J1_I, "\n",
      'koszt jednostkowy przetwórstwa owocowo-warzywnej produkcji na każdym zakładzie produkcyjnym: ', "\n",
      J1_R, "\n",
      'koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych: ', "\n",
      DataFrame(J1_R__1_I), "\n",
      'koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów: ', "\n",
      DataFrame(J1_R__1_E), "\n",
      'koszty uruchomienia zakładów produkcyjnych: ', "\n",
      S, "\n",
      'pojemność auta dla transportowania gotowej produkcji (w litrach): ', "\n",
      Q, "\n",
      'pojemność auta, które transportuje surowiec (w kilogramach): ', "\n",
      Q_TIR, "\n",
      'ilości już zakupionych surowców u sprzedawców (kg): ', "\n",
      Z, "\n",
      'ilość już przywiezionego surowca do zakładów produkcyjnych (kg): ', "\n",
      Z1_R, "\n",
      'ilość już wyprodukowanych produktów na zakładach produkcyjnych ale nie dowiezionych jeszcze do klientów (l): ', "\n",
      Y, "\n",
      'ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych: ', "\n",
      DataFrame(A1_R__1_I), "\n",
      'ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych do klientów: ', "\n",
      DataFrame(A1_R__1_E), "\n",
      'strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych: ', "\n",
      DataFrame(c1_R__1_I), "\n",
      'strata przy transportowaniu produktów od zakładów produkcyjnych do klientów: ', "\n",
      DataFrame(c1_R__1_E), "\n",
      'strata przy produkcji, na zakładach produkcyjnych: ', "\n",
      C, "\n",
      'ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy od sprzedawców do zakładów produkcyjnych: ', "\n",
      DataFrame(X1_R__1_I), "\n",
      'ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy od zakładów produkcyjnych do klientów: ', "\n",
      DataFrame(X1_R__1_E), "\n",
      'ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców: ', "\n",
      W1_I, "\n",
      'ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować na zakładach produkcyjnych: ', "\n",
      D1_R, "\n",
      'ogólna dostępna ilość surowca do przetwarzania: ', "\n",
      W_all, "\n",
      'ilość produktu którą jeszcze trzeba wyprodukować, żeby spełnić ogólne zapotrzebowanie klientów: ', "\n",
      K_all, "\n",
      'suma produkcyjnej mocy wszystkich zakładów produkcyjnych: ', "\n",
      G_all, "\n",
      'koszty zakupionych surowców od 0 do i-ego sprzedawcy:', "\n",
      P1_I, "\n",
      'koszty produkowania produktów od 0 do r-ego zakładów produkcyjnych:', "\n",
      P1_R, "\n",
      'koszty przewozu surowca od i-ych sprzedawców do r-ych zakładów produkcyjnych:', "\n",
      DataFrame(P1_R__1_I), "\n",
      'koszty przewozu produktów z r-ych zakładów produkcyjnych do e-ych klientów:', "\n",
      DataFrame(P1_R__1_E), "\n",
      'koszt całkowity. Parametr funkcji celu:', "\n",
      P_all, "\n")


#mathModel.mathematicalModel(3, 3, 3)

#\\\\\\\\\\\\
# some tests
#////////////

if sum(P1_I) == sum([J1_I[elem] * W1_I[elem] for elem in range(len(W1_I))]):
    print('all working')
else:
    print('wrong!')


if len(A1_R__1_I_arr) + len(A1_R__1_E_arr) == I * R + R * E:
    print('well done proger')
else:
    print('eeeeee')


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

countOfConstraints = (I * R) + (R * E) + E + R + R + 2
countOfDesitionVariables = (I * R) + (R * E)

sumaA = 0
for i in range(I):
    for r in range(R):
        sumaA += (1 - 1/V[r]) * A1_R__1_I[i][r]


print('sumaA: ', sumaA)

sumaZ = 0
for r in range(R):
    sumaZ += 1/V[r] * Z1_R[r]

print('sumaZ: ', sumaZ)

constOfConstraint7 = sum(itertools.chain(W, Z)) + sumaA + sum(A1_R__1_E_arr) + sum(Y) + sumaZ
constOfConstraint6 = sum(A1_R__1_I_arr) + sum(itertools.chain(W, Z))
constsOfConstraint5 = []
constsOfConstraint4 = []
constsOfConstraint3 = []
constsOfConstraint2 = A1_R__1_E_arr
constsOfConstraint1 = A1_R__1_I_arr

for iteratorR in range(R):
    temporary5 = (sumColumn(A1_R__1_I, iteratorR) - Z1_R[iteratorR]) / V[iteratorR] - Y[iteratorR] - sumRow(A1_R__1_E, iteratorR)
    constsOfConstraint5.append(temporary5)
    temporary4 = G[iteratorR] * V[iteratorR] + sumColumn(A1_R__1_I, iteratorR)
    constsOfConstraint4.append(temporary4)

for iteratorE in range(E):
    temporary3 = K[iteratorE] + sumColumn(A1_R__1_E, iteratorE)
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
signsOfConstrain5 = [equalTo for i in range(R)]
signsOfConstrainExpressions.extend(signsOfConstrain5)
signOfConstrainExpression6 = lessThenEqual
signsOfConstrainExpressions.append(signOfConstrainExpression6)
signsOfConstrain4 = [lessThenEqual for i in range(R)]
signsOfConstrainExpressions.extend(signsOfConstrain4)
signsOfConstrain3 = [greaterThenEqual for i in range(E)]
signsOfConstrainExpressions.extend(signsOfConstrain3)
signsOfConstrain1 = [greaterThenEqual for i in range(R * I)]
signsOfConstrainExpressions.extend(signsOfConstrain1)
signsOfConstrain2 = [greaterThenEqual for i in range(R * E)]
signsOfConstrainExpressions.extend(signsOfConstrain2)


constantsOfDecisionVariableOfConstrain7 = []
constantsOfDecisionVariableOfConstrain6 = [1 for i in range(I * R)] + [0 for i in range(R * E)]
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
for i in range((I * R) + (R * E)):
    if indeks + 1 > R:
        indeks = 0
    constantsOfDecisionVariableOfConstrain7.append(1 - 1/V[indeks])
    indeks += 1

for iter in range(R):
    constantsOfDecisionVariableOfConstrain5i1.append([0 for i in range(I * R)])
    constantsOfDecisionVariableOfConstrain5i2.append([0 for i in range(R * E)])
    constantsOfDecisionVariableOfConstrain4i1.append([0 for i in range(I * R)])
    constantsOfDecisionVariableOfConstrain4i2.append([0 for i in range(R * E)])

for it in range(E):
    constantsOfDecisionVariableOfConstrain3i1.append([0 for i in range(I * R)])
    constantsOfDecisionVariableOfConstrain3i2.append([0 for i in range(R * E)])

for itrator in range(I * R):
    constantsOfDecisionVariableOfConstrain1i1.append([0 for i in range(I * R)])
    constantsOfDecisionVariableOfConstrain1i2.append([0 for i in range(R * E)])

for ittrator in range(R * E):
    constantsOfDecisionVariableOfConstrain2i1.append([0 for i in range(I * R)])
    constantsOfDecisionVariableOfConstrain2i2.append([0 for i in range(R * E)])

iterator = 0
iteratorV = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain5i1:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < I * R:
        lists[iterator] = 1/V[iteratorV]
        iterator += R
    iteratorV += 1

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain5i2:
    indexOfLists += 1
    iterator = indexOfLists
    for i in range(E):
        lists[iterator] = -1
        iterator += 1
    indexOfLists += E-1

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain4i1:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < I * R:
        lists[iterator] = 1
        iterator += R

iterator = 0
indexOfLists = -1
for lists in constantsOfDecisionVariableOfConstrain3i2:
    indexOfLists += 1
    iterator = indexOfLists
    while iterator < R * E:
        lists[iterator] = 1
        iterator += E

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

for i in range(R):
    constantsOfDecisionVariableOfConstrain5arr.extend(constantsOfDecisionVariableOfConstrain5i1[i] + constantsOfDecisionVariableOfConstrain5i2[i])
    constantsOfDecisionVariableOfConstrain4arr.extend(constantsOfDecisionVariableOfConstrain4i1[i] + constantsOfDecisionVariableOfConstrain4i2[i])

for i in range(E):
    constantsOfDecisionVariableOfConstrain3arr.extend(constantsOfDecisionVariableOfConstrain3i1[i] + constantsOfDecisionVariableOfConstrain3i2[i])

for i in range(I * R):
    constantsOfDecisionVariableOfConstrain1arr.extend(constantsOfDecisionVariableOfConstrain1i1[i] + constantsOfDecisionVariableOfConstrain1i2[i])

for i in range(R * E):
    constantsOfDecisionVariableOfConstrain2arr.extend(constantsOfDecisionVariableOfConstrain2i1[i] + constantsOfDecisionVariableOfConstrain2i2[i])

constantsOfDecisionVariableOfConstrain5 = [constantsOfDecisionVariableOfConstrain5arr[y:y + ((I * R) + (R * E))] for y in range(0, len(constantsOfDecisionVariableOfConstrain5arr), ((I * R) + (R * E)))]
constantsOfDecisionVariableOfConstrain4 = [constantsOfDecisionVariableOfConstrain4arr[z:z + ((I * R) + (R * E))] for z in range(0, len(constantsOfDecisionVariableOfConstrain4arr), ((I * R) + (R * E)))]
constantsOfDecisionVariableOfConstrain3 = [constantsOfDecisionVariableOfConstrain3arr[t:t + ((I * R) + (R * E))] for t in range(0, len(constantsOfDecisionVariableOfConstrain3arr), ((I * R) + (R * E)))]
constantsOfDecisionVariableOfConstrain2 = [constantsOfDecisionVariableOfConstrain2arr[x:x + ((I * R) + (R * E))] for x in range(0, len(constantsOfDecisionVariableOfConstrain2arr), ((I * R) + (R * E)))]
constantsOfDecisionVariableOfConstrain1 = [constantsOfDecisionVariableOfConstrain1arr[v:v + ((I * R) + (R * E))] for v in range(0, len(constantsOfDecisionVariableOfConstrain1arr), ((I * R) + (R * E)))]


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
if count == (R * E):
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
if count == (I * R):
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
if count == (R * E):
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
lowerBounds.extend(0 for i in range((I * R) + (R * E)))
upperBounds.extend(1.0E+30 for i in range((I * R) + (R * E)))
pointersToCharacters.extend('I' for i in range((I * R) + (R * E)))


J1_I_FIT = []
for i in J1_I:
    for iteratorR in range(R):
        J1_I_FIT.append(i)

J1_R_FIT = []
for i in J1_R:
    for iteratorE in range(E):
        J1_R_FIT.append(i)

J1_R__1_I_FIT = []
J1_R__1_E_FIT = []
for i in J1_R__1_I_arr:
    J1_R__1_I_FIT.append(i / Q_TIR)

for i in J1_R__1_E_arr:
    J1_R__1_E_FIT.append(i / Q)

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

if countOfDesitionVariables == len(matrixOfDecisionVariables[0]) == len(constantsOfFunctionFit) == len(lowerBounds) == len(upperBounds):
    print('countOfDesitionVariables equal to count of the first row in matrix of Decision Variables ')
else:
    print('countOfDesitionVariables IS NOT equal to count of the first row in matrix of Decision Variables !!!')

if countOfConstraints == len(allConstsOfConstraints) == len(signsOfConstrainExpressions) == len(matrixOfDecisionVariables):
    print('count of constraint equal to count of constants on the right hand of contraint expressions and their signs')
else:
    print(
        'count of constraint _NOT_ equal to count of constants on the right hand of contraint expressions and their signs')

if len(constantsOfDecisionVariableOfConstrain5[0]) == len(constantsOfDecisionVariableOfConstrain7) == len(
        constantsOfDecisionVariableOfConstrain6) == len(constantsOfDecisionVariableOfConstrain4[0]) == len(
        constantsOfDecisionVariableOfConstrain3[0]) == len(constantsOfDecisionVariableOfConstrain2[0]) == len(
        constantsOfDecisionVariableOfConstrain1[0]):
    print('all length of constantsOfDecisionVariableOfConstrain are the same')
else:
    print('hmm.. some length of constantsOfDecisionVariableOfConstrain are different from other !!!')

if len(columnStartIndices) - 1 == ((I * R) + (R * E)):
    print('columnStartIndices have good length')
else:
    print('columnStartIndices have BAD length!!!')

if len(nonZeroCoeficients) == len(rowIndices):
    print('length of nonZeroCoeficients are the same as rowIndices')
else:
    print('length of nonZeroCoeficients are NOT the same as rowIndices!!!')

if countOfConstraints == len(matrixOfDecisionVariables) == len(allConstsOfConstraints) == len(signsOfConstrainExpressions):
    print('count of constraint is fine')
else:
    print('count wrong')

if len(nonZeroCoeficients) == (I * R) + (R * E) + (I * R) + (R * E) + (I * R) + (I * R) + (R * E) + (I * R) + (R * E):
    print('Length of non zero coeficients of decision variables is correct')
else:
    print('LENGTH OF NON ZERO COEFICIENTS OF DECISION VARIABLES IS NOT CORRECT', "\n",
          'Checking why length of non zero coefocoents is not correct:')
    if len(constantsOfDecisionVariableOfConstrain7) == ((I * R) + (R * E)):
        print('constants of decision variable of constrain 7 is fine')
    else:
        print('constants of decision variable of constrain 7 is NOT fine', "\n",
              'len of constants of desition variable 7:', len(constantsOfDecisionVariableOfConstrain7), "\n",
              'factual length: ', ((I * R) + (R * E)))

    count = 0
    allCount = 0
    for i in range(len(constantsOfDecisionVariableOfConstrain5)):
        for j in constantsOfDecisionVariableOfConstrain5[i]:
            allCount += 1
            if j != 0:
                count += 1
    if count == ((I * R) + (R * E)):
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
    if count == (I * R):
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
    if count == (I * R):
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
adC = N.array(constantsOfFunctionFit,dtype=N.double) # coficients of variables in function fit
adB = N.array(allConstsOfConstraints,dtype=N.double) # constant on the right hand of constrain expressions
acConTypes = N.array(signsOfConstrainExpressions,dtype=N.character) # signs of the constrain expressions
nNZ = len(nonZeroCoeficients)  # the number of nonzero coefficients in the constraint matrix
anBegCol = N.array(columnStartIndices,dtype=N.int32) # column-start indices
pnLenCol = N.asarray(None) # if no blanks are been lefy in matrix = None
adA = N.array(nonZeroCoeficients,dtype=N.double) # nonzero coefficients
anRowX = N.array(rowIndices,dtype=N.int32) # row indices
pdLower = N.array(lowerBounds,dtype=N.double) # lower bounds for desition variables
pdUpper = N.array(upperBounds,dtype=N.double) # upper bounds for desition variables
#pachVarType = N.array(pointersToCharacters,dtype=N.character) # A pointer to a character vector containing the type of each variable (‘C’, ‘B’, ‘I’, or ‘S’ for continuous, binary, general integer or semi-continuous, respectively.)

print("\nnCons", nCons, "\nnVars", nVars, "\nnDir", nDir, "\ndObjCons", dObjConst, "\nlen adC", len(adC), "\nadC", adC, "\nlen adB", len(adB),"\nadB", adB, "\nlen acConTypes", len(acConTypes), "\nacConTypes", acConTypes)
print("\nnNZ", nNZ, "\nlen anBegCol", len(anBegCol), "\nanBegCol", anBegCol, "\npnLenCol", pnLenCol, "\nlen adA", len(adA), "\nadA", adA, "\nlen anRowX", len(anRowX), "\nanRowX", anRowX, "\nlen pdLower", len(pdLower), "\npdLower", pdLower, "\nlen pdUpper", len(pdUpper), "\npdUpper", pdUpper)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#create LINDO environment and model objects
#//////////////////////////////////////////
LicenseKey = N.array('',dtype='S1024')
lindo.pyLSloadLicenseString('/home/morton/My_Files/Politechnika_Wroclawska/DYPLOM/lindoapi/license/lndapi100.lic',LicenseKey)
pnErrorCode = N.array([-1],dtype=N.int32) # A reference to an integer to return the error code
pEnv = lindo.pyLScreateEnv(pnErrorCode,LicenseKey)

pModel = lindo.pyLScreateModel(pEnv,pnErrorCode)

geterrormessage(pEnv,pnErrorCode[0])


#\\\\\\\\\\\\\\\\\\\\\\\\\
#load data into the model
#/////////////////////////
print("Loading LP data...")
errorcode = lindo.pyLSloadLPData(pModel,nCons,nVars,nDir,
                                 dObjConst,adC,adB,acConTypes,nNZ,anBegCol,
                                 pnLenCol,adA,anRowX,pdLower,pdUpper)
geterrormessage(pEnv,errorcode)


#\\\\\\\\\\\\\\\
#solve the model
#///////////////
print("Solving the model...")
pnStatus = N.array([-1],dtype=N.int32)
errorcode = lindo.pyLSoptimize(pModel,LSconst.LS_METHOD_FREE,pnStatus)
geterrormessage(pEnv,errorcode)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the objective value
#//////////////////////////////
dObj = N.array([-1.0],dtype=N.double)
errorcode = lindo.pyLSgetInfo(pModel,LSconst.LS_DINFO_POBJ,dObj)
geterrormessage(pEnv,errorcode)
print("Objective is: %.5f" %dObj[0])
print("")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the primal solution
#/////////////////////////////
padPrimal = N.empty((nVars),dtype=N.double)
errorcode = lindo.pyLSgetPrimalSolution(pModel,padPrimal)
geterrormessage(pEnv,errorcode)
print("Primal solution is: ")
for x in padPrimal: print("%.5f" % x)


#delete LINDO model pointer
errorcode = lindo.pyLSdeleteModel(pModel)
geterrormessage(pEnv,errorcode)

#delete LINDO environment pointer
errorcode = lindo.pyLSdeleteEnv(pEnv)
geterrormessage(pEnv,errorcode)
