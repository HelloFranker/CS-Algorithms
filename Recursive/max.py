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

     
# 更加简洁的写法
def max(lst):
    if len(lst)==2:
        return lst[0] if lst[0]>lst[1] else lst[1]
    sub_max=max(lst[1:])
    return lst[0] if lst[0]>sub_max  else sub_max
l2=[1,3,2,4,5,7,6,8,10,9,15,-6,36,99,12,87]     
print(max(l2))