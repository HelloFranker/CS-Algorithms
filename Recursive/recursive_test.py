# 数组求和的递归方法
# 如果列表为空，返回0
# 如果列表不为空，计算列表中第一个数字+数组中剩余其他的数字组成的数组
def sum_iter(lst):
    if not lst:# 列表为空
        return 0
    else:# 列表不为空
        return lst.pop(0)+sum_iter(lst)

l=[1,2,3,4,5,6]
print(sum_iter(l))


# 计算列表中包含的元素数量（递归思想）
def count_items(lst):
    if not lst:
        return 0
    else:
        lst.pop()
        return 1+count_items(lst)

l=[1,2,3,4,5,6,7,8,9,10]
print(count_items(l))


# 找出列表中最大的数字(递归思想)
def find_max(lst,max=0):
    if not lst:
        return max
    else:
        item=lst.pop(0)
        if max<item:
            max=item
        return find_max(lst,max=max)
l=[1,3,2,4,5,7,6,8,10,9,15,-6,36,99,12,87]
print(find_max(l))

     
