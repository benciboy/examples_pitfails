import scipy
from scipy.special import comb
def combtoindex(arg):
    ''' az argumentum lista kombinaciohoz tarozo index kiszamitasa  '''
    arg.reverse()
    result = 0
    k = len(arg)
    for var in range(0,k):
        if ((arg[var]-1)<(k-var)) :
            result += 0
        else:
            result += comb(arg[var]-1,k-var)
    return int(result)



a=[6, 18, 23, 34, 37, 44]
a=[1,2,3,4,5,6]
amax=[86,87,88,89]
b=[1,2,3,4,89]


c = combtoindex(indextocomb(485654)), indextocomb(6554565)
print c
#print comb(amax[0],len(amax)), scipy.special.binom(amax[0],len(amax))