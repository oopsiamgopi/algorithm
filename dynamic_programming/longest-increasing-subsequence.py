# Dynamic programming Python implementation of LIS problem 
  
# lis returns length of the longest increasing subsequence 
# in arr of size n 
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    LIS = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and LIS[i] < (LIS[j] + 1): 
                LIS[i] = LIS[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    print(LIS)
    maximum = 0  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , LIS[i]) 
  
    return maximum 
# end of lis function 
  
# Driver program to test above function 
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Length of LIS is", lis(arr) )