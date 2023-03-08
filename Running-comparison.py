'''Problem Code: RUNCOMPARE'''


t = int(input())
for i in range(t):
    
    n =  int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    
    happyDays = 0
    
    for a,b in zip(alice, bob):
        
        if(a<=(b*2) and b<=(a*2)):
            happyDays += 1 
            
    print(happyDays)
