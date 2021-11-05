import random
number = random.randint(1,100)
n=int(input("Please Enter Your Number:"))
while n!=number:    
    if n>number:
        print("decrease your number")
        n=int(input("Please Enter Your Number:"))

    else:
        print("increase your number")
        n=int(input("Please Enter Your Number:"))
print("your number is correct:")
    
