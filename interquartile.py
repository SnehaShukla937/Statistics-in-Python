# Enter your code here. Read input from STDIN. Print output to STDOUT
def getActualdata(n,x,f):
    a = []
    if n >= 5 and n <= 50:
        for i in range(n):
            if x[i] > 0 and x[i] <= 100 and f[i] > 0 and f[i] <= (10**3):
                for k in range(0,f[i]):
                 a.append(x[i])

    return a

def finterquartile(a):
    lh = []
    uh = []
    a.sort()
    l = len(a)
    if l%2 == 0:
        lh.append([a[j] for j in range(0,l//2)])
        uh.append([a[j] for j in range(l//2,l)])
        lh = lh[0]
        uh = uh[0]
        if len(lh)%2 == 0:
            q1 = (lh[len(lh)//2] + lh[(len(lh)//2)-1]) / 2
            q3 = (uh[len(uh)//2] + uh[(len(uh)//2)-1]) / 2
        else:
            q1 = lh[len(lh)//2]
            q3 = uh[len(uh)//2]
    else:
        lh.append([a[j] for j in range(0,l//2)])
        uh.append([a[j] for j in range((l//2)+1,l)])
        lh = lh[0]
        uh = uh[0]
        if len(lh)%2 == 0:
            q1 = (lh[len(lh)//2] + lh[(len(lh)//2)-1]) / 2
            q3 = (uh[len(uh)//2] + uh[(len(uh)//2)-1]) / 2
        else:
            q1 = lh[len(lh)//2]
            q3 = uh[len(uh)//2]
    
    return float(q3-q1)

n = int(input())
x = list(input().split())
f = list(input().split())
for i in range(n):
    x[i] = int(x[i])
    f[i] = int(f[i])
a = getActualdata(n,x,f)
iq = finterquartile(a)

print(round(iq,1))
