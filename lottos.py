from scipy.special import comb
import csv

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


def indextocomb( ind, k=6, n=45):
    subs = k
    var = 0
    komb = []
    for var in range(k):

        while ( n>=subs ) and ( ind < comb(n,subs) ):
                n-=1

        if (n>=subs):
                komb.append(n+1)
                ind = ind - comb(n,subs)
        else:
                komb.append(subs)

        subs-=1

    komb.reverse()
    return komb


with open('/home/ebenkoc/Downloads/hatos.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    szamok=[]
    for row in reader:
        szamok.append(row[-7:-1])


def getmaxgap(items):
    ''' return from a sorted number list the max gap and the interval  '''
    maxgap = 0
    for i in range(1, len(items)):
        localmax = max(maxgap, items[i] - items[i - 1])
        if (localmax > maxgap):
            maxgap = localmax
            maxgapitem = i

    return maxgap, items[maxgapitem - 1], items[maxgapitem]


# a = [10, 20, 24, 26, 27, 300, 2900]
# print getmaxgap(a)
# getmaxgap.__doc__

a=[6, 18, 23, 34, 37, 44]
a=[1,2,3,4,5,6]
amax=[86,87,88,89]
b=[1,2,3,4,89]


c = combtoindex(indextocomb(485654)), indextocomb(6554565)
print c
#print comb(amax[0],len(amax)), scipy.special.binom(amax[0],len(amax))

print len(szamok), szamok[0]