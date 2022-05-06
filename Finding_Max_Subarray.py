'''
MAX Crossing SubArray
'''

def find_max_crossing_subarray(A,low,mid,high):
    LS=float('-inf')
    total=0
    for i in range(mid,low-1,-1):
        total+=A[i]
        if total>LS:
            LS=total
            max_left=i
    RS=float('-inf')
    total=0
    for j in range(mid+1,high+1):
        total+=A[j]
        if total>RS:
            RS=total
            max_right=j

    return (max_left,max_right,LS+RS)




'''
Find Maximum SubArray
'''
def find_maximum_subarray(A,low,high):
    if high==low:
        return (low,high,A[low])

    else:
        mid=(low+high)//2
        (left_low,left_high,left_sum)=find_maximum_subarray(A,low,mid)
        (right_low,right_high,right_sum)=find_maximum_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=find_max_crossing_subarray(A,low,mid,high)
        
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)





if __name__=="__main__":
    A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print(find_maximum_subarray(A,0,len(A)-1))


    
