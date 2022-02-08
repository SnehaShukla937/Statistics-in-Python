def fweightedMean(n,x,w):
    if n >= 5 and n<= 50:
        c = 0
        t = 0
        for i in range(n):
            if x[i] > 0  and x[i] <= 100 and w[i] > 0 and w[i] <= 100:
                num = x[i] * w[i]
                c = c + num
                t = t + w[i]
        mw = c / t

    return mw



n = int(input())
x = list(input().split())
w = list(input().split())

for i in range(n):
    x[i]= int(x[i])
    w[i]= int(w[i])

mw = fweightedMean(n,x,w)

print(round(mw,1))
