#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    
    def __init__(self):
        self.root = Node(None,None)

    # 入栈
    def push(self, data):
        top = self.root
        while top.next != None:
            top = top.next
        top.next = Node(data,None)

    # 出栈
    def pop(self):
        if self.is_empty():
            return None
        top = self.root.next
        if top.next != None:
            self.root.next = top.next
        else:
            self.root.next = None
        return top

    # 返回队列的大小
    def size(self):
        top = self.root.next
        size = 0
        while top != None:
            size = size + 1
            top = top.next
        return size

    # 判断队列是否为空
    def is_empty(self):
        if self.root.next == None:
            return True
        return False


if __name__=='__main__':
    queue=Queue()
    print("初始化状态")
    print("队列为空? %d"%queue.is_empty())
    print("打印当前队列的大小")
    print(queue.size())

    queue.push(2)
    queue.push(34)
    queue.push(21)
    queue.push(4)
    print("添加元素2,34,21,4 后")
    print("队列为空? %d"%queue.is_empty())
    print("打印当前队列的大小")
    print(queue.size())

    while queue.is_empty() == 0:
        tmp = queue.pop()  
        print("推出元素 %d 后"%tmp.data)
        print("打印当前队列的大小")
        print(queue.size())
