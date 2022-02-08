# Enter your code here. Read input from STDIN. Print output to STDOUT
def fquartile(n,x):
    x.sort()
    LH = []
    UH = []
    if n >= 5 and n <= 50 and [x[i] > 0 and x[i] <= (10**5) for i in range(n)]:
        if n%2 == 0:
            LH.append([x[i] for i in range(0,n//2)])
            LH = LH[0]
            UH.append([x[i] for i in range(n//2,n)])
            UH = UH[0]
            
            q2 = (x[(n//2) - 1] + x[(n//2)])/2
            if len(LH) % 2 == 0:
                q1 = (LH[(len(LH))//2] + LH[(len(LH)//2) - 1])/2
                q3 = (UH[(len(UH))//2] + UH[(len(UH)//2) - 1])/2
            else:
                q1 = LH[(len(LH))//2]
                q3 = UH[(len(UH))//2]
        else:
            LH.append([x[i] for i in range(0,n//2)])
            LH = LH[0]
            UH.append([x[i] for i in range((n//2)+1,n)])
            UH = UH[0]
            
            q2 = x[n//2]
            if len(LH) % 2 == 0:
                q1 = (LH[(len(LH))//2] + LH[(len(LH)//2) - 1])/2
                q3 = (UH[(len(UH))//2] + UH[(len(UH)//2) - 1])/2
            else:
                q1 = LH[(len(LH))//2]
                q3 = UH[(len(UH))//2]


    return q1,q2,q3

n = int(input())
x = list(input().split())
for i in range(n):
    x[i] = int(x[i])

q1,q2,q3 = fquartile(n,x)

print(int(q1))
print(int(q2))
print(int(q3))
