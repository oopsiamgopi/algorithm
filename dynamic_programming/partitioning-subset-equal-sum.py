def is_subset_sum_recursive(arbitary_list, n, equal_sum):
    if equal_sum == 0: 
        return True
    if n == 0 and equal_sum != 0: 
        return False
  
    # If last element is greater than sum, then  
    # ignore it 
    if arbitary_list[n-1] > equal_sum:
        return is_subset_sum_recursive(arbitary_list, n-1, equal_sum) 
  
    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''
      
    return is_subset_sum_recursive(arbitary_list, n-1, equal_sum) or is_subset_sum_recursive(arbitary_list, n-1, equal_sum-arbitary_list[n-1])

def find_partition (arbitary_list, n):
    sum_arbitary_list = sum(arbitary_list)
    '''
    If sum_arbitary_list is odd, 
    it can not be divided into 2 equal subset
    '''
    if sum_arbitary_list % 2 != 0:
        return False 

    # Find if there is subset with sum equal
    return is_subset_sum_recursive(arbitary_list, n, sum_arbitary_list // 2) 

arbitary_list = [3, 1, 5, 9, 12]
#arbitary_list = [1, 65]
n = len(arbitary_list)
if find_partition(arbitary_list, n) == True: 
    print ("Can be partitionable as equal sum") 
else: 
    print ("Can not be partitionable as equal sum") 