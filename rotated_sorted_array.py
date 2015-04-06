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
        #print "first:",first
        #print "last:",last

        if (last - first > 1) :
             mid = (first+last)/2
        else :
            if number == array[first]:
                return first
            else :
                if number ==array[last] :
                    return last
                else :
                    return -1
        #print "mid:",mid
        if array[mid] == number:
            return mid

        if (number <= array[last]) :
            first = mid
        else :
            last = mid
    if(first == last):
        if (number == array[first]):
            return first
    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [4, 5, 6, 7, 8, 1, 2, 3]
c = [5, 6, 7, 1, 2, 3, 4]

print "a,2"
result = search_elem(a,2)
print_result(result)

print "a,6"
result = search_elem (a,6)
print_result(result)

print "b,2"
result = search_elem(b,2)
print_result(result)

print "b,6"
result = search_elem (b,6)
print_result(result)

print "c,2"
result = search_elem(c,2)
print_result(result)

print "c,6"
result = search_elem (c,6)
print_result(result)

print "c,10"
result = search_elem (c,10)
print_result(result)

print "c,0"
result = search_elem (c,0)
print_result(result)
