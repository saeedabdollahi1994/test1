from time import clock
def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark

def HeapSort(A):
    def heapify(A):
        start = (len(A) - 2) / 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

    def siftDown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1

def shellSort(alist):
    sublistcount = n // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for k in range(start + gap, n, gap):

        currentvalue = alist[k]
        position = k

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

def bubbleSort(alist):
    for p in range(n-1,0,-1):
        for i in range(p):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def radixsort( alist ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    buckets = [list() for _ in range( RADIX )]

    # split aList between lists
    for  i in alist:
      tmp = i // placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False


    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        alist[a] = i
        a += 1

    placement *= RADIX
  return alist

a,b,c,d,e=0,0,0,0,0
i=input("i:")
n=input("n:")
import random
alist = [None] * n
for x in range(i):
 for j in range(n):
      alist[j] = random.randint(0, 10)
 clock()
 bubbleSort(alist)
 a =a+clock()

 clock()
 shellSort(alist)
 b=b+clock()

 clock()
 HeapSort(alist)
 c=c+clock()

 clock()
 quickSort(alist)
 d=d+clock()

 clock()
 radixsort(alist)
 e=e+clock()


print("bubble sort:")
print(a)
print("shell sort:")
print(b)
print("heap sort:")
print(c)
print("quick sort:")
print(d)
print("radix sort:")
print(e)




