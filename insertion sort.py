# a =[2,1,4,3]
# n= len(a)
# i =0
# for i in range(n -i):
#     min_index = i
#     for j in range(n):
#         j=0
#         while a[i] < a[j]:
#             min_value = a[min_index]
#             j +=1

#             if j > n:
#                 break

       

# print ("sorted array :" ,a)



# # its not done


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)