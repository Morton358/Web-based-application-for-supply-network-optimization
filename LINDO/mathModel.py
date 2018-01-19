import random
import itertools
import math
from pandas import *
from operator import add

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Mathemetical model of problem
#//////////////////////////////
#def mathematicalModel(countI, countR, countE):
I = 2 #random.randint(2, 20) # 3
R = 2 #random.randint(2, 10) # 3
E = 2 #random.randint(2, 50) # 5
i = [] # numery jednostek sprzedajacej surowiec
r = [] # numery/indeksy jednostek produkcyjnych
e = [] # numery/indeksy klientow ktorzy tworza zapotrzebowanie w produkcii jednostek produkcyjnych
W = [] # ilosc surowca u kazdego z sprzedawcow
G = [] # obserwowana produkcyjna moc kazdego z zakladow produkcyjnych
K = [] # obserwowany popyt/zapotrzebowanie na produkcje przedsiebiorstwa kazdego klienta
V = [] # wspolczynnik produkcji dla przeliczania ilosci surowca na ilosc produktu na kazdym zakladzie produkcyjnym
J1_I = [] # koszt jednostkowy surowca u kazdego sprzedawcy
J1_R = [] # koszt jednostkowy przetworstwa owocowo-warzywnej produkcji na kazdym zakladzie produkcyjnym
J1_R__1_I_arr = [] # koszt jednostkowy przejazdu od sprzedawcow do zakladow produkcyjnych (jeden ciag kosztow)
J1_R__1_I = [] # koszt jednostkowy przejazdu od sprzedawcow do zakladow produkcyjnych (podzielono od kazdej ...
# jednostki sprzedajacej surowiec do wszystkich zalladow produkcyjnych)
J1_R__1_E_arr = [] # koszt jednostkowy przejazdu od zakladow produkcyjnych do klientow (jeden ciag kosztow)
J1_R__1_E = [] # koszt jednostkowy przejazdu od zakladow produkcyjnych do klientow (podzielono od kazdego zakladu
#  produkcyjnego do wszystkich klientow)
M1_R__1_I = [] # dystans od sprzedawca do zakladu produkcyjnego
M1_R__1_E = [] # dystans od zakladu produkcyjnego do jednostki, sprzedajacej gotowa produkcje
S = [] # koszty uruchomienia zakladow produkcyjnych
Q = 500 # pojemnosc auta dla transportowania gotowej produkcji (w litrach)
Q_TIR = 24000 # pojemnosc auta, ktore transportuje surowiec (w kilogramach)
# Q_TIR_all = [1/Q_TIR] * I * R  # dla zapisywania w funkcje celu
Z = [] # ilosci juz zakupionych surowcow u sprzedawcow (kg)
Z1_R = [] # ilosc juz przywiezionego surowca do zakladow produkcyjnych (kg)
Z1_R_in_l = [] # ilosc juz przywiezionego surowca do zakladow produkcyjnych (l)
Y = [] # ilosc juz wyprodukowanych produktow na zakladach produkcyjnych ale nie dowiezionych jeszcze do klientow
A1_R__1_I_arr = [] # ogolna ilosc surowca, ktora bylo przetransportowano od sprzedawcow do zakladow produkcyjnych
# (jeden ciag ilosci)
A1_R__1_I = [] # ogolna ilosc surowca, ktora bylo przetransportowano od sprzedawcow do zakladow produkcyjnych
A1_R__1_E_arr = [] # ogolna ilosc produktu, ktora bylo przetransportowano od zakladow produkcyjnych
# do klientow (jeden ciag ilosci)
A1_R__1_E = [] #  ogolna ilosc produktu, ktora bylo przetransportowano od zakladow produkcyjnych
# do klientow (lists of lists)
c1_R__1_I_arr = [] # strata przy transportowaniu surowca od sprzedawcow do zakladow produkcyjnych (jeden ciag strat)
c1_R__1_I = [] # strata przy transportowaniu surowca od sprzedawcow do zakladow produkcyjnych (lists of lists)
c1_R__1_E_arr = [] # strata przy transportowaniu produktow od zakladow produkcyjnych do klientow (jeden ciag strat)
c1_R__1_E = [] # strata przy transportowaniu produktow od zakladow produkcyjnych do klientow (lists of lists)
C = [] # strata przy produkcji, na zakladach produkcyjnych
X1_R__1_I_arr = [] # ogolna ilosc surowca, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy
# od sprzedawcow do zakladow produkcyjnych (jeden ciag ilosci)
X1_R__1_I = [] # ogolna ilosc surowca, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy
# od sprzedawcow do zakladow produkcyjnych (lists of lists)
X1_R__1_E_arr = [] # ogolna ilosc produktu, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy
# od zakladow produkcyjnych do klientow (jeden ciag ilosci)
X1_R__1_E = [] # ogolna ilosc produktu, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy
# od zakladow produkcyjnych do klientow (lists of lists)
W1_I = [] # ogolna ilosc surowca, ktorego juz kupilismy oraz bedziemy kupowac u sprzedawcow
D1_R = [] # ogolna ilosc produktu, co wyprodukowalismy oraz bedziemy produkowac na zakladach produkcyjnych
W_all = 0 # ogolna dostepna ilosc surowca do przetwarzania (u sprzedawcow i na zakladach produkcyjnych)
K_all = 0 # ilosc produktu ktora jeszcze trzeba wyprodukowac, zeby spelnic ogolne zapotrzebowanie klientow
G_all = 0 # suma produkcyjnej mocy wszystkich zakladow produkcyjnych
P1_I = [] # koszty zakupionych surowcow od 0 do i-ego sprzedawcy
P1_R = [] # koszty produkowania produktow od 0 do r-ego zakladow produkcyjnych
P1_R__1_I_arr = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakladu produkcyjnego (jeden ciag kosztow)
P1_R__1_I = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakladu produkcyjnego (list of lists)
P1_R__1_E_arr = [] # koszt przewozu produktow z r-ego zakladu produkcyjnego do e-ego klienta (jeden ciag kosztow)
P1_R__1_E = [] # koszt przewozu produktow z r-ego zakladu produkcyjnego do e-ego klienta (list of lists)
P_all = [] # koszt calkowity


