a = [23,57,4,89]
n = len(a)
i =0
for i in range(n-i):
    min_indexn=i
    for j in range(i+1 ,n):
        if a[j] < a[min_indexn]:
            min_indexn = j
    a[i],a[min_indexn] = a[min_indexn],a[i]

print("sorting array:" , a)