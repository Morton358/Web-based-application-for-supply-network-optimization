import random
import itertools
import math
from pandas import *
from operator import add

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Mathemetical model of problem
#//////////////////////////////
#def mathematicalModel(countI, countR, countE):
I = 3 #random.randint(2, 20) # 3
R = 3 #random.randint(2, 10) # 3
E = 3 #random.randint(2, 50) # 5
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
J1_R__1_I = [] # koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych (podzielono od każdej ...
# jednostki sprzedającej surowiec do wszystkich zalładów produkcyjnych)
J1_R__1_E_arr = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (jeden ciąg kosztów)
J1_R__1_E = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (podzielono od każdego zakładu
#  produkcyjnego do wszystkich klientów)
S = [] # koszty uruchomienia zakładów produkcyjnych
Q = 900 # pojemność auta dla transportowania gotowej produkcji (w litrach)
Q_TIR = 24000 # pojemność auta, które transportuje surowiec (w kilogramach)
# Q_TIR_all = [1/Q_TIR] * I * R  # dla zapisywania w funkcje celu
Z = [] # ilości już zakupionych surowców u sprzedawców (kg)
Z1_R = [] # ilość już przywiezionego surowca do zakładów produkcyjnych (kg)
Z1_R_in_l = [] # ilość już przywiezionego surowca do zakładów produkcyjnych (l)
Y = [] # ilość już wyprodukowanych produktów na zakładach produkcyjnych ale nie dowiezionych jeszcze do klientów
A1_R__1_I_arr = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych
# (jeden ciąg ilości)
A1_R__1_I = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych
A1_R__1_E_arr = [] # ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych
# do klientów (jeden ciąg ilości)
A1_R__1_E = [] #  ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych
# do klientów (lists of lists)
c1_R__1_I_arr = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (jeden ciąg strat)
c1_R__1_I = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (lists of lists)
c1_R__1_E_arr = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (jeden ciąg strat)
c1_R__1_E = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (lists of lists)
C = [] # strata przy produkcji, na zakładach produkcyjnych
X1_R__1_I_arr = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy
# od sprzedawców do zakładów produkcyjnych (jeden ciąg ilości)
X1_R__1_I = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy
# od sprzedawców do zakładów produkcyjnych (lists of lists)
X1_R__1_E_arr = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy
# od zakładów produkcyjnych do klientów (jeden ciąg ilości)
X1_R__1_E = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy
# od zakładów produkcyjnych do klientów (lists of lists)
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
        Ari = random.randint(0, 50000) # ogólna ilość surowca, którą było przetransportowano od i-ego sprzedawcy
        # do r-ego zakładu produkcyjnego
        A1_R__1_I_arr.append(Ari)
        cri = random.randint(0, 50000) # strata przy transportowaniu surowca od i-ego sprzedawcy do r-ego
        # zakładu produkcyjnego
        c1_R__1_I_arr.append(cri)
        Xri = random.randint(0, 100000) # ogólna ilość surowca, którą trzeba przetransportować oraz którą
        # już przetransportowaliśmy od i-ego sprzedawcy do r-ego zakładu produkcyjnego
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
        Are = random.randint(0, 5000) # ogólna ilość produktu, którą było przetransportowano
        # od r-ego zakładu produkcyjnego do e-ego klienta
        A1_R__1_E_arr.append(Are)
        cre = random.randint(0, 5000) # strata przy transportowaniu produktu
        # od r-ego zakładu produkcyjnego do e-ego klienta
        c1_R__1_E_arr.append(cre)
        Xre = Xri = random.randint(0, 50000) # ogólna ilość produktu, którą trzeba przetransportować oraz
        # którą już przetransportowaliśmy od r-ego zakładu produkcyjnego do e-ego klienta
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

W1_I = [sum(b) for b in X1_R__1_I] # ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców

D1_R = [sum(c) for c in X1_R__1_E] # ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować
# na zakładach produkcyjnych

W_all = sum(itertools.chain(W, Z, Z1_R)) # ogólna dostępna ilość surowca
# do przetwarzania (u sprzedawców i na zakładach produkcyjnych);

K_all = sum(K) - sum(Y) # ilość produktu którą jeszcze trzeba wyprodukować,
# żeby spełnić ogólne zapotrzebowanie klientów

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
      'współczynnik produkcji dla przeliczania ilości surowca na ilość produktu '
      'na każdym zakładzie produkcyjnym:', "\n",
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
      'ilość już wyprodukowanych produktów na zakładach produkcyjnych '
      'ale nie dowiezionych jeszcze do klientów (l): ', "\n",
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
      'ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy '
      'od sprzedawców do zakładów produkcyjnych: ', "\n",
      DataFrame(X1_R__1_I), "\n",
      'ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy '
      'od zakładów produkcyjnych do klientów: ', "\n",
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


# \\\\\\\\\\\\
# some tests
# ////////////

if sum(P1_I) == sum([J1_I[elem] * W1_I[elem] for elem in range(len(W1_I))]):
    print('the mathematical model is correct')
else:
    print('something goes wrong with mathematical Model!')

if len(A1_R__1_I_arr) + len(A1_R__1_E_arr) == I * R + R * E:
    print('the mathematical model is correct')
else:
    print('something goes wrong with mathematical Model')


'''return (I, R, E, i, r, e, W, G, K, V, J1_I, J1_R, J1_R__1_I, J1_R__1_I_arr, J1_R__1_E, J1_R__1_E_arr, S, Q, Q_TIR,
        Z, Z1_R, Z1_R_in_l, Y, A1_R__1_I, A1_R__1_I_arr, A1_R__1_E, A1_R__1_E_arr, c1_R__1_I, c1_R__1_I_arr,
        c1_R__1_E, c1_R__1_E_arr, C, X1_R__1_I, X1_R__1_I_arr, X1_R__1_E, X1_R__1_E_arr, W1_I, D1_R, W_all, K_all,
        G_all, P1_I, P1_R, P1_R__1_I, P1_R__1_E, P1_R__1_I_arr, P1_R__1_E_arr, P_all)'''