for k in range(I):
    i.append(k)
    Wi = random.randint(1000, 10000) # Ilosc surowca w kg.
    W.append(Wi)
    Ji = round(random.uniform(0.5, 3.0), 2) # koszt surowca od 0.5 zl do 3 zl za kilogram
    J1_I.append(Ji)
    for k in range(R):
        Jri = round(random.uniform(2, 4.5), 2) # cena za 1 km przewozu surowca autem ciezarowym
        J1_R__1_I_arr.append(Jri)
        Mri = round(random.uniform(8.0, 35.5), 1) # odleglosc od i-ego sprzdawcy do r-ego przedsiebiorstwa
        M1_R__1_I.append(Mri)
        Ari = random.randint(0, 50000) # ogolna ilosc surowca, ktora bylo przetransportowano od i-ego sprzedawcy
        # do r-ego zakladu produkcyjnego
        A1_R__1_I_arr.append(Ari)
        cri = random.randint(0, 50000) # strata przy transportowaniu surowca od i-ego sprzedawcy do r-ego
        # zakladu produkcyjnego
        c1_R__1_I_arr.append(cri)
        Xri = random.randint(0, 100000) # ogolna ilosc surowca, ktora trzeba przetransportowac oraz ktora
        # juz przetransportowalismy od i-ego sprzedawcy do r-ego zakladu produkcyjnego
        X1_R__1_I_arr.append(Xri)

    Zi = random.randint(500, 10000) # Ilosc juz zakupionego surowca u I-ego sprzedawcy w kg.
    Z.append(Zi)

J1_R__1_I = [J1_R__1_I_arr[y:y + R] for y in range(0, len(J1_R__1_I_arr), R)]
A1_R__1_I = [A1_R__1_I_arr[t:t + R] for t in range(0, len(A1_R__1_I_arr), R)]
c1_R__1_I = [c1_R__1_I_arr[p:p + R] for p in range(0, len(c1_R__1_I_arr), R)]
X1_R__1_I = [X1_R__1_I_arr[c:c + R] for c in range(0, len(X1_R__1_I_arr), R)]


