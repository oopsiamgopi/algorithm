def find_partition(arr):
    n = len(arr)
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False

    table=[[True]*(n+1)]
        
    for i in range(1,(total_sum//2)+1):
        table.append([False])

    for i in range(1,(total_sum//2)+1):
        for j in range(1, n+1):
            table[i].append(table[i][j-1])
            if i >= arr[j-1]:
                table[i][j] = table[i][j] or table[i - arr[j-1]][j-1]

    return table[total_sum//2][n]

arr = [3, 1, 1, 2, 2, 1]
arr = [3, 1, 5, 9, 12]

if find_partition(arr) == True: 
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")