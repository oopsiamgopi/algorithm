def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in xrange(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    print("Length of LCS is ", L[m][n])

    #longent Sequence List
    longest_sequence = []
    i,j = m,n
    while i!=0 and j!=0:
        current_value = L[i][j]
        if current_value>L[i-1][j] and current_value>L[i][j-1]:
            i-=1
            j-=1
            longest_sequence.append(X[current_value+1])
        elif current_value==L[i-1][j]:
            i-=1
        elif current_value==L[i][j-1]:
            j-=1
    print("Sequence", "".join(longest_sequence[::-1]))

X = "AGGTAB"
Y = "GXTXAYB"
lcs(X, Y)