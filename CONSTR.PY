t = int(input())
for i in range(t):
    
    s = int(input())
    u = str(input())
    
    s_minimum = ''
    
    for i in range(len(u)):
        if u[i] != u[i-1]:
            s_minimum += u[i]
            
    print(s_minimum)
