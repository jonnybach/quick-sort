"""standford online course algorithms - quick_sort implementation"""
__author__ = 'jonathan'

from math import floor
import random
from merge_sort import sort

#file global pivot method variable
pvt_mthd = -9999
#number_of_compares = 0

# Generic Swap for manipulating list data.
def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp    

def med_three(arr, left, right):
    mid = floor((left + right)/2)
    if arr[right] < arr[left]:
        swap(arr, left, right)        
    if arr[mid] < arr[left]:
        swap(arr, mid, left)
    if arr[right] < arr[mid]:
        swap(arr, right, mid)
    return mid

def my_med_three(numbers, imin, imax):
    diff = (imax - imin + 1)
    if diff <= 2:
        pvt_indx = imin
    else:
        ## commented out section of code did not give the same number of comparisons
        # as the test cases on the website, however taking the floor of the average
        # does???
        #med_indx = -9999
        #if (diff%2 == 0):
        #    med_indx = floor((diff-1)/2) + imin
        #else:
        #    med_indx = floor(diff/2) + imin
        med_indx = floor((imin + imax)/2)
        #print("\nmedian indices: {0:d}, {1:d}, {2:d}".format(imin, med_indx, imax))
        #print("median values: {0:d}, {1:d}, {2:d}".format(numbers[imin], numbers[med_indx], numbers[imax]))
        med_3 = sort( [numbers[imin], numbers[med_indx], numbers[imax]] )
        pvt_indx = numbers.index(med_3[1])
        #print("sorted values: {0:d}, {1:d}, {2:d}".format(med_3[0], med_3[1], med_3[2]))
        #print("chosen index: {0:d}".format(pvt_indx))
        
    return pvt_indx

    
def choose_pivot(numbers, imin, imax,):
    '''Compute the number of comparisons (as in Problem 1), using the "median-of-three" 
    pivot rule. [The primary motivation behind this rule is to do a little bit of extra work 
    to get much better performance on input arrays that are nearly sorted or reverse sorted.] 
    In more detail, you should choose the pivot as follows. Consider the first, middle, and 
    final elements of the given array. (If the array has odd length it should be clear what 
    the "middle" element is; for an array with even length 2k, use the kth element as the 
    middle" element. So for the array 4 5 6 7, the "middle" element is the second 
    ne ---- 5 and not 6!) Identify which of these three elements is the median 
    (i.e., the one whose value is in between the other two), and use this as your pivot'''

    pvt_indx = -999
    
    if pvt_mthd == 1:
        #method 1 of pivot, always use 1st element
        pvt_indx = imin
    elif pvt_mthd == 2:
        #method 2 of pivot, use random pivot
        pvt_indx = imax
    elif pvt_mthd == 3:
        #method 3 of pivot, median of three
        pvt_indx = my_med_three(numbers, imin, imax)
        #pvt_indx = med_three(numbers, imin, imax)
    else:    
        #method random
        pvt_indx = random.randint(0, len(numbers)-1)

    return pvt_indx


def partition(numbers, imin, imax, pvt_indx):
   
    #check if pivot value is at first element, if not swap
    if (pvt_indx != imin):
        numbers[imin], numbers[pvt_indx] = numbers[pvt_indx], numbers[imin]
        pvt_indx = imin
        
    #initialize partition split position
    i = imin + 1
    
    #scan through all elements after pivot and partition based
    # on comparison to pivot value
    for j in range(imin+1, imax+1):
        if (numbers[j] < numbers[pvt_indx]):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
    
    #swap last left partitioned array element with pivot element
    numbers[i-1], numbers[imin] = numbers[imin], numbers[i-1]
    new_pvt_indx = i - 1
    
    return new_pvt_indx


def _quick_sort(numbers, imin, imax):
    
    global number_of_compares
    
    #since it is known that the partition routine will
    # make len-1 comparisons, store this value now
    my_compares = imax - imin
    number_of_compares = number_of_compares + my_compares
    
    if (my_compares <= 0):
        return 0
    
    #get pivot index
    pvt_indx = choose_pivot(numbers, imin, imax)
    
    #partition array into left and right sides about pivot
    pvt_indx = partition(numbers, imin, imax, pvt_indx)
    
    #recursively call quick_sort on left and right sides
    num_compares_lft = _quick_sort(numbers, imin, pvt_indx-1)
    num_compares_rt = _quick_sort(numbers, pvt_indx+1, imax)
    
    return (num_compares_lft + num_compares_rt + my_compares)


def quick_sort(numbers):
    return _quick_sort(numbers, 0, len(numbers)-1)


def run_quick_sort(numbers, answer):

    global number_of_compares
    number_of_compares = 0
    nmbrs_tmp = list(numbers)
    num_compares = quick_sort(nmbrs_tmp)
    
    print("total number of elements: {0:d}".format(len(numbers)))
    print("calculated total number of comparisons: {0:d}".format(num_compares))
    print("correct total number of comparisons:    {0:d}".format(answer))
    #print("global total number of comparisons:    {0:d}".format(number_of_compares))

    i = 0
    imax = min(len(nmbrs_tmp),100)
    print("first {0:d} sorted numbers:".format(imax))
    while i < imax:
        print("{0:d} ".format(nmbrs_tmp[i]),end='')
        i += 1
    print("\n", flush=True)


if __name__ == "__main__":
    
    numbers = list()
    
    test_case = 0
    
    if test_case == 0:
        #read in numbers from text file
        with open('IntegerArray.txt') as f:
            for line in f:
                numbers.append( int(line.strip('\n')) )
        answer_frst = -9999
        answer_last = -9999
        answer_median = -9999
                
    elif test_case == 1:
        #read in numbers from text file
        with open('IntArry10.txt') as f:
            for line in f:
                numbers.append( int(line.strip('\n')) )
        answer_frst = 25
        answer_last = 29
        answer_median = 21         
        
    elif test_case == 2:
        #read in numbers from text file
        with open('IntArry100.txt') as f:
            for line in f:
                numbers.append( int(line.strip('\n')) )
        answer_frst = 615
        answer_last = 587
        answer_median = 518        

    elif test_case == 3:
        #read in numbers from text file
        with open('IntArry1000.txt') as f:
            for line in f:
                numbers.append( int(line.strip('\n')) )
        answer_frst = 10297
        answer_last = 10184
        answer_median = 8921 
    
    pvt_mthd = 1
    run_quick_sort(numbers, answer_frst)
    
    pvt_mthd = 2
    run_quick_sort(numbers, answer_last)

    pvt_mthd = 3
    run_quick_sort(numbers, answer_median)