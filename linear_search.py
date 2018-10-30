import sys

def linear_search_practice(source_list, search_value):
    last_index = -1
    for index in range(len(source_list)):
        if source_list[index] == search_value:
            last_index = index
    return last_index

if __name__== "__main__":

    number_of_element = int(input("Enter List Size:"))
    search_value = int(input("Enter Search Value:"))
    
    source_list = []

    for i in range(int(number_of_element)):
        source_list.append(input("Enter %s Element Value:" % str(i+1)))

    print("Output Index: %s" % linear_search_practice(source_list, search_value))