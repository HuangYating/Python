class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


class SingleLinkedList(object):
    # root初始化为哨兵
    def __init__(self):
        self.root = Node(None, None)


    # 遍历链表
    def iterate(self):
        top = self.root.next
        while top!=None:
            print(top.data) 
            top = top.next


    # 返回链表的大小
    def size(self):
        top = self.root.next
        size = 0
        while top != None:
            size = size + 1
            top = top.next
        return size


    # 查找值为data的第一个结点
    def find(self, data):
        top = self.root.next
        while top != None:
            if top.data == data:
                return top
            top = top.next
        return None


    # 查找值为data的结点的上一个结点
    def find_before(self, data):
        top = self.root 
        while top.next != None:
            if top.next.data == data :
                return top
            top = top.next
        return None

    # 修改第pos+1个结点的值为data
    def modify(self, pos, data):
        if 0 > pos or pos > self.size()-1:
            return  
        top = self.root.next
        while pos != 0:
            top = top.next
            pos = pos - 1 
        top.data = data


    # 在开头添加结点
    def add_at_beginning(self, data):
        node = Node(data, self.root.next)
        self.root.next = node   


    # 在结尾添加结点
    def add_at_end(self, data):
        # 先找到最后一个结点
        top = self.root
        while top.next != None:
            top = top.next
        #在结尾添加结点
        top.next = Node(data, None) 

        
    # 在指定结点node后插入新结点
    def insert_after(self, node, data): 
        top = self.root.next
        while top != None:
            if top == node:
                newNode = Node(data,top.next)
                top.next = newNode
                return 
            top = top.next

    # 在指定位置添加结点(0表示第一个位置)
    def insert_at(self, pos, data):
        if 0 > pos or pos > self.size():
            print("illegal position!")
        else:
            i = pos
            top = self.root
            while i != 0:
                top = top.next
                i = i - 1
            node = Node(data, top.next)
            top.next = node


    # 删除值为data的第一个结点
    def delete(self, data):
        top = self.root
        while top.next != None:
            if top.next.data == data:
                top.next = top.next.next
                return 
            else:
                top = top.next

    # 删除值为data的所有结点
    def delete_all(self, data):
        top = self.root
        while top.next != None:
            if top.next.data == data:
                top.next = top.next.next
            else:
                top = top.next
        return  

    # 判断链表是否为空
    def is_empty(self):
        if self.root.next == None:
            return True
        return False


if __name__=='__main__':
    s_l_list=SingleLinkedList()
    print("初始化状态")
    print("链表为空? %d"%s_l_list.is_empty())
    print("打印当前链表的大小")
    print(s_l_list.size())

    ''' 添加结点'''
    s_l_list.add_at_beginning(1)
    print("添加一个元素1后")
    print("链表为空? %d"%s_l_list.is_empty())
    print("打印当前链表所有值 ")
    s_l_list.iterate()

    print("在结尾添加结点2，8；在开头添加结点9，8  ")
    s_l_list.add_at_end(2)
    s_l_list.add_at_end(8)
    s_l_list.add_at_beginning(9)
    s_l_list.add_at_beginning(8)
    s_l_list.add_at_beginning(8)
    print("打印当前链表所有值 ")
    s_l_list.iterate()
    print("打印当前链表的大小")
    print(s_l_list.size())

    print("在第6个位置添加结点13 ")
    s_l_list.insert_at(5, 13)
    print("打印当前链表所有值 ")
    s_l_list.iterate()

    print("在第2个结点后添加结点100 ")
    node = s_l_list.root.next.next
    s_l_list.insert_after(node, 100)
    print("打印当前链表所有值 ")
    s_l_list.iterate()

    ''' 查找结点'''
    print("查找值为100的结点 ")
    node = s_l_list.find(100)
    print(node, node.data) 

    print("查找值为100的结点的前一个结点 ")
    node = s_l_list.find_before(100)
    print(node, node.data) 

    ''' 修改结点'''
    print("修改第4个结点的值为200 ")
    s_l_list.modify(3, 200)
    print("打印当前链表所有值 ")
    s_l_list.iterate() 

    ''' 删除结点'''
    print("删除值为8的第一个结点 ")
    s_l_list.delete(8)
    print("打印当前链表所有值 ")
    s_l_list.iterate()
    print("打印当前链表的大小")
    print(s_l_list.size())

    print("删除所有值为8的结点 ")
    s_l_list.delete_all(8)
    print("打印当前链表所有值 ")
    s_l_list.iterate()
    print("打印当前链表的大小")
    print(s_l_list.size())
