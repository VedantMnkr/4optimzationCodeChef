# cook your dish here ATM2
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b=''
    for i in range(n):
        if k>=a[i]:
            k-=a[i]
            b+='1'
        else:
            b+='0'
    print(b)
