a =[7 , 5 , 6 , 3]
n = len(a)
i = 0
for i in range(n-i): # type: ignore
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]

print ("sorted array is :" , a)

# where i is used for the paring value like ( 7,5) , (5,6) ,(6,3)

# the j value are use for  swaping to access the array