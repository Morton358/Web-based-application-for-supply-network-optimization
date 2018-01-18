# -*- coding: utf-8 -*-
import random
import itertools
import math
from pandas import *
from operator import add

class Modell:
    'Mathemetical model of problem'

    def __init__(self, arr):
        self.I = arr[0]
        self.R = arr[1]
        self.E = arr[2]

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #Mathemetical model of problem
        #//////////////////////////////
        #def mathematicalModel(countI, countR, countE):
        #I = 3 #random.randint(2, 20) # 3
        #R = 3 #random.randint(2, 10) # 3
        #E = 5 #random.randint(2, 50) # 5
        self.i = [] # numery jednostek sprzedającej surowiec
        self.r = [] # numery/indeksy jednostek produkcyjnych
        self.e = [] # numery/indeksy klientów którzy tworzą zapotrzebowanie w produkcii jednostek produkcyjnych
        self.W = [] # ilość surowca u każdego z sprzedawców
        self.G = [] # obserwowana produkcyjna moc każdego z zakładów produkcyjnych
        self.K = [] # obserwowany popyt/zapotrzebowanie na produkcje przedsiębiorstwa każdego klienta
        self.V = [] # współczynnik produkcji dla przeliczania ilości surowca na ilość produktu na każdym zakładzie produkcyjnym
        self.J1_I = [] # koszt jednostkowy surowca u każdego sprzedawcy
        self.J1_R = [] # koszt jednostkowy przetwórstwa owocowo-warzywnej produkcji na każdym zakładzie produkcyjnym
        self.J1_R__1_I_arr = [] # koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych (jeden ciąg kosztów)
        self.J1_R__1_I = [] # koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych (podzielono od każdej ...
        # jednostki sprzedającej surowiec do wszystkich zalładów produkcyjnych)
        self.J1_R__1_E_arr = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (jeden ciąg kosztów)
        self.J1_R__1_E = [] # koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów (podzielono od każdego zakładu
        #  produkcyjnego do wszystkich klientów)
        self.M1_R__1_I = [] # dystans od sprzedawca do zakładu produkcyjnego
        self.M1_R__1_E = [] # dystans od zakładu produkcyjnego do jednostki, sprzedającej gotową produkcję
        self.S = [] # koszty uruchomienia zakładów produkcyjnych
        self.Q = 500 # pojemność auta dla transportowania gotowej produkcji (w litrach)
        self.Q_TIR = 200 # 2400 pojemność auta, które transportuje surowiec (w kilogramach)
        # Q_TIR_all = [1/Q_TIR] * I * R  # dla zapisywania w funkcje celu
        self.Z = [] # ilości już zakupionych surowców u sprzedawców (kg)
        self.Z1_R = [] # ilość już przywiezionego surowca do zakładów produkcyjnych (kg)
        self.Z1_R_in_l = [] # ilość już pfładów produkcyjnych (l)
        self.Y = [] # ilość już wyprodukowanych produktów na zakładach produkcyjnych ale nie dowiezionych jeszcze do klientów
        self.A1_R__1_I_arr = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych
        # (jeden ciąg ilości)
        self.A1_R__1_I = [] # ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych
        self.A1_R__1_E_arr = [] # ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych
        # do klientów (jeden ciąg ilości)
        self.A1_R__1_E = [] #  ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych
        # do klientów (lists of lists)
        self.c1_R__1_I_arr = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (jeden ciąg strat)
        self.c1_R__1_I = [] # strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych (lists of lists)
        self.c1_R__1_E_arr = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (jeden ciąg strat)
        self.c1_R__1_E = [] # strata przy transportowaniu produktów od zakładów produkcyjnych do klientów (lists of lists)
        self.C = [] # strata przy produkcji, na zakładach produkcyjnych
        self.X1_R__1_I_arr = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy
        # od sprzedawców do zakładów produkcyjnych (jeden ciąg ilości)
        self.X1_R__1_I = [] # ogólna ilość surowca, którą trzeba przetransportować oraz którą już przetransportowaliśmy
        # od sprzedawców do zakładów produkcyjnych (lists of lists)
        self.X1_R__1_E_arr = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy
        # od zakładów produkcyjnych do klientów (jeden ciąg ilości)
        self.X1_R__1_E = [] # ogólna ilość produktu, którą trzeba przetransportować oraz którą już przetransportowaliśmy
        # od zakładów produkcyjnych do klientów (lists of lists)
        self.W1_I = [] # ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców
        self.D1_R = [] # ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować na zakładach produkcyjnych
        self.W_all = 0 # ogólna dostępna ilość surowca do przetwarzania (u sprzedawców i na zakładach produkcyjnych)
        self.K_all = 0 # ilość produktu którą jeszcze trzeba wyprodukować, żeby spełnić ogólne zapotrzebowanie klientów
        self.G_all = 0 # suma produkcyjnej mocy wszystkich zakładów produkcyjnych
        self.P1_I = [] # koszty zakupionych surowców od 0 do i-ego sprzedawcy
        self.P1_R = [] # koszty produkowania produktów od 0 do r-ego zakładów produkcyjnych
        self.P1_R__1_I_arr = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakładu produkcyjnego (jeden ciąg kosztów)
        self.P1_R__1_I = [] # koszt przewozu surowca od i-ego sprzedawcy do r-ego zakładu produkcyjnego (list of lists)
        self.P1_R__1_E_arr = [] # koszt przewozu produktów z r-ego zakładu produkcyjnego do e-ego klienta (jeden ciąg kosztów)
        self.P1_R__1_E = [] # koszt przewozu produktów z r-ego zakładu produkcyjnego do e-ego klienta (list of lists)
        self.P_all = [] # koszt całkowity


        for k in range(self.I):
            self.i.append(k)
            Wi = random.randint(1000, 10000) # Ilość surowca w kg.
            self.W.append(Wi)
            Ji = round(random.uniform(0.5, 3.0), 2) # koszt surowca od 0.5 zł do 3 zł za kilogram
            self.J1_I.append(Ji)
            for k in range(self.R):
                Jri = round(random.uniform(2, 4.5), 2) # cena za 1 km przewozu surowca autem cięzarowym
                self.J1_R__1_I_arr.append(Jri)
                Mri = round(random.uniform(8.0, 35.5), 1) # odległość od i-ego sprzdawcy do r-ego przedsiębiorstwa
                self.M1_R__1_I.append(Mri)
                Ari = random.randint(0, 50000) # ogólna ilość surowca, którą było przetransportowano od i-ego sprzedawcy
                # do r-ego zakładu produkcyjnego
                self.A1_R__1_I_arr.append(Ari)
                cri = random.randint(0, 50000) # strata przy transportowaniu surowca od i-ego sprzedawcy do r-ego
                # zakładu produkcyjnego
                self.c1_R__1_I_arr.append(cri)
                Xri = random.randint(0, 100000) # ogólna ilość surowca, którą trzeba przetransportować oraz którą
                # już przetransportowaliśmy od i-ego sprzedawcy do r-ego zakładu produkcyjnego
                self.X1_R__1_I_arr.append(Xri)

            Zi = random.randint(1000, 10000) # Ilość już zakupionego surowca u I-ego sprzedawcy w kg.
            self.Z.append(Zi)

        J1_R__1_I = [self.J1_R__1_I_arr[y:y + self.R] for y in range(0, len(self.J1_R__1_I_arr), self.R)]
        self.A1_R__1_I = [self.A1_R__1_I_arr[t:t + self.R] for t in range(0, len(self.A1_R__1_I_arr), self.R)]
        c1_R__1_I = [self.c1_R__1_I_arr[p:p + self.R] for p in range(0, len(self.c1_R__1_I_arr), self.R)]
        X1_R__1_I = [self.X1_R__1_I_arr[c:c + self.R] for c in range(0, len(self.X1_R__1_I_arr), self.R)]


        for k in range(self.R):
            self.r.append(k)
            Gr = random.randint(50000, 100000) # Produkcyjna moc zakładu produkcyjnego w l. na miesiąc
            Vr = round(random.uniform(1, 2.5), 2) # współczynnik produkcji surowiec na produkt (od 1 do 2)
            self.G.append(Gr)
            self.V.append(Vr)
            Jr = round(random.uniform(1, 1.9), 2) # cena od 1 do 1.9 zł za wyprodukowania 1 l. soku
            self.J1_R.append(Jr)
            for k in range(self.E):
                Jre = round(random.uniform(0.4, 2.5), 2) # cena za 1 km przewozu produkcji
                self.J1_R__1_E_arr.append(Jre)
                Mre = round(random.uniform(1.5, 13.5), 1)  # odległość od r-ego przedsiębiorstwa do e-go sprzedawcy
                self.M1_R__1_E.append(Mre)
                Are = random.randint(0, 5000) # ogólna ilość produktu, którą było przetransportowano
                # od r-ego zakładu produkcyjnego do e-ego klienta
                self.A1_R__1_E_arr.append(Are)
                cre = random.randint(0, 5000) # strata przy transportowaniu produktu
                # od r-ego zakładu produkcyjnego do e-ego klienta
                self.c1_R__1_E_arr.append(cre)
                Xre = Xri = random.randint(0, 50000) # ogólna ilość produktu, którą trzeba przetransportować oraz
                # którą już przetransportowaliśmy od r-ego zakładu produkcyjnego do e-ego klienta
                self.X1_R__1_E_arr.append(Xre)

            Sr = random.randint(3500, 6500) # koszt uruchomienia zakładów produkcyjnych
            self.S.append(Sr)
            Zr = random.randint(1000, 8000) # Ilość już przywiezionego surowca do R-ego zakładu produkcyjnego w kg.
            self.Z1_R.append(Zr)
            Yr = random.randint(500, 5000)  # ilość wyprodukowanego produktu na r-ym zakładzie produkcyjnym (w l.)
            self.Y.append(Yr)
            Cr = random.randint(500, 5000) # strata przy produkcji, na r-ym zakładzie produkcyjnym
            self.C.append(Cr)

        J1_R__1_E = [self.J1_R__1_E_arr[y:y + self.E] for y in range(0, len(self.J1_R__1_E_arr), self.E)]
        self.A1_R__1_E = [self.A1_R__1_E_arr[t:t + self.E] for t in range(0, len(self.A1_R__1_E_arr), self.E)]
        c1_R__1_E = [self.c1_R__1_E_arr[p:p + self.E] for p in range(0, len(self.c1_R__1_E_arr), self.E)]
        X1_R__1_E = [self.X1_R__1_E_arr[c:c + self.E] for c in range(0, len(self.X1_R__1_E_arr), self.E)]

        for k in range(self.E):
            self.e.append(k)
            Ke = random.randint(100, 5000) #Popyt klienta na produkcję przedsiębiorstwa w l.
            self.K.append(Ke)

        W1_I = [sum(b) for b in X1_R__1_I] # ogólna ilość surowca, którego już kupiliśmy oraz będziemy kupować u sprzedawców

        D1_R = [sum(c) for c in X1_R__1_E] # ogólna ilość produktu, co wyprodukowaliśmy oraz będziemy produkować
        # na zakładach produkcyjnych

        W_all = sum(itertools.chain(self.W, self.Z, self.Z1_R)) # ogólna dostępna ilość surowca
        # do przetwarzania (u sprzedawców i na zakładach produkcyjnych);

        K_all = sum(self.K) - sum(self.Y) # ilość produktu którą jeszcze trzeba wyprodukować,
        # żeby spełnić ogólne zapotrzebowanie klientów

        ki = 0
        for k in self.Z1_R:
            self.Z1_R_in_l.append(k/self.V[ki])
            ki += 1

        G_all = sum(self.G) - sum(self.Z1_R_in_l) # suma produkcyjnej mocy wszystkich zakładów produkcyjnych

        ki = 0
        for k in W1_I:
            self.P1_I.append(k * self.J1_I[ki])
            ki += 1

        ki = 0
        for k in D1_R:
            self.P1_R.append((k * self.J1_R[ki]) + self.S[ki])
            ki += 1

        list_index = 0
        for list in X1_R__1_I:
            number_index = 0
            for number in list:
                self.P1_R__1_I_arr.append((math.ceil(number / self.Q_TIR)) * J1_R__1_I[list_index][number_index])
                number_index += 1
            list_index += 1

        P1_R__1_I = [self.P1_R__1_I_arr[y:y + self.R] for y in range(0, len(self.P1_R__1_I_arr), self.R)]

        list_index = 0
        for list in X1_R__1_E:
            number_index = 0
            for number in list:
                self.P1_R__1_E_arr.append((math.ceil(number / self.Q) * J1_R__1_E[list_index][number_index]))
                number_index += 1
            list_index += 1

        P1_R__1_E = [self.P1_R__1_E_arr[z:z + self.E] for z in range(0, len(self.P1_R__1_E_arr), self.E)]


        P_all = sum(self.P1_I) + sum(self.P1_R) + sum(self.P1_R__1_I_arr) + sum(self.P1_R__1_E_arr)

        print('numery jednostek sprzedającej surowiec: ', "\n",
              self.i, "\n",
              'numery/indeksy jednostek produkcyjnych: ', "\n",
              self.r, "\n",
              'numery/indeksy klientów którzy tworzą zapotrzebowanie w produkcii jednostek produkcyjnych: ', "\n",
              self.e, "\n",
              'ilość surowca u każdego z sprzedawców:', "\n",
              self.W, "\n",
              'W: ', self.W, "\n",
              'obserwowana produkcyjna moc każdego z zakładów produkcyjnych: ', "\n",
              self.G, "\n",
              'obserwowany popyt/zapotrzebowanie na produkcje przedsiębiorstwa każdego klienta: ', "\n",
              self.K, "\n",
              'współczynnik produkcji dla przeliczania ilości surowca na ilość produktu '
              'na każdym zakładzie produkcyjnym:', "\n",
              self.V, "\n",
              'koszt jednostkowy surowca u każdego sprzedawcy: ', "\n",
              self.J1_I, "\n",
              'koszt jednostkowy przetwórstwa owocowo-warzywnej produkcji na każdym zakładzie produkcyjnym: ', "\n",
              self.J1_R, "\n",
              'koszt jednostkowy przejazdu od sprzedawców do zakładów produkcyjnych: ', "\n",
              DataFrame(J1_R__1_I), "\n",
              'J1_R__1_I: ', J1_R__1_I, "\n",
              'J1_R__1_I_arr: ', self.J1_R__1_I_arr, "\n",
              'koszt jednostkowy przejazdu od zakładów produkcyjnych do klientów: ', "\n",
              DataFrame(J1_R__1_E), "\n",
              'J1_R__1_E: ', J1_R__1_E, "\n",
              'J1_R__1_E_arr: ', self.J1_R__1_E_arr, "\n",
              'odległość od i-ego sprzdawcy do r-ego przedsiębiorstwa: ', "\n",
              self.M1_R__1_I, "\n",
              'odległość od r-ego przedsiębiorstwa do e-go sprzedawcy: ', "\n",
              self.M1_R__1_E, "\n",
              'koszty uruchomienia zakładów produkcyjnych: ', "\n",
              self.S, "\n",
              'pojemność auta dla transportowania gotowej produkcji (w litrach): ', "\n",
              self.Q, "\n",
              'pojemność auta, które transportuje surowiec (w kilogramach): ', "\n",
              self.Q_TIR, "\n",
              'ilości już zakupionych surowców u sprzedawców (kg): ', "\n",
              self.Z, "\n",
              'ilość już przywiezionego surowca do zakładów produkcyjnych (kg): ', "\n",
              self.Z1_R, "\n",
              'Z1_R:', self.Z1_R, "\n",
              'A1_R__1_E_arr:', self.A1_R__1_E_arr, "\n",
              'A1_R__1_I_arr', self.A1_R__1_I_arr, "\n",
              'ilość już wyprodukowanych produktów na zakładach produkcyjnych '
              'ale nie dowiezionych jeszcze do klientów (l): ', "\n",
              self.Y, "\n",
              'ogólna ilość surowca, którą było przetransportowano od sprzedawców do zakładów produkcyjnych: ', "\n",
              DataFrame(self.A1_R__1_I), "\n",
              self.A1_R__1_I, "\n",
              'ogólna ilość produktu, którą było przetransportowano od zakładów produkcyjnych do klientów: ', "\n",
              DataFrame(self.A1_R__1_E), "\n",
              'A1_R__1_E: ', self.A1_R__1_E, "\n",
              'strata przy transportowaniu surowca od sprzedawców do zakładów produkcyjnych: ', "\n",
              DataFrame(c1_R__1_I), "\n",
              'strata przy transportowaniu produktów od zakładów produkcyjnych do klientów: ', "\n",
              DataFrame(c1_R__1_E), "\n",
              'strata przy produkcji, na zakładach produkcyjnych: ', "\n",
              self.C, "\n",
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
              self.P1_I, "\n",
              'koszty produkowania produktów od 0 do r-ego zakładów produkcyjnych:', "\n",
              self.P1_R, "\n",
              'koszty przewozu surowca od i-ych sprzedawców do r-ych zakładów produkcyjnych:', "\n",
              DataFrame(P1_R__1_I), "\n",
              'koszty przewozu produktów z r-ych zakładów produkcyjnych do e-ych klientów:', "\n",
              DataFrame(P1_R__1_E), "\n",
              'koszt całkowity. Parametr funkcji celu:', "\n",
              P_all, "\n")


        # \\\\\\\\\\\\
        # some tests
        # ////////////

        if sum(self.P1_I) == sum([self.J1_I[elem] * W1_I[elem] for elem in range(len(W1_I))]):
            print('the mathematical model is correct')
        else:
            print('something goes wrong with mathematical Model!')

        if len(self.A1_R__1_I_arr) + len(self.A1_R__1_E_arr) == self.I * self.R + self.R * self.E:
            print('the mathematical model is correct')
        else:
            print('something goes wrong with mathematical Model')




