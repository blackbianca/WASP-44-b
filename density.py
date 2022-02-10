import numpy as np

R_Rj = 1.057139
sigma_R=(0.027212+0.027189)/2.

M_Mj =0.881943
sigma_M=(0.071550+0.074306)/2.

rhoj=1.3262
sigma_rhoj=0.0003

rho = M_Mj/R_Rj**3
sigma_rho = np.sqrt((rho/M_Mj)**2*sigma_M**2+(rho/R_Rj)**2*sigma_R**2)

print("rho[rho_j]",rho, "+-", sigma_rho)

#convert to g/cm^3
rho = rho*rhoj
sigma_rho = np.sqrt((rhoj*sigma_rho)**2+(rho*sigma_rhoj)**2)

print("rho[g/cm^3]",rho, "+-", sigma_rho)
