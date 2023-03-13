''' 
Problem Code:AVGPROBLEM
Not a very fancy question but I did it to try the 'Ternary Operator' here.
When you have some simple conditions to be checked you can use this one liner which not even looks good but is easy to understand.

'''

# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    
    print('YES') if (a+b)/2 > c else print('NO')
    
