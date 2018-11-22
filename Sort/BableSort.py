def BableSort(A):
     '''冒泡排序算法：传入一个List，对list中的元素进行排序'''
    print('冒泡排序前的顺序：',A)
    length=len(A)
     for i in range(1,length):
         #rang=range(i)
         #for j in reversed(rang):
         for j in range(i,0,-1): #range逆序遍历
             if A[j-1]> A[j]:
                 temp=A[j]
                 A[j]=A[j-1]
                 A[j-1]=temp
 
     print('冒泡排序后的顺序：',A)
     # 冒泡排序时间复杂度为：n^2,空间复杂度1，相同元素保持相对不变性
 if __name__=='__main__':
     listA=[1,5,7,3,4,6,7,8,9,9,15,10,4]
     alist = [54,26,93,17,77,31,44,55,20]
     BableSort(listA)