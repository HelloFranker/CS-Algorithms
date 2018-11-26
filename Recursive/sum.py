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


# 更简洁的写法
def sum(lst):
    if lst == []:
        return 0
    return lst[0]+sum(lst[1:])

l2=[1,2,3,4,5,6]
print(sum(l2))

     