for k in range(R):
    r.append(k)
    Gr = random.randint(10000, 100000) # Produkcyjna moc zakladu produkcyjnego w l. na miesiac
    Vr = round(random.uniform(1, 2.5), 2) # wspolczynnik produkcji surowiec na produkt (od 1 do 2)
    G.append(Gr)
    V.append(Vr)
    Jr = round(random.uniform(1, 1.9), 2) # cena od 1 do 1.9 zl za wyprodukowania 1 l. soku
    J1_R.append(Jr)
    for k in range(E):
        Jre = round(random.uniform(0.4, 2.5), 2) # cena za 1 km przewozu produkcji
        J1_R__1_E_arr.append(Jre)
        Mre = round(random.uniform(1.5, 13.5), 1)  # odleglosc od r-ego przedsiebiorstwa do e-go sprzedawcy
        M1_R__1_E.append(Mre)
        Are = random.randint(0, 5000) # ogolna ilosc produktu, ktora bylo przetransportowano
        # od r-ego zakladu produkcyjnego do e-ego klienta
        A1_R__1_E_arr.append(Are)
        cre = random.randint(0, 5000) # strata przy transportowaniu produktu
        # od r-ego zakladu produkcyjnego do e-ego klienta
        c1_R__1_E_arr.append(cre)
        Xre = Xri = random.randint(0, 50000) # ogolna ilosc produktu, ktora trzeba przetransportowac oraz
        # ktora juz przetransportowalismy od r-ego zakladu produkcyjnego do e-ego klienta
        X1_R__1_E_arr.append(Xre)

    Sr = random.randint(3500, 6500) # koszt uruchomienia zakladow produkcyjnych
    S.append(Sr)
    Zr = random.randint(500, 5000) # Ilosc juz przywiezionego surowca do R-ego zakladu produkcyjnego w kg.
    Z1_R.append(Zr)
    Yr = random.randint(100, 5000)  # ilosc wyprodukowanego produktu na r-ym zakladzie produkcyjnym (w l.)
    Y.append(Yr)
    Cr = random.randint(100, 10000) # strata przy produkcji, na r-ym zakladzie produkcyjnym
    C.append(Cr)

J1_R__1_E = [J1_R__1_E_arr[y:y + E] for y in range(0, len(J1_R__1_E_arr), E)]
A1_R__1_E = [A1_R__1_E_arr[t:t + E] for t in range(0, len(A1_R__1_E_arr), E)]
c1_R__1_E = [c1_R__1_E_arr[p:p + E] for p in range(0, len(c1_R__1_E_arr), E)]
X1_R__1_E = [X1_R__1_E_arr[c:c + E] for c in range(0, len(X1_R__1_E_arr), E)]

for k in range(E):
    e.append(k)
    Ke = random.randint(100, 5000) #Popyt klienta na produkcje przedsiebiorstwa w l.
    K.append(Ke)

W1_I = [sum(b) for b in X1_R__1_I] # ogolna ilosc surowca, ktorego juz kupilismy oraz bedziemy kupowac u sprzedawcow

D1_R = [sum(c) for c in X1_R__1_E] # ogolna ilosc produktu, co wyprodukowalismy oraz bedziemy produkowac
# na zakladach produkcyjnych

W_all = sum(itertools.chain(W, Z, Z1_R)) # ogolna dostepna ilosc surowca
# do przetwarzania (u sprzedawcow i na zakladach produkcyjnych);

K_all = sum(K) - sum(Y) # ilosc produktu ktora jeszcze trzeba wyprodukowac,
# zeby spelnic ogolne zapotrzebowanie klientow

ki = 0
for k in Z1_R:
    Z1_R_in_l.append(k/V[ki])
    ki += 1

G_all = sum(G) - sum(Z1_R_in_l) # suma produkcyjnej mocy wszystkich zakladow produkcyjnych

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

