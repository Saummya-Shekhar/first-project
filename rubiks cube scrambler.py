import random
n = random.randint(15,25)
moves = ["R","L","F","B","U","D","R2","L2","F2","B2","U2","D2","R(prime)",
             "L(prime)","F(prime)","B(prime)","U(prime)","D(prime)"]
scramble = []

def check_scramble():
    for k in range(n-1):
        first = scramble[k]
        second = scramble[k+1]
        if first[0] == second[0]:
            corrector()
            check_scramble()
                
def corrector():
    for k in range(n-1):
        first = scramble[k]
        second = scramble[k+1]
        if first[0] == second[0]:
            x = random.randint(0,17)
            ad = moves[x]
            scramble[k] = ad

def scrambler():
    for i in range(n):
        x = random.randint(0,17)
        ad = moves[x]
        scramble.append(ad)

    check_scramble()
            
    for _ in scramble:
        print(_ , end=" ")

            
scrambler()

    
















    