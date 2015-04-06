__author__ = 'User'
''' return the position of the element for a rotated array which was previously sorted
the only change is in the line with the condition         if((number > array[mid]) and (number < array[last])) :
In the normal binary search we would just have if(number > array[mid]) to get the new first position
But in this case we have to check if the last element is also less
This will work for both rotated as well regular sorted arrays.
'''
def print_result (result) :
    if (result != -1) :
        print "element  was found in position",result+1
    else :
        print "element not found"


def search_elem(array,number):
    first = 0
    last = array.__len__()
    last = last - 1
    while (first  < last):
        mid = (first+last)/2
        print "first:",first
        print "last:",last
        print "mid:",mid
        if array[mid] == number:
            return mid

        if(number <=array[last]) :
                if number < array[first]:
                    first = mid +1
                else  :
                    last = mid -1
        if(number >= array[first]) :
                if number > array[last]:
                    first = mid +1
                else  :
                    last = mid -1

    if(first == last):
        if (number == array[first]):
            return first
    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [4, 5, 6, 7, 8, 1, 2, 3]
c = [5, 6, 7, 1, 2, 3, 4]

print "b,2"
result = search_elem(b,2)
print_result(result)
