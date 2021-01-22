# Write a function that sorts a list of numbers in ascending order.
"""

The intuition:
As an overview, the array is superficially split into 2 segments, the sorted segment from lst[0] to lst[i-1], and the unsorted segment from lst[i] to lst[length of lst array - 1] (After the first iteration of the for loop, as that is when the first sorted element exists)
Once an element is put into the sorted segment, it is left untouched. 
The goal in the unsorted segment, is to find the minimum element, as it will be the next number to be placed onto the sorted segment. This is obvious when you consider that
all numbers on the sorted segment are smaller, and all numbers on the unsorted segment are bigger, than the minimum element found in the unsorted segment.
Because we do not care about the ordering of the unsorted segment, we can swap the minimum element into the ith position in the array, and the ith element into the minimum element's position. 
Eventually, afer stacking the smallest minimum element repeatedly on the sorted segment, the array will be sorted.

How the code works:
There are two functions which can be called, selectionSort and findMinIndex. Functions usually require parameters and in this case, an array lst is given for selectionSort and findMinIndex.
The for loop within the selectionSort function generates a iterator variable, which increases after a single loop, and ends after the last element index is produced.
The findMinIndex function is called and each time the array lst and iterator i is given. It's purpose is to find the minimum element's index position in the array.
FindMinIndex function is abstracted out of the selectionSort function for readability and clarity for the programmer/reader.
In the findMinIndex function the minIndex is assigned to the beginning of the unsorted segment of the array lst. Now within the while loop, elements are compared to find the minimum,
which if found, is assigned as the new minIndex. The j is iterated, to get the next element in the unsorted segment. Once the while loop is completed the minIndex is returned.
Once the minimum element postion is found, it swaps the elements at their respective positions.
This occurs until the loop is exitted, and the function returns the array lst.
"""

# Takes as imput an array of integers
def selectionSort(lst):
    for i in range(len(lst)):
        minIndex = findMinIndex(lst, i)

        # Swap
        temp = lst[i]
        lst[i] = lst[minIndex]
        lst[minIndex] = temp
    return lst

def findMinIndex(lst, i):
    minIndex = i
    j = i+1
    while j < len(lst):
        if lst[j] < lst[minIndex]:
            minIndex = j
        j += 1
    return minIndex

# standard test/multiple of equal elements
print(selectionSort([0,3,3,4,1,2,9,1,7,5]))
# empty test
print(selectionSort([]))
# single element test
print(selectionSort([1]))
# negative elements test
print(selectionSort([-11,-22,-33,44]))