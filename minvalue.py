# this is used for check the min value 
#array = [7 ,5,8,23,46]


# if i take input then what will be the answer

array = input("enter the array : \n")
minvalue = array[0]
for x in array :
    if x < minvalue :
        minvalue = x
        

print("minimum value is :" ,minvalue)


