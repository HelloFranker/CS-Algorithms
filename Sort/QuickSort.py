# 利用快排对数组进行排序
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if  i<=pivot]
        greater=[i for i  in arr[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

if __name__=='__main__':
    arr=[1,4,2,3,6,8,5,4,9]
    print(quick_sort(arr))