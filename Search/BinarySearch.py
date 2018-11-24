# 二分查找算法
# 前提条件：数组有序，顺序存储
# 时间复杂度O(logn)
def  binary_search(lst,item):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2 # 除法的结果自动向下取整
        guess=lst[mid]
        if guess==item:# 相等
            return mid
        elif guess <item:# 小了
            low=mid+1
        else:# 大了
            high=mid-1
    return None
l=[1,3,4,6,7,8,10,12,15,16,18,25,36,45]        
print(binary_search(l,12))