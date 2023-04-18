arr = [8, 1, 9, 6, 5, 4, 3, 2, 7]

test = list()
for i in range(0 , len(arr)):
    test.append(arr[i])
    print(test[i])

def heapSort(n):
    root = 0
    for i in range(0,len(n)):
        if i > len(n):
            print("end")
            return False
        else:
            temp = n[i]
            n[i] = list[root]
            list[root]


