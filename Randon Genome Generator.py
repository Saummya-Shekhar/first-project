import random

Letters = ["A","T","G","C"]
x = int(input("Enter The Length(multiple of 3) of Genome Sequence: "))
Body = []
for i in range(x-6):
    Body.append(Letters[random.randint(0,3)])

def check(Body):
    for i in range(0,x-6,3):
        if Body[i:i+3] in [["T","A","G"], ["T","A","A"], ["T","G","A"]]:
            corrector(Body, i)
            check(Body)

def corrector(Body,i ):
    X = ""
    X = Letters[random.randint(0,3)]
    if X != Body[i]:
        Body[i] = X
    else:
        corrector(Body, i)


check(Body)
body = ""
for i in Body:
    body += i
Genome = "ATG" + body + "TAG"
print(Genome)
