# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:38:06 2021

@author: pc
"""

import numpy as np

print("\nSimulation 1 \nModel: PARSEC, Method: 1 step\n")
print("Disclaimer:\nWISE photometric data not included\n")

fname="median_outdata.dat" 

age,mass,logg,rad,logrho,mbol,J,H,K,par,dist = np.genfromtxt(fname,dtype="float", \
   comments="#", usecols=(1,6,11,16,21,26,31,36,41,61,66), unpack=True)
    
age_68L, age_68U, mass_68L, mass_68U,logg_68L, logg_68U, rad_68L, rad_68U, logrho_68L, logrho_68U = np.genfromtxt(fname, dtype = "float", \
                            comments = "#", usecols=(2,3,7,8,12,13,17,18, 22,23), unpack = True)  

mbol_68L, mbol_68U, J_68L, J_68U, H_68L, H_68U, K_68L, K_68U, par_68L, par_68U, dist_68L, dist_68U = np.genfromtxt(fname, dtype = "float", \
                                                                                                                   comments = "#", usecols = (27,28,32,33,37,38,42,43,62,63,67,68), unpack = True)   
    
logL, logL_68L, logL_68U, Av, Av_68L, Av_68U, mu0, mu0_68L, mu0_68U = np.genfromtxt(fname, dtype= "float", \
                                                                                    comments="#", usecols=(46,47,48,51,52,53,56,57,58), unpack=True)
    
    
age_min = age - age_68L
age_plus = age_68U - age

mass_min = mass - mass_68L
mass_plus = mass_68U - mass   

logg_min = logg - logg_68L
logg_plus = logg_68U - logg

rad_min = rad - rad_68L
rad_plus = rad_68U - rad

logrho_min = logrho - logrho_68L
logrho_plus = logrho_68U - logrho

mbol_min = mbol - mbol_68L
mbol_plus = mbol_68U - mbol

J_min = J - J_68L
J_plus = J_68U - J

H_min = H - H_68L
H_plus = H_68U - H

K_min = K - K_68L
K_plus = K_68U - K

logL_min = logL - logL_68L
logL_plus = logL_68U - logL

Av_min = Av - Av_68L
Av_plus = Av_68U - Av

mu0_min = mu0 - mu0_68L
mu0_plus = mu0_68U - mu0

par_min = par - par_68L
par_plus = par_68U - par

dist_min = dist - dist_68L
dist_plus = dist_68U - dist


print("Age: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(age, age_plus, age_min))
print("Mass: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(mass, mass_plus, mass_min))
print("log g: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(logg, logg_plus, logg_min)) 
print("Radius: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(rad, rad_plus, rad_min))
print("log rho: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(logrho, logrho_plus, logrho_min)) 
print("Mbol: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(mbol, mbol_plus, mbol_min)) 
print("J: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(J, J_plus, J_min)) 
print("H: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(H, H_plus, H_min)) 
print("K: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(K, K_plus, K_min))
print("log L: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(logL, logL_plus, logL_min))
print("Av: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(Av, Av_plus, Av_min))
print("mu0: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(mu0, mu0_plus, mu0_min))
print("Parallax: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(par, par_plus, par_min)) 
print("Distance: {0:8.3f} +- ({1:5.3f}, {1:5.3f})".format(dist, dist_plus, dist_min)) 

 




 






