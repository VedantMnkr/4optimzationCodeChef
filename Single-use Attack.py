'''Problem
Chef is playing a video game, and is now fighting the final boss.

The boss has 

H health points. Each attack of Chef reduces the health of the boss by 

X.
Chef also has a special attack that can be used at most once, and will decrease the health of the boss by 

Y.

Chef wins when the health of the boss is 
≤
0
≤0.
What is the minimum number of attacks needed by Chef to win?

Input Format
The first line of input will contain a single integer 

T, denoting the number of test cases.
The first and only line of each test case will contain three space-separated integers 

H,X,Y — the parameters described in the statement.
Output Format
For each test case, output on a new line the minimum number of attacks needed by Chef to win. '''

t = int(input())
for i in range(t):
    bHealth, healthReducedByBasicAttack, healthReducedByUltimate = map(int, input().split())
    attacks = int(0)
    if(bHealth >0):
        bHealth = bHealth - healthReducedByUltimate
        attacks += 1
        while(bHealth > 0):
            bHealth -= healthReducedByBasicAttack
            attacks += 1 
    print(attacks)
