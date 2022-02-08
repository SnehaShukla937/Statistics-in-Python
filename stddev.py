def fstddev(n,x):
    if n >= 5 and n <= 100:
        mean = 0
        num  = 0
        for i in range(n):
            if x[i] > 0 and x[i] <= (10**5):
                mean = mean + x[i]
        meanVal = mean / n
        for i in range(n):
           num = num + ((x[i] - meanVal)**2)
        sd = ((num/n)**(1/2))
    return sd

n = int(input())
x = list(input().split())
for i in range(n):
    x[i] = int(x[i])

s = fstddev(n,x)

print(round(s,1))
