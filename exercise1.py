addo=0
adde=0
count=0
n=int(input("Please Enter N Value:"))
for x in range(1,n+1):
    if x%2==0:
        adde=adde+x
        count=count+1
        
    elif x%2==1:
        addo=addo+x
print("odd number's sum are",addo)        
print("even number's avarage are",adde/count)        

    