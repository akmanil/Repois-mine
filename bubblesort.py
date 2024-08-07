my_array =[2,3,4,5,6]

n=len(my_array)
i=0
for i in range(n-i):
    swaped = False
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
            swaped = True
    if not swaped:
        break

print("sorted array is:",my_array)

