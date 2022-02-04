#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:17:29 2022

@author: adri
"""

#import math
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams.update({'lines.markeredgewidth': 1})
#plt.rc(usetex = True)
plt.rcParams['font.size'] = 20
#import seaborn as sns

fig1 = plt.figure(figsize=(10, 6))




# MASS
# RV: 0.88 ±0.07
# Anderson: 0.889 ± 0.062
# Addison: 0.858 + 0.072-0.068
# Turner: 0.867±0.064


x_values = [1,2,3,4]
y_values = [0.88,0.889,0.858,0.867]

y_low=[0.07,0.062,0.068,0.064]
y_up=[0.07,0.062,0.072,0.064]

plt.errorbar(x_values, y_values,  yerr=(y_low,y_up) ,fmt='o', markersize=10, capsize = 5)

plt.ylabel(r'$\mathrm{M_{P} sini [m s^{-1}] }$', fontsize = 16)
plt.xlabel("Literature", fontsize = 16)
LABELS = ["Present study (RV)", "Anderson (2011)", "Addison (2019)", "Turner (2016)"]
plt.xticks(x_values, LABELS, fontsize = 14)
plt.show()



# PERIOD
# TESS: 2.42385 pm 0.00017
# Anderson:  2.423804 ±0.000009 d
# Addison: 2.423802 +0.000032-0.000030
# Turner: 2.4238120±0.0000012


x_values = [1,2,3,4]
y_values = [ 2.42385,2.423804,2.423802,2.4238120]

y_low=[0.00017,0.000009,0.000030,0.0000012]
y_up=[0.00017,0.000009,0.000032,0.0000012]

plt.errorbar(x_values, y_values,  yerr=(y_low,y_up) ,fmt='o', markersize=10, capsize = 5)

plt.ylabel(r'$\mathrm{Period [d]} $', fontsize = 16)
plt.xlabel("Literature", fontsize = 16)
LABELS = ["TESS", "Anderson (2011)", "Addison (2019)", "Turner (2016)"]
plt.xticks(x_values, LABELS, fontsize = 16)
plt.show()



# SCALED PLANETARY RADIUS
# TESS: 0.1170+0.0025−0.0026
# TASTE: 0.1283 ±0.0035 (uniform prior)
# Anderson: 0.1260 ±0.0030
# Addison: 0.1255 ± 0.0021
# Turner: 0.1228 pm 0.0028

x_values = [1,2,3,4,5]
y_values = [ 0.1170,0.1283,0.1260,0.1255, 0.1228]

y_low=[0.0026,0.0035 ,0.0030,0.0021, 0.0028]
y_up=[0.0025,0.0035,0.0030,0.0021, 0.0028]

plt.errorbar(x_values, y_values,  yerr=(y_low,y_up) ,fmt='o', markersize=10, capsize = 5)

plt.ylabel(r'$\mathrm{ R_{P}/R_{\star} }$', fontsize = 16)
plt.xlabel("Literature", fontsize = 16)
LABELS = ["TESS", "TASTE", "Anderson (2011)", "Addison (2019)", "Turner (2016)"]
plt.xticks(x_values, LABELS, fontsize = 14)
plt.show()



# K
# RV: 138+11−10
# Anderson: 138.8 ± 9.0
# Addison: 136.5 +10-9.6


x_values = [1,2,3]
y_values = [138,138.8,136.5]

y_low=[10,9,9.6]
y_up=[11,9,10]

plt.errorbar(x_values, y_values,  yerr=(y_low,y_up) ,fmt='o', markersize=10, capsize = 5)

plt.ylabel(r'K $\mathrm{ [m s^{-1}] }$', fontsize = 16)
plt.xlabel("Literature", fontsize = 16)
LABELS = ["Present study (RV)", "Anderson (2011)", "Addison (2019)"]
plt.xticks(x_values, LABELS, fontsize = 16)
plt.show()
