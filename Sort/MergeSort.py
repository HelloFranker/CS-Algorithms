# 归并排序，对数组进行排序
def MergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2#精确除法，取小于等于结果的最大整数，相当于对结果进行向下取整
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        MergeSort(lefthalf)#递归调用左半部分
        MergeSort(righthalf)#递归调用右半部分
 
        #合并过程
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
 
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
 
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
     # 归并排序算法时间复杂度：n*lgn,空间复杂度:n,相同元素保持顺序不变性
     
if __name__=='__main__':
    listA=[1,5,7,3,4,6,7,8,9,9,15,10,4]
    MergeSort(listA)