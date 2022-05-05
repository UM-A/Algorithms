'''
INSERTION SORT
'''

def insertion_sort_nondecreasing(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while (i>=0 and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

def insertion_sort_nonincreasing(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while(i>=0 and A[i]<key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

'''
MERGE SORT
'''

def merge(A,L,R):
    '''
    #Merge with sentiinels
    
    L.append(1000)
    R.append(1000)

    i=0
    j=0

    for k in range(len(A)):
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
    '''


    #Without Sentinels
    i = 0
    j = 0
    k = 0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1
 
    

def merge_sort(A):
    if len(A)>1:
        middle=len(A)//2
        L=A[:middle]
        R=A[middle:]
        merge_sort(L)
        merge_sort(R)
        merge(A,L,R)
    return A

