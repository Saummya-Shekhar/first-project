def main():
  x = int(input("Enter your number "))
  Prime(x)

def Prime(x):
i=2
m=0
for _ in range(x-2):
    if x%i != 0:
        m = m+1
        i = i+1

if m == x-2:
    print("This number is prime")
else:
    print("This number is not prime")
