def InsertSort(A):
    '''插入排序算法：传入一个数组，对数组进行排序'''
    print('排序前的顺序：',A)
    length=len(A)
    for i  in range(1,length):#从第二个开始
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
            A[j+1]=key
    print('排序后的顺序：',A)
 	#插入排序时间复杂度:n^2,空间复杂度:1,相同元素保持相对不变性(相对位置不变)
 
if __name__=='__main__':
    listA=[1,5,7,3,4,6,7,8,9,9,15,10,4]
    InsertSort(listA)

