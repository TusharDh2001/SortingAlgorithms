def merge_sort(arr):
    if len(arr) >1:
        mid =len(arr) //2
        l=arr[:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i <len(l) and j< len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k] =r[j]
            j+=1
            k+=1


if __name__ == "__main__":
    arr=[41,9,3,25,28,39,19,47,4,50,21,8]
    merge_sort(arr)
    print(f"Sorted array is :{arr}")
