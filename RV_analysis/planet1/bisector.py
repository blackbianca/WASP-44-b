#We investigate the possibility of an unresolved eclipsing binary being the source of observed transits
import numpy as np
import numpy.random as rnd
from numpy.linalg import solve
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10})

def data_set(): 
    fname="WASP44_RV_PyORBIT.dat"
    RV, bisector=np.genfromtxt(fname,dtype=float, comments="#", usecols=(1,2),unpack=True)
    return RV, bisector


def poly_fit(x,y,m):
    A=np.zeros([m+1,m+1],float)
    b=np.zeros([m+1],float)

    for j in range(0,m+1):
        b[j]=sum(x**j*y)            #it's just the definition (in the slides we actually use k instead of j)
        for k in range(0,m+1):
            A[j][k]=sum(x**(j+k))   #again, just the definition (and again j and k are switched wrt the slides)
    
    # in both cases above the sum function substitutes the sum over the i index

    k=solve(A,b)
    return k

    # k is the vector of coefficients a for the polynomials

def least_square(x,y,k,m):

    N=len(x)
    ynew=np.zeros([N],float)

    for i in range(N):
        temp=0.0
        for j in range(len(k)):
            temp+=(k[j]*x[i]**j)
        ynew[i]=temp

    res = sum((y-ynew)*(y-ynew))

    sy = np.sqrt(res/(N-m))
   # sa= sy * np.sqrt(sx2/D)
   # sb= sy * np.sqrt(N/D)

    return ynew, res


m=1 #order of polynomial
x,y=data_set()

k=poly_fit(x,y,m)
ynew1,res1=least_square(x,y,k,m)


xvec=np.linspace(-4200,-3850,int(1e3))
yvec=np.polyval([k[1],k[0]],xvec)
a=plt.scatter(x,y,color="forestgreen",s=15)
b,=plt.plot(xvec,yvec,linestyle="-",color="black",linewidth="0.5")
plt.xlabel("RV [m/s]")
plt.ylabel("Bispector span")
plt.legend([a,b],["Data","Linear fit"+"\n"+"slope=0.0064"])
print(k[0],k[1])

plt.tight_layout()
plt.show()