print('numery jednostek sprzedajacej surowiec: ', "\n",
      i, "\n",
      'numery/indeksy jednostek produkcyjnych: ', "\n",
      r, "\n",
      'numery/indeksy klientow ktorzy tworza zapotrzebowanie w produkcii jednostek produkcyjnych: ', "\n",
      e, "\n",
      'ilosc surowca u kazdego z sprzedawcow:', "\n",
      W, "\n",
      'W: ', W, "\n",
      'obserwowana produkcyjna moc kazdego z zakladow produkcyjnych: ', "\n",
      G, "\n",
      'obserwowany popyt/zapotrzebowanie na produkcje przedsiebiorstwa kazdego klienta: ', "\n",
      K, "\n",
      'wspolczynnik produkcji dla przeliczania ilosci surowca na ilosc produktu '
      'na kazdym zakladzie produkcyjnym:', "\n",
      V, "\n",
      'koszt jednostkowy surowca u kazdego sprzedawcy: ', "\n",
      J1_I, "\n",
      'koszt jednostkowy przetworstwa owocowo-warzywnej produkcji na kazdym zakladzie produkcyjnym: ', "\n",
      J1_R, "\n",
      'koszt jednostkowy przejazdu od sprzedawcow do zakladow produkcyjnych: ', "\n",
      DataFrame(J1_R__1_I), "\n",
      'J1_R__1_I: ', J1_R__1_I, "\n",
      'J1_R__1_I_arr: ', J1_R__1_I_arr, "\n",
      'koszt jednostkowy przejazdu od zakladow produkcyjnych do klientow: ', "\n",
      DataFrame(J1_R__1_E), "\n",
      'J1_R__1_E: ', J1_R__1_E, "\n",
      'J1_R__1_E_arr: ', J1_R__1_E_arr, "\n",
      'odleglosc od i-ego sprzdawcy do r-ego przedsiebiorstwa: ', "\n",
      M1_R__1_I, "\n",
      'odleglosc od r-ego przedsiebiorstwa do e-go sprzedawcy: ', "\n",
      M1_R__1_E, "\n",
      'koszty uruchomienia zakladow produkcyjnych: ', "\n",
      S, "\n",
      'pojemnosc auta dla transportowania gotowej produkcji (w litrach): ', "\n",
      Q, "\n",
      'pojemnosc auta, ktore transportuje surowiec (w kilogramach): ', "\n",
      Q_TIR, "\n",
      'ilosci juz zakupionych surowcow u sprzedawcow (kg): ', "\n",
      Z, "\n",
      'ilosc juz przywiezionego surowca do zakladow produkcyjnych (kg): ', "\n",
      Z1_R, "\n",
      'Z1_R:', Z1_R, "\n",
      'A1_R__1_E_arr:', A1_R__1_E_arr, "\n",
      'A1_R__1_I_arr', A1_R__1_I_arr, "\n",
      'ilosc juz wyprodukowanych produktow na zakladach produkcyjnych '
      'ale nie dowiezionych jeszcze do klientow (l): ', "\n",
      Y, "\n",
      'ogolna ilosc surowca, ktora bylo przetransportowano od sprzedawcow do zakladow produkcyjnych: ', "\n",
      DataFrame(A1_R__1_I), "\n",
      A1_R__1_I, "\n",
      'ogolna ilosc produktu, ktora bylo przetransportowano od zakladow produkcyjnych do klientow: ', "\n",
      DataFrame(A1_R__1_E), "\n",
      'A1_R__1_E: ', A1_R__1_E, "\n",
      'strata przy transportowaniu surowca od sprzedawcow do zakladow produkcyjnych: ', "\n",
      DataFrame(c1_R__1_I), "\n",
      'strata przy transportowaniu produktow od zakladow produkcyjnych do klientow: ', "\n",
      DataFrame(c1_R__1_E), "\n",
      'strata przy produkcji, na zakladach produkcyjnych: ', "\n",
      C, "\n",
      'ogolna ilosc surowca, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy '
      'od sprzedawcow do zakladow produkcyjnych: ', "\n",
      DataFrame(X1_R__1_I), "\n",
      'ogolna ilosc produktu, ktora trzeba przetransportowac oraz ktora juz przetransportowalismy '
      'od zakladow produkcyjnych do klientow: ', "\n",
      DataFrame(X1_R__1_E), "\n",
      'ogolna ilosc surowca, ktorego juz kupilismy oraz bedziemy kupowac u sprzedawcow: ', "\n",
      W1_I, "\n",
      'ogolna ilosc produktu, co wyprodukowalismy oraz bedziemy produkowac na zakladach produkcyjnych: ', "\n",
      D1_R, "\n",
      'ogolna dostepna ilosc surowca do przetwarzania: ', "\n",
      W_all, "\n",
      'ilosc produktu ktora jeszcze trzeba wyprodukowac, zeby spelnic ogolne zapotrzebowanie klientow: ', "\n",
      K_all, "\n",
      'suma produkcyjnej mocy wszystkich zakladow produkcyjnych: ', "\n",
      G_all, "\n",
      'koszty zakupionych surowcow od 0 do i-ego sprzedawcy:', "\n",
      P1_I, "\n",
      'koszty produkowania produktow od 0 do r-ego zakladow produkcyjnych:', "\n",
      P1_R, "\n",
      'koszty przewozu surowca od i-ych sprzedawcow do r-ych zakladow produkcyjnych:', "\n",
      DataFrame(P1_R__1_I), "\n",
      'koszty przewozu produktow z r-ych zakladow produkcyjnych do e-ych klientow:', "\n",
      DataFrame(P1_R__1_E), "\n",
      'koszt calkowity. Parametr funkcji celu:', "\n",
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




