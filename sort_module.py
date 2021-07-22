def bubble(list):
    
    swap = True
    n = len(list)
    while swap == True:
        for i in range(n - 1):
            for j in range(0, n - i - 1 ):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                else:
                    swap = False
    return list

def selection(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

def mergeSort(lst):
    if len(lst) > 1:
        firstHalf = lst[:len(lst) // 2]
        mergeSort(firstHalf)
        
        secondHalf = lst[len(lst) // 2 :]
        mergeSort(secondHalf)
        
        return merge(firstHalf,secondHalf,lst)
        
def merge(list1, list2, temp):
    current1 = 0
    current2 = 0
    current3 = 0
    
    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1
    
    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1
        
    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1

    return temp

def insertion(list):
    for i in range(1, len(list)):
        currentElement = list[i]
        k = i - 1
        while k >= 0 and list[k] > currentElement:
            list[k + 1] = list[k]
            k -= 1
        list[k + 1] = currentElement
    return list

def quickSort(list):
   quickSortHelper(list, 0, len(list) - 1)
    
def quickSortHelper(list, first, last):
    if last > first:
        pivotIndex = partition(list, first, last)
        quickSortHelper(list, first, pivotIndex - 1)
        quickSortHelper(list, pivotIndex + 1, last)
        
def partition(list, first, last):
    pivot = list[first]
    low = first + 1
    high = last
    
    while high > low:
        while low <= high and list[low] <= pivot:
            low += 1
            
        while low <= high and list[high] > pivot:
            high -= 1
            
        if high > low:
            list[high], list[low]= list[low], list[high]
            
    while high > first and list[high] >= pivot:
        high -= 1
        
    if pivot > list[high]:
        list[first] = list[high]
        list[high] = pivot
        return high
    else:
        return first
    
    
def main():
    list = [125.38, 1000.1, -5.821, 8, -23, 0.0076]
    print(bubble(list))
    
main()