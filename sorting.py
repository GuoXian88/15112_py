#sort
# sorting.py

import time, random

####################################################
# swap
####################################################

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

####################################################
# selectionSort
####################################################

def selectionSort(a):
    n = len(a)
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex+1, n):
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, startIndex, minIndex)

####################################################
# bubbleSort 遍历一下，如果不是小到大的顺序就换
####################################################

def bubbleSort(a):
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        #第一轮遍历一定能把最大的换到最右边，所以end可以-1,如果全都是从小到大的顺序，那么
        #可以不用换了swap为False
        for i in range(1, end):
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        end -= 1

####################################################
# mergeSort
####################################################



def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]
    print("merge: ", a)
#基本思路就是从第一个开始，然后先是数组中1个元素合并成两两一组的形式
#然后再step再乘2再把2 2一组的合并成4  4一组 再8 8一组...
def mergeSort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            print(start1, start2)
            merge(a, start1, start2, end)
        step *= 2 # 因为merge sort是log下降的

####################################################
# builtinSort (wrapped as a function)
####################################################

def builtinSort(a):
    a.sort()

####################################################
# testSort
####################################################

def testSort(sortFn, n):
    a = [random.randint(0,2**31) for i in range(n)]
    sortedA = sorted(a)
    startTime = time.time()
    sortFn(a)
    endTime = time.time()
    elapsedTime = endTime - startTime
    assert(a == sortedA)
    print("%20s n=%d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))

def testSorts():
    n = 2**8 # use 2**8 for Brython, use 2**12 or larger for Python
    for sortFn in [selectionSort, bubbleSort, mergeSort, builtinSort]:
        testSort(sortFn, n)

testSorts()