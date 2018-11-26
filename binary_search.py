import sys
#Work with sorted list
def binary_search_practice(low, high, source_list, search_value):
    if low<=high:
        mid=(low+high)/2
        if source_list[mid] < search_value:
            low = mid +1
            return binary_search_practice(low, high, source_list, search_value)
        elif source_list[mid] > search_value:
            high = mid-1
            return binary_search_practice(low, high, source_list, search_value)
        else:
            return mid
    return -1

if __name__== "__main__":

    number_of_element = int(input("Enter List Size:"))
    search_value = int(input("Enter Search Value:"))
    
    source_list = []

    for i in range(int(number_of_element)):
        source_list.append(input("Enter %s Element Value:" % str(i+1)))

    low = 0
    high = len(source_list)-1
    print("Output Index: %s" % binary_search_practice(low, high, source_list, search_value))