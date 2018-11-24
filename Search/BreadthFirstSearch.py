# 广度优先搜索(队列结构)
# 解决两类问题：
    #1.图中A--->B是否能存在路径？
    #2.图中A--->B最短的路径是哪条？

# eg.查找一个人的朋友交际圈是否存在芒果销售商
# 图结构的存储：散列表（Python中的dict结构）
graph={}
graph['you']=['Alice','Bob','Charles']
graph['Alice']=['Anuj','Peggy']
graph['Bob']=['Peggy']
graph['Charles']=['Thom','Jonny']
graph['Anuj']=[]
graph['Peggy']=[]
graph['Thom']=[]
graph['Jonny']=[]

# 广度优先搜索图中的节点
def BFS(name):
    from collections import deque #Python中的双端队列
    search_queue=deque()# 待搜索队列
    search_queue+=graph[name]
    searched=[]# 记录已经搜索过的节点
    while search_queue:#待搜索队列不为空
        person=search_queue.popleft()#出队
        if person not in searched:
            if person_is_seller(person):
                print(person+' is a mango seller!')
                return True
            else:
                search_queue+=graph[person]# 将这个人的朋友加入待搜索队列
                searched.append(person)
    return False
    
# 判断一个人是不是芒果销售商
def person_is_seller(name):
    return name[-1]=='m'  
    
if __name__=='__main__':
    BFS('you')