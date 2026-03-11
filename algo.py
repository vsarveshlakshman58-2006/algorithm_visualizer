def bubblesort(arr):
    n=len(arr)
    swap=1
    while(swap):
        swap=0
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=1
                yield arr



def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
            yield arr
        arr[j+1]=key
        yield arr
def premerge(arr):
    p = 0
    r = len(arr) - 1
    yield from mergesort(arr, p, r)


def merge(arr, p, q, r):

    left = arr[p:q+1]
    right = arr[q+1:r+1]

    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1
        yield arr

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr


def mergesort(arr, p, r):

    if p < r:

        q = (p + r) // 2

        yield from mergesort(arr, p, q)

        yield from mergesort(arr, q+1, r)

        yield from merge(arr, p, q, r)

def prequick(arr):
    low, high = 0, len(arr)-1
    yield from quicksort(arr, low, high)


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for k in range(low, high):

        if arr[k] < pivot:
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
            yield arr

    arr[i+1], arr[high] = arr[high], arr[i+1]

    yield arr

    return i+1


def quicksort(arr, low, high):

    if low < high:

        gen = partition(arr, low, high)

        while True:
            try:
                yield next(gen)
            except StopIteration as e:
                pi = e.value
                break

        yield from quicksort(arr, low, pi-1)

        yield from quicksort(arr, pi+1, high)


def maxheapify(arr,n,i):

    largest=i
    left=(2*i)+1
    right=(2*i)+2

    if left<n and arr[left]>arr[largest]:
        largest=left

    if right<n and arr[right]>arr[largest]:
        largest=right

    if largest!=i:

        arr[i],arr[largest]=arr[largest],arr[i]

        yield arr

        yield from maxheapify(arr,n,largest)


def buildmaxheap(arr):

    n=len(arr)

    for i in range((n//2)-1,-1,-1):

        yield from maxheapify(arr,n,i)


def heapsort(arr):

    n=len(arr)

    yield from buildmaxheap(arr)

    for i in range(n-1,0,-1):

        arr[0],arr[i]=arr[i],arr[0]

        yield arr

        yield from maxheapify(arr,i,0)



