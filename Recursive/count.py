# 计算列表中包含的元素数量（递归思想）
def count_items(lst):
    if not lst:
        return 0
    else:
        lst.pop()
        return 1+count_items(lst)

l=[1,2,3,4,5,6,7,8,9,10]
print(count_items(l))

# 更简洁的写法
def count(lst):
    if lst==[]:
        return 0
    return 1+count(lst[1:])
l2=[1,2,3,4,5,6,7,8,9,10]      
print(count(l2))

     
