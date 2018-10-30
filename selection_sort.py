import sys

def selection_sort_practice(source_list):
    source_length = len(source_list)
    for i in range(source_length):
        minimum = i
        for j in range(i+1, source_length):
            if source_list[j] < source_list[minimum]:
                minimum = j
        source_list[i],source_list[minimum] = source_list[minimum],source_list[i]
    return source_list

if __name__== "__main__":

    number_of_element = int(input("Enter List Size:"))       
    source_list = []

    for i in range(int(number_of_element)):
        source_list.append(int(input("Enter %s Element Value:" % str(i+1))))

    print("Output Index: %s" % selection_sort_practice(source_list))