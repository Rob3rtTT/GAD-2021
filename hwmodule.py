def sum(n):
    s=0
    for i in range(n+1):
        s+=i
    print(s)

def even_sum(n):
    s=0
    for i in range(n+1):
        if i%2==0:
            s+=i
    print(s)

def uneven_sum(n):
    s=0
    for i in range(n+1):
        if i%2!=0:
            s+=i
    print(s)
