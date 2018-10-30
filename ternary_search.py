import sys
'''
"We need to know the start and end of the range. Lets call them Low and High.
LOW = 0
HIGH = n-1
1. Calculate SPLIT_SIZE = (LOW-HIGH)/3
2. Calulate MID1=LOW + SPLIT_SIZE -> Mid1
3. Calulate MID2=HIGH - SPLIT_SIZE -> Mid2
4. Check Check serach value in MID1 index & return if found & exit the program
5. Check Check serach value in MID2 index & return if found & exit the program
6. Check Search value(K) less than MID1 index. set HIGH=MID1-1 & repet from Step 1-8.
7. Check Search value(K) greater than MID2 index. set HIGH=MID2+1 & repet from Step 1-8.
8. Else set LOW=MID+1, HIGH=MID2-1 & repet from Step 1-6."

'''
def ternary_search_practice(low, high, source_list, search_value):
    global iteration_count
    iteration_count +=  1
    print("Iternation Level %s", str(iteration_count))
    if low<=high:
        split_size = (high-low)/3
        mid1 = low  + split_size
        mid2 = high - split_size

        if source_list[mid1] == search_value:
            return mid1
        if source_list[mid2] == search_value:
            return mid2

        if source_list[mid1] > search_value:
            return ternary_search_practice(low, mid1-1, source_list, search_value)
        elif source_list[mid2] < search_value:
            return ternary_search_practice(mid2+1, high, source_list, search_value)
        else:
            return ternary_search_practice(mid1+1, mid2-1, source_list, search_value)

    return -1

if __name__== "__main__":

    number_of_element = int(input("Enter List Size:"))
    search_value = int(input("Enter Search Value:"))
    
    source_list = []

    for i in range(int(number_of_element)):
        source_list.append(input("Enter %s Element Value:" % str(i+1)))

    low = 0
    high = len(source_list)-1
    iteration_count = 0
    print("Output Index: %s" % ternary_search_practice(low, high, source_list, search_value))