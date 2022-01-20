Tc_tess = 2458386.578190
Tc_taste = 2459174.317808
P = 2.423849

E = int(abs(Tc_tess-Tc_taste)/P)+1
print(E)

Tc = Tc_tess+E*P
D = Tc-Tc_taste
print(D)
print(D*24*60)