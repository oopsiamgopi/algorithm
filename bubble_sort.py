import sys

def bubble_sort_practice(source_list):
    source_length = len(source_list)
    for i in range(source_length):
        for j in range(source_length-i-1):
            if source_list[j] > source_list[j+1]:
                source_list[j],source_list[j+1] = source_list[j+1],source_list[j]
    return source_list

if __name__== "__main__":

    number_of_element = int(input("Enter List Size:"))       
    source_list = []

    for i in range(int(number_of_element)):
        source_list.append(int(input("Enter %s Element Value:" % str(i+1))))

    print("Output Index: %s" % bubble_sort_practice(source_list))