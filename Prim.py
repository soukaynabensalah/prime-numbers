n=int(input("entrer n : "))
for j in range(2,n) :
    for i in range(2,n-1) :
        if j%i!=0 :
            print(j)
            
