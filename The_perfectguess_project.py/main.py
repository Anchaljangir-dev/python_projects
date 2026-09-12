import random
n = random.randint(1, 100)
a = -1
gussess = 1 
while(a!=n):
    gussess+=1
    a = int(input("guess the number :"))
    if(a>n):
        print("Guess lower please")
    
    elif(a<n):
        print("Guess higher please")
    else:
        print("correct guess!")

print(f"you have gussed the number {n} correctly in {gussess} attempts")