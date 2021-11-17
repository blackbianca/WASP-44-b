import numpy as np 
#teff_val = np.asarray([5420.,5480.,5407.,5400.,5410.,5410.,], float)
#teff_err = np.asarray([100., 129.58,83.5,150., 150., 150.], float)

# not corrected for systematical error

#teff_avg, teff_std = np.average(teff_val, weights=1./teff_err**2, returned=True)
#np.average returns the sum of weights

# all the previous part was commented, since Anderson 2011 (discovery paper) is the only usable one
teff_avg = 5400
teff_std = np.sqrt(150**2 + 60**2)
# adding systematic contribution

print("Teff: {0:8.1f} +- {1:5.1f} K".format(teff_avg, teff_std))

#met_val = np.asarray([0.,0.06,0.], float)
#met_err = np.asarray([0.1,0.1,0.1], float)

#met_avg, met_std = np.average(met_val, weights=1./met_err**2, returned=True)
met_avg = 0.06
met_std = np.sqrt(0.1**2 + 0.04**2)
print("[Fe/H]: {0:8.3f} +- {1:5.3f}".format(met_avg, met_std))


#logg_val = np.asarray([4.49,4.45,4.48], float)
#logg_err = np.asarray([0.04,0.08,0.05], float)

#logg_avg, logg_std = np.average(logg_val, weights=1./logg_err**2, returned=True)
logg_avg = 4.5
logg_std = np.sqrt(0.2**2 + 0.1**2)
print("logg: {0:8.3f} +- {1:5.3f}".format(logg_avg, logg_std))


# just print the necessary parameters
par = 2.7644070     #GAIA eDR3
par_err = 0.0199208

#photometry
w1mpro = 11.246
w1mpro_err = 0.022

w2mpro = 11.301
w2mpro_err = 0.021

w3mpro = 11.345
w3mpro_err = 0.191

J = 11.702 
J_err = 0.023
H = 11.408
H_err = 0.025
K = 11.341
K_err =  0.026

print("J: {0:8.3f} +- {1:5.3f}".format(J, J_err))
print("H: {0:8.3f} +- {1:5.3f}".format(H, H_err))
print("K: {0:8.3f} +- {1:5.3f}".format(K, K_err))
print("Parallax: {0:8.3f} +- {1:5.3f}".format(par, par_err))
print("w1mpro: {0:8.3f} +- {1:5.3f}".format(w1mpro, w1mpro_err))
print("w2mpro: {0:8.3f} +- {1:5.3f}".format(w2mpro, w2mpro_err))
print("w3mpro: {0:8.3f} +- {1:5.3f}".format(w3mpro, w3mpro_err))


