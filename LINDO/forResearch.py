I = 3 #random.randint(2, 20) # 3
R = 2 #random.randint(2, 10) # 3
E = 3 #random.randint(2, 50) # 5

V = [2.39, 1.9] # współczynnik produkcji dla przeliczania ilości surowca na ilość produktu na każdym zakładzie
# produkcyjnym
W = [1000000, 3500000, 2500000] # ilość surowca u każdego z sprzedawców
Z1_R = [55571, 4968] # ilość już przywiezionego surowca do zakładów produkcyjnych (kg)
A1_R__1_E_arr = [1830, 1563, 2901, 1516, 2616, 3795, 2896, 801, 2662, 2485]
A1_R__1_I_arr = [23977, 31649, 6688, 29315, 5710, 25522] # ogólna ilość surowca, którą było
# przetransportowano od sprzedawców do zakładów produkcyjnych (jeden ciąg ilości)
J1_R__1_E = [[2.21, 1.77, 1.44, 1.1, 1.83], [1.99, 2.03, 1.14, 2.3, 1.28]]
J1_R__1_E_arr = [2.21, 1.77, 1.44, 1.1, 1.83, 1.99, 2.03, 1.14, 2.3, 1.28] # ogólna ilość produktu, którą było
# przetransportowano od zakładów produkcyjnych do klientów (jeden ciąg ilości)
J1_R__1_I = [[2.5, 2.88], [3.54, 2.72], [3.47, 3.46]] # koszt jednostkowy przejazdu od sprzedawców
# do zakładów produkcyjnych (podzielono od każdej jednostki sprzedającej surowiec do wszystkich zalładów produkcyjnych)
J1_R__1_I_arr = [2.5, 2.88, 3.54, 2.72, 3.47, 3.46]
A1_R__1_I = [[23977, 31649], [6688, 29315], [5710, 25522]]
A1_R__1_E = [[1830, 1563, 2901, 1516, 2616], [3795, 2896, 801, 2662, 2485]]
Z = [22758, 21374, 14321] # ilości już zakupionych surowców u sprzedawców (kg)
Y = [21386, 23309] # ilość już wyprodukowanych produktów na zakładach produkcyjnych ale nie dowiezionych
# jeszcze do klientów
Q_TIR = 24000
Q = 500
J1_I = [0.66, 2.69, 0.76] # koszt jednostkowy surowca u każdego sprzedawcy
J1_R = [1.35, 1.14] # koszt jednostkowy przetwórstwa owocowo-warzywnej produkcji na każdym zakładzie produkcyjnym
M1_R__1_I = [30.3, 10.6, 28.6, 30.7, 12.9, 26.7] # dystans od sprzedawca do zakładu produkcyjnego
M1_R__1_E = [7.6, 10.0, 5.3, 10.7, 1.8, 13.2, 2.8, 2.5, 8.7, 13.2]
G = [139414, 638021]  # obserwowana produkcyjna moc każdego z zakładów produkcyjnych
K =  [36374, 36597, 13718, 47998, 39443] # obserwowany popyt/zapotrzebowanie na produkcje przedsiębiorstwa każdego klienta

