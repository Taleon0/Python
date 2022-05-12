# Forma 1

def numpat(n):
    num=1
    for i in range(0,n):
        num=1
        for j in range(0, i+1):
            print(num, end=' ')
            num = num+1
        print('\r')

numpat(5)

# Forma 2 -- recursiva

def numpat2(min,max):
    if min == max:
        print(min)
        return
    numpat2(min,max-1)
    print(*list(range(min,max+1)))

# numpat2(1,5)

# Forma 3

n=5
for i in range(1,n+1):pass
#    print(int(i*str(i)))