import random
e=random.randint(1,100)
yes=int(input("Please give me the lucky number."))
while yes !=e:
    yes=int(input("Please give me the lucky number."))
    if yes>e:
        print("Too much.")
    elif (yes<e):
        print("Too little")