import time
import random

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def orderStatistics(arr, i):
    if len(arr) <= 5:
        A = insertionSort(arr)
        return A[i]
    
    groupsOf5 = []
    j = 0
    while j < len(arr):
        groupsOf5.append(insertionSort( arr[j : j  + 5] ))
        j += 5
    medians = []

    for group in groupsOf5:
        medians.append( group[ len(group) // 2] )
    
    if len(medians) <= 5:
        pivot = medians[ len(medians) // 2 ]
    else:
        pivot = orderStatistics(medians, len(medians) // 2)
    
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    
    k = len(low)
    
    if i < k:
        return orderStatistics(low, i)
    elif i < k + len(middle):
        return pivot
    else:
        return orderStatistics(high, i - k - len(middle))


def runTests():
    sampleSizeN = [100, 300, 500, 1000, 2000, 4000, 5000, 8000, 10000]
    populationSizeN = [100, 300, 500, 1000, 2000, 4000]
    for n in range(len(sampleSizeN)):
        print("|=================================================================================|")
        for popN in range(len(populationSizeN)):
            print(f"For Sample Size: {sampleSizeN[n]} and Population Size: {populationSizeN[popN]}")
            theArray = [random.randint(1, populationSizeN[popN]) for x in range(sampleSizeN[n])]
            for ith in range(6):
                i = random.randint(0, sampleSizeN[n])
                print("Find ith number:", i + 1, "(th/rd) number")
                start = time.time()
                theIthNum = orderStatistics(theArray, i)
                timeTook = start - time.time()
        
                print("The", i + 1, "(th/rd) number is", theIthNum)
                print(f"RunTime =  {round(timeTook, 4)} Seconds")
            print("|=================================================================================|")

if __name__ == "__main__":
    runTests()