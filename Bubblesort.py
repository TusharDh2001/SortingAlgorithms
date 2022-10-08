#bubble sorting code i python
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],  arr[j+1] = arr[j+1], arr[j]


n=[]
num=int(input("Enter the number of elements in array :"))
for i in range(num):
    c=int(input())
    n.append(c)
bubble_sort(n)
print("sorted elements is :")
print(n)
