def fmean(n,x):
    if n >= 10 and n <= 2500 and [x[i] > 0 and x[i] <= (10**5) for i in range(n)]:
        c = 0
        for i in range(0,n):
            c = c + x[i]
        meanVal = c/n 
    return meanVal

def fmed(n,x):
    x.sort()
    if n >= 10 and n <= 2500 and [x[i] > 0 and x[i] <= (10**5) for i in range(n)]:
        middle = int(n / 2)
        m = x[middle] + x[middle - 1]
        midVal = m / 2

    return midVal    

def fmode(n,x):
    if n >= 10 and n <= 2500 and [x[i] > 0 and x[i] <= (10**5) for i in range(n)]:
        a = []
        z = 0
        for j in range(0,n):
            z = x.count(x[j])
            a.append(z)
        
        aMax = max(a)
        b = []
        for k in range(0,n):
            if a[k] == aMax:
                b.append(x[k])
        
        if a.count(aMax) > 1:
            modeVal = min(b)
        else:
            modeVal = x[a.index(aMax)]

    return modeVal
    
n = int(input())
x = list(input().split())
for i in range(len(x)):
    x[i] = int(x[i])

m1 = fmean(n,x)
m2 = fmed(n,x)
m3 = fmode(n,x)

print(round(m1,1))
print(round(m2,1))
print(m3)
