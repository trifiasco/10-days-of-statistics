

cntA = 0
cntB = 0
cntAandB = 0

A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]

for a in A:
    for b in B:
        #if a != b:
           # cntA += 1
        #if a + b == 6:
            #cntB += 1
        if a != b and  a + b ==6:
            cntAandB += 1

print(cntA, cntB, cntAandB)
